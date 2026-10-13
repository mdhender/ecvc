#!/usr/bin/env python3
"""Run the phase 5 checks from docs/REORG.md on docs/manual.md and docs/variants.md.

Also lists the plain-text section references (such as "See 5.2.2.") left for phase 4.
Exits 1 if any check fails.
"""

import os
import re
import sys
from collections import Counter

from build import Builder
from common import (
    ANCHOR_RE, CONCORDANCE, CONNECT, DOCS, LINK_RE, MANUAL, VARIANTS, VARIANTS_NOTE,
    Model, heading_level, heading_slugs, id_numbers, normalize_links, parse_connect,
    read_lines, scan, tutorials, errata,
)

RULE_HEADING_RE = re.compile(r"^([A-Z]\d+(?:\.\d+)*) (.*)$")
SUBJECT_HEADING_RE = re.compile(r"^([A-Z])\. ")
SECTION_REF_RE = re.compile(
    r"(?<![\d.])(\d{1,2}(?:\.\d{1,2})+)(?:,? step (\d+))?(?![\d%])"  # 5.2.2, 15.0, 16.2.4, step 5
    r"|[Cc]hapter (\d{1,2})\b"  # Chapter 9
    r"|\bsee (\d{1,2})\. [A-Z]"  # see 19. Espionage
    r"|\b[Ss]ee [A-Z]\w* \((\d{1,2})\)")  # See Combat (15)


class Doc:
    def __init__(self, path):
        self.path = path
        self.name = os.path.basename(path)
        self.lines = read_lines(path)
        self.slugs = set(heading_slugs(self.lines))
        self.anchors = []
        for line in self.lines:
            self.anchors += ANCHOR_RE.findall(line)
        # IDs of the numbered rule headings, including rules added since the rule book.
        self.rule_ids = set()
        for kind, i, payload in scan(self.lines):
            if kind == "heading":
                m = RULE_HEADING_RE.match(payload[1])
                if m:
                    self.rule_ids.add(m.group(1))
        # Line ranges (0-based, end exclusive) of top-level sections that are not rule text.
        self.skip = set()
        start = None
        for kind, i, payload in scan(self.lines):
            if kind != "heading" or payload[0] != 1:
                continue
            if start is not None:
                self.skip.update(range(start, i))
                start = None
            if payload[1] in ("Table of Contents", "Concordance"):
                start = i
        if start is not None:
            self.skip.update(range(start, len(self.lines)))

    def targets(self):
        return self.slugs | set(self.anchors)


def body_lines(lines, kinds_skip, extra_skip=()):
    for kind, i, payload in scan(lines):
        if kind == "heading" or i in kinds_skip:
            continue
        line = lines[i]
        if not line.strip():
            continue
        yield i, line


def compare_bodies(model, manual, variants):
    """Sorted body lines of manual + variants must equal those of the rule book."""
    rb_lines = model.rulebook_lines
    # Skip the rule book's table of contents and the bodies of deleted sections,
    # which have no manual ID; the concordance records them as deleted.
    deleted = {model.unmapped_section[id(u)].line - 1
               for u in model.unmapped if u.reason == "Deleted." and id(u) in model.unmapped_section}
    toc_skip = set()
    in_skip = False
    for kind, i, payload in scan(rb_lines):
        if kind == "heading":
            in_skip = payload[1] == "TABLE OF CONTENTS" or i in deleted
        if in_skip:
            toc_skip.add(i)
    expected = Counter()
    for i, line in body_lines(rb_lines, toc_skip):
        line, _ = model.rewrite_links(line, "manual.md")
        expected[line] += 1

    # The reviewed phase 4 edits in docs/connect.md are the only allowed differences.
    out = []
    edits, problems = parse_connect(read_lines(CONNECT))
    out += problems
    for e in edits:
        old = normalize_links(ANCHOR_RE.sub("", e.old))
        if expected[old] == 0:
            out.append(f"{e.where}: edit for {e.rule} replaces a line not in the rule book: {e.old!r}")
            continue
        expected[old] -= 1
        for new in e.new:
            if new.strip():
                expected[normalize_links(ANCHOR_RE.sub("", new))] += 1

    labels = {f"**{u.title}**" for u in model.unmapped if model.folded_into(u)}
    generated = Builder(model).generated_lines()
    actual = Counter()
    where = {}
    for doc in (manual, variants):
        for i, line in body_lines(doc.lines, doc.skip):
            if line in labels or line in generated:
                continue
            line = ANCHOR_RE.sub("", line)
            if not line.strip():
                continue
            line = normalize_links(line)
            actual[line] += 1
            where.setdefault(line, f"{doc.name}:{i + 1}")
    missing = expected - actual
    extra = actual - expected
    rb_where = {}
    for i, line in body_lines(rb_lines, toc_skip):
        rb_where.setdefault(model.rewrite_links(line, "manual.md")[0], f"rulebook.md:{i + 1}")
    for line, n in sorted(missing.items(), key=lambda kv: rb_where.get(kv[0], "")):
        out.append(f"missing from manual/variants ({rb_where.get(line, 'from connect.md')}, x{n}): {line!r}")
    for line, n in sorted(extra.items(), key=lambda kv: where.get(kv[0], "")):
        out.append(f"only in manual/variants ({where.get(line)}, x{n}): {line!r}")
    return out


