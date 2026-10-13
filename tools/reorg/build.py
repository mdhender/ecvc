#!/usr/bin/env python3
"""Build docs/manual.md and docs/variants.md from docs/rulebook.md and docs/mapping.md.

Copies rule book body text unchanged, except that links into the rule book
are rewritten to manual anchors. Prints any problems found in the mapping.
"""

import re
import sys

from common import (
    B1_TEXT, CONNECT, MANUAL, VARIANTS, VARIANTS_NOTE, Model, anchor, doc_for,
    heading_level, parse_connect, read_lines, slugify,
)

GLOSSARY = "A7.0"
FRONT_MATTER = ("Foreword", "Table of Contents", "History of the Empyrean Cluster")
STEP_RE = re.compile(r"^(\d+)\. ")


def title_case(text):
    small = {"a", "an", "and", "as", "at", "but", "by", "for", "in", "of", "on", "or", "the", "to", "vs"}
    words = text.lower().split(" ")
    out = []
    for i, w in enumerate(words):
        parts = w.split("-")
        parts = [p if (i > 0 and p in small) else p[:1].upper() + p[1:] for p in parts]
        out.append("-".join(parts))
    return " ".join(out)


class Builder:
    def __init__(self, model):
        self.m = model
        self.problems = list(model.problems)
        self.warnings = []
        # Unmapped headings become unnumbered subheadings of the mapped rule before them.
        self.subheadings = {}
        owner = None
        for s in model.sections:
            claims = model.claimed.get(s.line)
            if claims:
                kind, obj = claims[0]
                owner = obj.id if kind == "row" else None
                if len(claims) > 1:
                    self.problems.append(f"rule book line {s.line} {s.text!r} is claimed {len(claims)} times")
                continue
            if owner is None:
                self.problems.append(f"rule book line {s.line} {s.text!r} has no mapping row")
                continue
            self.subheadings.setdefault(owner, []).append(s)
        # Folded rows go at the end of the rule named in the reason, in rule book order.
        self.folded = {}
        for u in model.unmapped:
            target = model.folded_into(u)
            s = model.unmapped_section.get(id(u))
            if target is None:
                if s and s.body and u.title not in FRONT_MATTER and u.reason != "Deleted.":
                    self.warnings.append(
                        f"rule book {s.key} {s.title!r} has no manual ID but has body text "
                        f"(dropped): {s.body!r}")
                continue
            if target not in model.ids:
                self.problems.append(f"{u.source} is folded into unknown rule {target}")
                continue
            self.folded.setdefault(target, []).append((s, u))
        for target in self.folded:
            self.folded[target].sort(key=lambda p: p[0].line)

    def body(self, lines, here):
        out = []
        for line in lines:
            line, unresolved = self.m.rewrite_links(line, here)
            for t in unresolved:
                self.problems.append(f"link to {t} has no manual ID")
            out.append(line)
        return out

    def rule(self, r, here):
        level = heading_level(r.id)
        out = [f'<a id="{anchor(r.id)}"></a>', f"{'#' * level} {r.id} {r.title}", ""]
        if r.id == GLOSSARY:
            out += [self.glossary_index(), ""]
        s = self.m.row_section.get(r.id)
        if r.id == "B1.0":
            out += B1_TEXT + [""]
        elif s is not None:
            if "Heading only" in r.notes and s.body:
                self.warnings.append(f"{r.id} is marked heading only but rule book {s.key} has body text")
            if "Heading only" not in r.notes and not s.body and r.id != "D7.0":
                self.warnings.append(f"{r.id} has no body text in rule book {s.key}")
            body = self.body(s.body, here)
            if re.fullmatch(r"B3\.\d+", r.id):
                body = self.anchor_steps(r.id, body)
            if body:
                out += body + [""]
        elif r.source or "New group heading" not in r.notes:
            self.problems.append(f"{r.id} has no rule book text")
        for sub in self.subheadings.get(r.id, []):
            out += [f"{'#' * (level + 1)} {title_case(sub.text)}", ""]
            body = self.body(sub.body, here)
            if body:
                out += body + [""]
        for s, u in self.folded.get(r.id, []):
            out += [f"**{u.title}**", ""]
            body = self.body(s.body, here)
            if body:
                out += body + [""]
        return out

    def glossary_index(self):
        """Generated line of links to the glossary's letter headings."""
        letters = [sub.text for sub in self.subheadings.get(GLOSSARY, [])]
        return " · ".join(f"[{x}](#{slugify(x)})" for x in letters)

    def generated_lines(self):
        """Lines the build writes that are not rule book text."""
        return set(VARIANTS_NOTE) | set(B1_TEXT) | {self.glossary_index()}

    def anchor_steps(self, rid, body):
        out = []
        for line in body:
            m = STEP_RE.match(line)
            if m:
                line = f'{m.group(0)}<a id="{anchor(rid + "." + m.group(1))}"></a>{line[m.end():]}'
            out.append(line)
        return out

    def unnumbered(self, title, here):
        for s in self.m.sections:
            if s.title.lower() == title.lower():
                return [f"# {title}", ""] + self.body(s.body, here) + [""]
        self.problems.append(f"no rule book section titled {title!r}")
        return []

    def toc(self):
        out = ["# Table of Contents", "", "- [Foreword](#foreword)",
               "- [History of the Empyrean Cluster](#history-of-the-empyrean-cluster)"]
        for letter, title in self.m.subjects:
            heading = f"{letter}. {title}"
            if letter == "V":
                out.append(f"- [{heading}](variants.md)")
            else:
                out.append(f"- [{heading}](#{slugify(heading)})")
            for r in self.m.rows:
                if r.subject == letter and heading_level(r.id) == 2:
                    out.append(f"  - [{r.id} {r.title}]({self.link(r.id, 'manual.md')})")
        out += ["- [Concordance](#concordance)", ""]
        return out

    def link(self, rid, here):
        doc = doc_for(rid)
        return f"{'' if doc == here else doc}#{anchor(rid)}"

    def concordance(self):
        m = self.m
        out = [
            "# Concordance", "",
            "Each rule book heading, linked to the rule book and to the manual rule that holds its text.",
            "Headings with no manual ID give the reason.", "",
            "| Rule book | Title | Manual | Notes |",
            "|-----------|-------|--------|-------|",
        ]
        rows_by_line = {}
        for r in m.rows:
            s = m.row_section.get(r.id)
            if s:
                rows_by_line.setdefault(s.line, []).append(r)
        unmapped_by_line = {}
        for u in m.unmapped:
            s = m.unmapped_section.get(id(u))
            if s:
                unmapped_by_line[s.line] = u
        for s in m.sections:
            ref = s.key if s.numbered else title_case(s.title)
            cell = f"[{ref}](rulebook.md#{s.slug})"
            if s.line in rows_by_line:
                rs = rows_by_line[s.line]
                manual = ", ".join(f"[{r.id}]({self.link(r.id, 'manual.md')})" for r in rs)
                out.append(f"| {cell} | {rs[0].title} | {manual} | |")
            elif s.line in unmapped_by_line:
                u = unmapped_by_line[s.line]
                reason = re.sub(
                    r"\b([A-Z]\d+(?:\.\d+)+)\b",
                    lambda x: f"[{x.group(1)}]({self.link(x.group(1), 'manual.md')})" if x.group(1) in m.ids else x.group(1),
                    u.reason)
                out.append(f"| {cell} | {u.title} | | {reason} |")
        out.append("")
        return out

    def build(self):
        m = self.m
        manual = self.unnumbered("Foreword", "manual.md")
        manual += self.toc()
        manual += self.unnumbered("History of the Empyrean Cluster", "manual.md")
        variants = [f"# V. {dict(m.subjects)['V']}", ""] + VARIANTS_NOTE + [""]
        for letter, title in m.subjects:
            if letter != "V":
                manual += [f"# {letter}. {title}", ""]
            for r in m.rows:
                if r.subject != letter:
                    continue
                if letter == "V":
                    variants += self.rule(r, "variants.md")
                else:
                    manual += self.rule(r, "manual.md")
        manual += self.concordance()
        manual, variants = self.apply_edits(manual, variants)
        return "\n".join(manual).rstrip("\n") + "\n", "\n".join(variants).rstrip("\n") + "\n"

    def apply_edits(self, manual, variants):
        """Apply the reviewed phase 4 edits in docs/connect.md."""
        edits, problems = parse_connect(read_lines(CONNECT))
        self.problems += problems
        self.edits = edits
        docs = {"manual.md": manual, "variants.md": variants}
        for e in edits:
            if e.rule not in self.m.ids:
                self.problems.append(f"{e.where}: unknown rule {e.rule}")
                continue
            lines = docs[doc_for(e.rule)]
            start = lines.index(f'<a id="{anchor(e.rule)}"></a>')
            end = start + 1
            while end < len(lines) and not lines[end].startswith(('<a id="rule-', "# ")):
                end += 1
            hits = [i for i in range(start, end) if lines[i] == e.old]
            if len(hits) != 1:
                self.problems.append(f"{e.where}: {e.rule} has {len(hits)} lines matching {e.old!r}")
                continue
            lines[hits[0]:hits[0] + 1] = e.new
        return docs["manual.md"], docs["variants.md"]


def main():
    b = Builder(Model())
    manual, variants = b.build()
    with open(MANUAL, "w", encoding="utf-8") as f:
        f.write(manual)
    with open(VARIANTS, "w", encoding="utf-8") as f:
        f.write(variants)
    print(f"wrote {MANUAL}")
    print(f"wrote {VARIANTS}")
    for w in b.warnings:
        print(f"warning: {w}")
    for p in b.problems:
        print(f"problem: {p}")
    return 1 if b.problems else 0


if __name__ == "__main__":
    sys.exit(main())
