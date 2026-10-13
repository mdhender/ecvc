"""Shared parsing for the rule book reorganization scripts.

Reads docs/rulebook.md and docs/mapping.md. Used by build.py and check.py.
"""

import os
import re
from dataclasses import dataclass, field

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
DOCS = os.path.join(ROOT, "docs")
RULEBOOK = os.path.join(DOCS, "rulebook.md")
MAPPING = os.path.join(DOCS, "mapping.md")
MANUAL = os.path.join(DOCS, "manual.md")
VARIANTS = os.path.join(DOCS, "variants.md")

# Lines the build writes that are not rule book text. The check ignores them.
VARIANTS_NOTE = [
    "This document holds the variant games of Empyrean Challenge: Maxi-Challenge and The Ten Planet War.",
    "The core rules are in [manual.md](manual.md).",
    "Like the rest of `docs/`, it is licensed under CC BY-NC-ND 4.0; see [LICENSE](LICENSE).",
]
B1_PLACEHOLDER = "The walkthrough of a turn is written in phase 6 of the reorganization."

HEADING_RE = re.compile(r"^(#{1,6}) (.*?)\s*$")
FENCE_RE = re.compile(r"^```")
LINK_RE = re.compile(r"\[([^\]]*)\]\(([^)\s]*)\)")
ANCHOR_RE = re.compile(r'<a id="([^"]+)"></a>')
NUMBERED_RE = re.compile(r"^(\d+(?:\.\d+)*)\.? (.*)$")
APPENDIX_RE = re.compile(r"^APPENDIX (I+): (.*)$")
ID_RE = re.compile(r"^([A-Z])(\d+(?:\.\d+)*)$")


def slugify(text):
    """GitHub's heading anchor: lower case, punctuation dropped, spaces to hyphens."""
    text = text.strip().lower()
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


def heading_slugs(lines):
    """All GitHub heading anchors in a file, with -1, -2 suffixes for repeats."""
    seen = {}
    slugs = []
    for kind, _, payload in scan(lines):
        if kind != "heading":
            continue
        base = slugify(payload[1])
        n = seen.get(base, 0)
        slugs.append(base if n == 0 else f"{base}-{n}")
        seen[base] = n + 1
    return slugs


def scan(lines):
    """Yield (kind, index, payload) for each line, tracking code fences.

    kind is "heading" (payload = (level, text)), "fence", "code", or "text".
    """
    in_fence = False
    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence
            yield "fence", i, line
        elif in_fence:
            yield "code", i, line
        else:
            m = HEADING_RE.match(line)
            if m:
                yield "heading", i, (len(m.group(1)), m.group(2))
            else:
                yield "text", i, line


def read_lines(path):
    with open(path, encoding="utf-8") as f:
        return f.read().split("\n")


@dataclass
class Section:
    """One rule book heading and the body text under it, up to the next heading."""
    line: int  # 1-based line number of the heading
    level: int
    text: str  # heading text as written
    key: str  # "3.1", "App. I", or the heading text when unnumbered
    title: str  # heading text without the number
    numbered: bool
    slug: str
    body: list = field(default_factory=list)


def parse_rulebook(lines):
    sections = []
    slugs = heading_slugs(lines)
    current = None
    for kind, i, payload in scan(lines):
        if kind == "heading":
            level, text = payload
            m = NUMBERED_RE.match(text)
            a = APPENDIX_RE.match(text)
            if m:
                key, title, numbered = m.group(1), m.group(2), True
            elif a:
                key, title, numbered = f"App. {a.group(1)}", a.group(2), True
            else:
                key, title, numbered = text, text, False
            current = Section(i + 1, level, text, key, title, numbered, slugs[len(sections)])
            sections.append(current)
        elif current is not None:
            current.body.append(lines[i])
    for s in sections:
        while s.body and not s.body[0].strip():
            s.body.pop(0)
        while s.body and not s.body[-1].strip():
            s.body.pop()
    return sections


@dataclass
class Row:
    id: str
    title: str
    source: str  # rule book column; blank for new headings and unnumbered sections
    notes: str
    subject: str


@dataclass
class Unmapped:
    source: str
    title: str
    reason: str


