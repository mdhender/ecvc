# Rule book reorganization scripts

Scripts for the reorganization described in [docs/REORG.md](../../docs/REORG.md).
They need Python 3.10 or later and no other packages.
Run them from the repository root.

## Build

```sh
python3 tools/reorg/build.py
```

Regenerates `docs/manual.md` and `docs/variants.md` from `docs/rulebook.md` and the tables in `docs/mapping.md`, then applies the phase 4 edits in `docs/connect.md`, overwriting both files.
Make changes to the manual through those three files, not by editing the output.
It prints warnings for things worth a look, such as rule book text with no manual ID, and problems for mapping errors.
It exits 1 if there are problems.

## Check

```sh
python3 tools/reorg/check.py
```

Runs the phase 5 checks on `docs/manual.md` and `docs/variants.md`:

- the sorted body lines match those of `docs/rulebook.md`, after rewriting the rule book's links, applying the edits in `docs/connect.md`, and skipping the bodies of sections the mapping marks "Deleted.";
- every internal and cross-file link resolves, including the links in `docs/tutorials/` and `docs/errata.md`;
- anchor IDs are unique, and every mapping row has exactly one anchor;
- heading levels follow the depth rule, and no ID has more than five numbers;
- every numbered rule book heading appears in the concordance exactly once.

It then lists the plain-text references still to rule book sections, such as "See 5.2.2." or "Chapter 9", with the manual ID each should become.
It exits 1 if any check fails.
