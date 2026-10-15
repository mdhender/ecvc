# CLAUDE.md

Code and documentation for Empyrean Challenge, a play-by-email science fiction game.
The code is Go; the documentation is in `docs/`.

## Source of truth

`docs/manual.md` is the source of truth for the rules, with the variant games in `docs/variants.md`.
Code or tests that do not match the manual are suspect: fix the code, or log the mismatch in `docs/errata.md` if the manual looks wrong.
Do not change a rule to match the code.

`docs/rulebook.md` is frozen.
It is the 1980 rule book as transcribed, kept for comparison with the manual.
Do not edit it, not even for typographic or scan errors.

## Manual IDs

Every rule in the manual has an ID, such as `D3.2.1`, and an anchor on its own line before its heading, such as `<a id="rule-D3.2.1"></a>`.
Tests cite the IDs of the rules they validate.

- Until coding starts, IDs may change while the manual is reorganized.
  When one changes, update everything that cites it: links in the manual and variants, `docs/concordance.md`, `docs/errata.md`, `docs/tutorials/`, and `docs/explanation/`.
- Once coding starts, IDs are frozen: an ID is never changed or reused.
  A new rule gets a new ID, and a deleted rule's ID stays reserved.
- IDs are strings that sort part by part, so `D3.2.10` follows `D3.2.9`.
- `X.0` holds the general provisions for its parent.
- Examples, charts, and tables belong to the rule they illustrate and have no ID of their own, so tests cite the rule, not the example.
- `docs/concordance.md` maps each rule book section number to its manual ID.

`docs/REORG.md` records the decisions behind the IDs, subjects, and heading depth.

## Editing the manual

- Edit `docs/manual.md` and `docs/variants.md` directly.
- Keep one sentence per line.
  A leading `\*` or `\*\*` is a footnote marker.
- Each subject is a level 1 heading, such as `# D. Combat`.
  A top-level rule such as `D3.0` is level 2, and every other rule's heading level is one more than the count of numbers in its ID.
- Manual titles are in title case; codes such as TL and S/C stay upper case.
- Links between rules use the anchors, such as `[D3.2.1](#rule-D3.2.1)`, or `manual.md#rule-D3.2.1` from another file.
- Keep `docs/concordance.md` and the tables of contents in step with any rule that moves.
- Rule changes go through `docs/errata.md` and the Deferred list in `docs/REORG.md`.
  Errata entries are numbered permanently; a resolved or mistaken entry is marked, not removed.
- `docs/tutorials/` and `docs/explanation/` explain the rules without adding to them; tests never cite them.
  Tutorials teach by doing, and explanations discuss why the rules work as they do.

## Tools

`tools/reorg/` holds the scripts that built the manual from the rule book.

- Do not run `tools/reorg/build.py`: it regenerates `docs/manual.md` and `docs/variants.md` from the rule book and would overwrite edits made to the manual.
- `tools/reorg/check.py` still checks links, anchors, heading levels, and `docs/concordance.md`.
  Its check that the manual's body lines match the rule book fails once the manual is edited directly, so it is skipped unless `--rulebook` is given.
- `tools/` is removed once the documentation is done, before coding starts.

## Git

- Documentation work is committed directly to `main` for now.
- Commit and push only when asked.

## License

The code is AGPL-3.0-or-later.
The documentation in `docs/` is CC BY-NC-ND 4.0: Empyrean Challenge is owned by James Colombo, who has given permission to use and update its rules here, but that permission can not be passed on.