def check_links(docs):
    """Every relative link in docs resolves to a file, and every fragment to an anchor in it."""
    out = []
    loaded = {d.path: d for d in docs}
    for doc in docs:
        here = os.path.dirname(doc.path)
        rel = os.path.relpath(doc.path, DOCS)
        for kind, i, payload in scan(doc.lines):
            if kind in ("code", "fence"):
                continue
            for text, target in LINK_RE.findall(doc.lines[i]):
                if re.match(r"^[a-z]+:", target):
                    continue
                path, _, frag = target.partition("#")
                other = doc
                if path:
                    full = os.path.normpath(os.path.join(here, path))
                    if not os.path.exists(full):
                        out.append(f"{rel}:{i + 1}: missing file {path!r}")
                        continue
                    if not frag:
                        continue
                    if full not in loaded:
                        if not full.endswith(".md"):
                            out.append(f"{rel}:{i + 1}: cannot check anchor in {path!r}")
                            continue
                        loaded[full] = Doc(full)
                    other = loaded[full]
                if frag and frag not in other.targets():
                    out.append(f"{rel}:{i + 1}: unresolved link [{text}]({target})")
    return out


def check_anchors(model, manual, variants):
    out = []
    for doc in (manual, variants):
        counts = Counter(doc.anchors)
        for a, n in counts.items():
            if n > 1:
                out.append(f"{doc.name}: anchor {a!r} appears {n} times")
        for a in counts:
            if a in doc.slugs:
                out.append(f"{doc.name}: anchor {a!r} collides with a heading anchor")
    both = Counter(manual.anchors + variants.anchors)
    for a, n in both.items():
        if n > 1 and manual.anchors.count(a) == 1 and variants.anchors.count(a) == 1:
            out.append(f"anchor {a!r} appears in both manual.md and variants.md")
    for r in model.rows:
        doc = variants if r.id.startswith("V") else manual
        n = doc.anchors.count(f"rule-{r.id}")
        if n != 1:
            out.append(f"{r.id}: {n} anchors in {doc.name}")
    known = {f"rule-{r.id}" for r in model.rows}
    for doc in (manual, variants):
        new_rules = {f"rule-{rid}" for rid in doc.rule_ids}
        for a in doc.anchors:
            if a in known or a in new_rules:
                continue
            m = re.fullmatch(r"rule-(B3\.\d+)\.\d+", a)
            if not (m and m.group(1) in model.ids):
                out.append(f"{doc.name}: anchor {a!r} is not a rule, mapping row, or stage step")
    return out