def split_row(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def parse_mapping(lines):
    """Return (subjects, rows, unmapped).

    subjects is a list of (letter, title); rows is the list of Row in table order.
    """
    subjects, rows, unmapped = [], [], []
    subject = None
    header = None
    for line in lines:
        m = re.match(r"^## ([A-Z])\. (.*)$", line)
        if m:
            subject = (m.group(1), m.group(2))
            subjects.append(subject)
            header = None
            continue
        if line.startswith("## "):
            subject = "unmapped" if line.strip() == "## No manual ID" else None
            header = None
            continue
        if not line.startswith("|") or subject is None:
            continue
        cells = split_row(line)
        if header is None:
            header = cells
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        rec = dict(zip(header, cells))
        if subject == "unmapped":
            unmapped.append(Unmapped(rec["Rule book"], rec["Title"], rec["Reason"]))
        else:
            rows.append(Row(rec["Manual ID"], rec["Title"], rec["Rule book"], rec["Notes"], subject[0]))
    return subjects, rows, unmapped


def id_numbers(rule_id):
    return ID_RE.match(rule_id).group(2).split(".")


def heading_level(rule_id):
    """Heading depth rule from REORG.md: X.0 is level 2, else one more than the count of numbers."""
    nums = id_numbers(rule_id)
    if len(nums) == 2 and nums[1] == "0":
        return 2
    return len(nums) + 1


def doc_for(rule_id):
    return "variants.md" if rule_id.startswith("V") else "manual.md"


def anchor(rule_id):
    return f"rule-{rule_id}"


class Model:
    """The rule book and mapping, joined."""

    def __init__(self):
        self.rulebook_lines = read_lines(RULEBOOK)
        self.sections = parse_rulebook(self.rulebook_lines)
        self.subjects, self.rows, self.unmapped = parse_mapping(read_lines(MAPPING))
        self.problems = []

        by_key = {}
        for s in self.sections:
            by_key.setdefault(s.key.lower(), []).append(s)
        self.by_key = by_key

        # Each mapping row and each "No manual ID" row claims one rule book section.
        self.row_section = {}
        self.claimed = {}
        for r in self.rows:
            if not r.source:
                # New headings claim nothing; unnumbered sections are matched by title.
                hits = [s for s in self.sections if not s.numbered and s.title.lower() == r.title.lower()]
                if hits:
                    self._claim(hits[0], ("row", r))
                    self.row_section[r.id] = hits[0]
                continue
            s = self._lookup(r.source, f"mapping row {r.id}")
            if s:
                self._claim(s, ("row", r))
                self.row_section[r.id] = s
        self.unmapped_section = {}
        for u in self.unmapped:
            s = self._lookup(u.source, f"No manual ID row {u.source}") if u.source else \
                self._lookup(u.title, f"No manual ID row {u.title}")
            if s:
                self._claim(s, ("unmapped", u))
                self.unmapped_section[id(u)] = s

        self.ids = {r.id: r for r in self.rows}
        # Rule book heading anchor -> manual ID, for link rewriting.
        self.slug_to_id = {}
        for rid, s in self.row_section.items():
            self.slug_to_id[s.slug] = rid

    def _lookup(self, key, who):
        hits = self.by_key.get(key.lower(), [])
        if len(hits) != 1:
            self.problems.append(f"{who}: {len(hits)} rule book headings match {key!r}")
            return None
        return hits[0]

    def _claim(self, section, owner):
        self.claimed.setdefault(section.line, []).append(owner)

    def folded_into(self, u):
        m = re.search(r"Folded into ([A-Z]\d+(?:\.\d+)*)", u.reason)
        return m.group(1) if m else None

    def rewrite_links(self, line, here):
        """Rewrite links into the rule book to manual anchors.

        here is the file the line will live in ("manual.md" or "variants.md").
        Returns (line, unresolved) where unresolved lists link targets with no manual ID.
        """
        unresolved = []

        def repl(m):
            text, target = m.group(1), m.group(2)
            if not target.startswith("#"):
                return m.group(0)
            rid = self.slug_to_id.get(target[1:])
            if rid is None:
                unresolved.append(target)
                return m.group(0)
            doc = doc_for(rid)
            prefix = "" if doc == here else doc
            return f"[{rid}]({prefix}#{anchor(rid)})"

        return LINK_RE.sub(repl, line), unresolved
