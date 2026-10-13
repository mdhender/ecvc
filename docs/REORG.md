# Rule book reorganization plan

This plan covers reorganizing the Empyrean Challenge rule book by subject, in the style of the Star Fleet Battles master rulebook.

## Goal

Produce `docs/manual.md`: the same rules as `docs/rulebook.md`, organized by subject, with new permanent rule IDs.

`docs/rulebook.md` stays as the baseline.
The two files sit side by side so any rule in the manual can be compared with the original text.

The reorganization moves text; it does not change rules.
Rule changes start only after the manual is baselined.

Tests will cite rules by their manual ID.

## Files

| File               | Role                                                                                                                |
|--------------------|---------------------------------------------------------------------------------------------------------------------|
| `docs/rulebook.md` | Baseline: the 1980 rule book as transcribed and edited so far. Only typographic and scan errors are corrected here. |
| `docs/manual.md`   | The reorganized rules, with new IDs.                                                                                |
| `docs/mapping.md`  | Working mapping from every rule book heading to its subject and manual ID.                                          |
| `docs/errata.md`   | Log of mistakes found in the rules, each citing a rule ID. Entries record problems; they do not fix them.           |
| `docs/REORG.md`    | This plan.                                                                                                          |

## Baselines

1. **`rulebook-baseline`**: tag `docs/rulebook.md` before the reorganization starts.
2. **`manual-baseline`**: tag `docs/manual.md` when the reorganization is complete and verified.
   Tests cite manual IDs only after this tag.
   Rule changes start from this tag, working through `docs/errata.md`.

## Manual IDs

- An ID is a subject letter followed by dot-separated numbers, such as `D3.2.1`.
- IDs are strings, not numbers.
  They sort part by part, so `D3.2.10` follows `D3.2.9`.
- `X.0` holds the general provisions for its parent, not just a heading.
  For example, `D3.2.0` holds the general provisions of `D3.2`.
- A rule may have both text and subordinate rules.
- Once `manual-baseline` is tagged, an ID is never changed or reused.
  New rules are added with new IDs, even when the hierarchy becomes awkward.
  A deleted rule's ID stays reserved.
- Gaps left by deleted rules in the rule book (12.2, 13.3.3, 15.6.6.4) are listed in the concordance as having no manual ID.

## Concordance

`docs/manual.md` ends with a concordance table mapping every rule book section number to its manual ID, linked to both documents.
Every numbered heading in the rule book appears in the concordance exactly once.
A rule book section split across several manual rules lists each of them.

The manual does not repeat rule book numbers in its headings.

## Subjects

This first-pass list of subjects is a starting point for the mapping, not a decision.

| Letter | Subject                       | Rule book chapters          |
|--------|-------------------------------|-----------------------------|
| A      | General rules and definitions | 1, 3, 4                     |
| B      | How to play                   | 16, 21, 22                  |
| C      | Movement and navigation       | 13                          |
| D      | Combat                        | 15                          |
| E      | Weapons and defenses          | 15.2, 15.6, 15.8 (parts)    |
| F      | Ships and colonies            | 7, 9                        |
| G      | Population                    | 5, 6                        |
| H      | Production and industry       | 8                           |
| J      | Technology and research       | 10                          |
| K      | Transfers and logistics       | 11                          |
| L      | Markets and trade             | 12                          |
| M      | Exploration and sensors       | 14                          |
| N      | Espionage and rebellion       | 18, 19                      |
| P      | Diplomacy and communications  | 20                          |
| R      | Reference material            | appendices, charts, reports |
| S      | Orders                        | 17                          |

Orders are their own subject because order entry is the biggest difference between EC and SFB: SFB is played live, with little plotted, while every EC turn is written orders.
Subject S may later be divided by the intent of the orders, such as combat or set-up.

The history of the Empyrean Cluster stays as unnumbered introductory material.

## Phases

### 1. Mapping

Draft `docs/mapping.md`: one row per rule book heading, giving its section number, title, subject, and proposed manual ID.
Rows note sections that split across subjects and sections that need a cross-reference.

Done when every rule book heading has a row and the subjects and IDs are agreed.

### 2. Settle open decisions

Record the answers to open questions under [Decisions](#decisions).

### 3. Move

Build `docs/manual.md` from the mapping with a script, copying rule book text unchanged.
Add manual IDs, anchors, and the concordance.
Rewrite internal links to manual anchors using the mapping.

### 4. Connect

Fix sentences that relied on the rule book's order, such as "as described above".
Each changed line is listed for review.

### 5. Verify

Because both files keep one sentence per line, the move can be checked mechanically:

- The sorted body lines of `docs/manual.md` match those of `docs/rulebook.md`, ignoring headings, anchors, and the concordance.
  Any difference must be on the reviewed list from phase 4.
- Every internal link resolves.
- No manual ID is duplicated.
- Every rule book heading appears in the concordance.

### 6. How to play

Write a short walkthrough in section B that takes a new player through a turn in the order the rule book teaches, linking to the manual rules.

### 7. Read-through

Read `docs/manual.md` in full.
Log mistakes in `docs/errata.md`; do not fix them.

Done when the read-through is complete and the checks in phase 5 pass.
Tag `manual-baseline`.

## Working rules

- Do not change rules during the reorganization.
  Log every mistake found in `docs/errata.md` instead, citing the rule ID.
- Keep the conventions of `docs/rulebook.md`: one sentence per line, and leading `\*` or `\*\*` as footnote markers.
- `docs/manual.md` is covered by the same license as the rest of `docs/`.

## Decisions

- **Orders.** Order syntax (chapter 17) is its own subject, S, separate from the rules governing what the orders do.
- **Ships and colonies.** They share subject F.
- **Anchors.** Each rule has an anchor of the form `<a id="rule-D3.2.1"></a>`, using the ID exactly as written.
- **Heading depth.** Each subject is a level 1 heading, such as `# D. Combat`.
  A top-level rule such as `D3.0` is a level 2 heading.
  Every other rule's heading level is one more than the count of numbers in its ID: `D3.1` is level 3, `D3.2.0` is level 4, and `D3.2.1.1.1` is level 6.
  A manual ID therefore has at most five numbers.
  The deepest rule book headings have five numbers, such as 17.4.27.1.1, and lose one when the chapter becomes a subject letter, so they fit with a level to spare.
- **Mapping format.** `docs/mapping.md` is a Markdown table, which the move script parses.
- **Transcription fixes.** `docs/rulebook.md` may still be corrected for typographic and scan errors, where it does not match the 1980 scans.
  Rule mistakes go to `docs/errata.md` instead.
  A correction made after `docs/manual.md` exists is applied to both files, so the check in phase 5 still holds.