def check_headings(model, manual, variants):
    out = []
    for doc in (manual, variants):
        lines = doc.lines
        parent_level = None
        for kind, i, payload in scan(lines):
            if kind != "heading":
                continue
            level, text = payload
            where = f"{doc.name}:{i + 1}"
            m = RULE_HEADING_RE.match(text)
            if m:
                # A rule from the mapping, or one added since the rule book.
                rid = m.group(1)
                nums = id_numbers(rid)
                if len(nums) > 5:
                    out.append(f"{where}: {rid} has more than five numbers")
                if level != heading_level(rid):
                    out.append(f"{where}: {rid} is level {level}, expected {heading_level(rid)}")
                if lines[i - 1] != f'<a id="rule-{rid}"></a>':
                    out.append(f"{where}: {rid} heading is not preceded by its anchor")
                if rid in model.ids and text != f"{rid} {model.ids[rid].title}":
                    out.append(f"{where}: heading {text!r} does not match mapping title")
                parent_level = level
            elif level == 1:
                if SUBJECT_HEADING_RE.match(text) is None and text not in (
                        "Foreword", "Table of Contents", "History of the Empyrean Cluster", "Concordance"):
                    out.append(f"{where}: unexpected level 1 heading {text!r}")
                parent_level = None
            else:
                if parent_level is None or level != parent_level + 1:
                    out.append(f"{where}: unnumbered heading {text!r} is level {level}, "
                               f"expected one below its rule")
    for r in model.rows:
        if len(id_numbers(r.id)) > 5:
            out.append(f"mapping: {r.id} has more than five numbers")
    return out


def check_concordance(model, concordance):
    out = []
    rows = Counter()
    for line in concordance.lines:
        m = re.match(r"^\| \[([^\]]+)\]\(rulebook\.md#([^)]+)\)", line)
        if m:
            rows[m.group(2)] += 1
    for s in model.sections:
        if s.numbered and rows[s.slug] != 1:
            out.append(f"concordance: rule book {s.key} appears {rows[s.slug]} times")
    return out


def plain_refs(model, docs):
    """Plain-text references to rule book section numbers, with the manual ID each should become."""
    sections = {s.key: s for s in model.sections if s.numbered}
    sec_to_id = {s.key: rid for rid, s in model.row_section.items()}
    unmapped = {u.source: u for u in model.unmapped if u.source}
    out = []
    for doc in docs:
        for kind, i, payload in scan(doc.lines):
            if kind != "text" or i in doc.skip:
                continue
            if doc.lines[i] in VARIANTS_NOTE:
                continue
            line = ANCHOR_RE.sub("", LINK_RE.sub("", re.sub(r"<!--.*?-->", "", doc.lines[i])))
            for m in SECTION_REF_RE.finditer(line):
                num, step = m.group(1) or m.group(3) or m.group(4) or m.group(5), m.group(2)
                key = num[:-2] if num.endswith(".0") and num[:-2] in sections else num
                if key not in sections:
                    continue
                if key in sec_to_id:
                    target = sec_to_id[key] + (f".{step}" if step else "")
                else:
                    subjects = sorted({rid[0] for k, rid in sec_to_id.items() if k.startswith(key + ".")})
                    target = f"no manual ID; its sections are in subject {' and '.join(subjects)}" \
                        if subjects else f"no manual ID ({unmapped[key].reason})"
                out.append(f"{doc.name}:{i + 1}: {m.group(0)!r} -> {target}    | {doc.lines[i].strip()}")
    return out


def main():
    model = Model()
    manual, variants, concordance = Doc(MANUAL), Doc(VARIANTS), Doc(CONCORDANCE)
    failed = False
    checks = [
        ("Body lines match the rule book", compare_bodies(model, manual, variants)),
        ("Links resolve", check_links([manual, variants, concordance] + [Doc(p) for p in tutorials() + errata()])),
        ("Anchors are unique and every mapping row has one", check_anchors(model, manual, variants)),
        ("Heading levels follow the depth rule", check_headings(model, manual, variants)),
        ("Every numbered rule book heading is in the concordance once", check_concordance(model, concordance)),
    ]
    for name, problems in checks:
        print(f"{'FAIL' if problems else 'ok  '} {name}")
        for p in problems:
            print(f"     {p}")
        failed = failed or bool(problems)
    refs = plain_refs(model, [manual, variants])
    print(f"\nPlain-text references for phase 4 ({len(refs)}):")
    for r in refs:
        print(f"  {r}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
