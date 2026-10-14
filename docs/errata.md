# Errata

This is the log of mistakes found in the rules of [manual.md](manual.md) and [variants.md](variants.md), as described in [REORG.md](REORG.md).
Entries record problems; they do not fix them.
Rule changes start from the `manual-baseline` tag and work through this list.

## How to read it

- Entries are numbered in the order they were logged, and a number is never reused.
  Cite an entry as "errata 12".
- **Rules** links every rule involved.
- **Kind** is one of:
  - *contradiction*: two rules, or a rule and its example, disagree;
  - *example*: an example or table does not match the rule it illustrates;
  - *ambiguity*: the rule can be read more than one way;
  - *gap*: the rules do not say what happens;
  - *structure*: a rule is out of place, or out of step with its counterparts;
  - *withdrawn*: the entry turned out not to be a rule mistake, and its number stays reserved.
- **Resolved**, when present, names the issue that fixed the rule and says how.
  A resolved entry has ✅ at the end of its title; an entry resolved only in part does not.
- **Won't fix**, when present, says why the rule is left as it is.
- A withdrawn entry, or one marked won't fix, has 🚫 at the end of its title.
- Entries are grouped by the subject of their first rule.

Typographic and scan errors are not logged here; they are corrected in `docs/rulebook.md` and the manual is rebuilt.

## A. General Rules and Definitions

### 1. Coordinate range does not match the cluster size ✅

- **Rules:** [A2.1](manual.md#rule-A2.1)
- **Kind:** contradiction

The cluster is 30 light years per side, but each coordinate ranges from 0 to 30, which is 31 values.

- **Resolved:** #3. The cluster is a sphere of radius 26 light years, with whole-number coordinates ([A2.1](manual.md#rule-A2.1)).

### 2. Number of orbits per star ✅

- **Rules:** [A2.2](manual.md#rule-A2.2), [A3.0](manual.md#rule-A3.0)
- **Kind:** contradiction

A2.2 says each star of a multiple star system has 10 orbits.
A3.0 says a star has 11 orbits, numbered 0 to 10.

- **Resolved:** #2. A solar system has orbits 1 to 10; orbit 0 belongs to the star system ([A3.1](manual.md#rule-A3.1)).

### 3. Scale of the habitability number ✅

- **Rules:** [A4.2](manual.md#rule-A4.2), [G3.9](manual.md#rule-G3.9), [H1.7](manual.md#rule-H1.7), [V1.0](variants.md#rule-V1.0)
- **Kind:** ambiguity

A4.2 says the habitability number, 0 to 25, "indicates the number of population units who can live on a planet's surface".
G3.9 scales it by 10,000,000 POP, H1.7 limits FRM-1 to the number times 100,000, and V1.0 counts 200,000 POP per habitability point.
A4.2 gives no scale.

- **Resolved:** #19. A4.2 defines the planet's HN limit as the habitability number (HN) times 10,000,000 POP, and lists its effects on births (G2.1), the death rate (G3.9), and FRM-1 (H1.7); G2.1 and G3.9 cite A4.2 for the limit.
  H1.7's 100,000 FRM-1 per HN feed G3.9's 10,000,000 POP per HN; V1.0's 200,000 POP per HN is a scoring threshold, not a capacity.

### 4. Contents of a resource deposit ✅

- **Rules:** [A4.3](manual.md#rule-A4.3)
- **Kind:** ambiguity

"Each deposit contains 1,000,000-99,000,000 units of: gold, fuel, metallics and non-metallics" can be read as one resource per deposit or all four.
M1.0 reports "the resource each deposit contains", which suggests one.

- **Resolved:** #22. A deposit contains 1,000,000 to 99,000,000 units of a single resource, with a yield of 1% to 9% for gold and 10% to 90% for the others ([A4.3](manual.md#rule-A4.3)).
  MIN's extract ORE, which is refined at the deposit's yield and rounded down, up to the quantity left in the deposit ([H2.1](manual.md#rule-H2.1)).

### 5. Race numbers for Regents and Independents ✅

- **Rules:** [A6.0](manual.md#rule-A6.0), [B4.1](manual.md#rule-B4.1), [B4.2](manual.md#rule-B4.2)
- **Kind:** gap

A6.0 maps player numbers 1 to 150 to races.
The Moderator assigns Regents a player number (B4.1), and Independents take the race of their population (B4.2), but neither number is covered by the table.

- **Resolved:** #24. Race is recorded separately from the player number; only the Rulers with home worlds, players 1 to 150, take their race from the A6.0 table ([A6.0](manual.md#rule-A6.0)).
  Regents and Independents get the next available player number.
  A Regent takes his Ruler's race ([B4.1](manual.md#rule-B4.1)); an Independent takes the race of his s/c's majority population ([B4.2](manual.md#rule-B4.2)).

### 6. Sample turnsheet race number 🚫

- **Rules:** [A6.0](manual.md#rule-A6.0), [S3.0](manual.md#rule-S3.0)
- **Kind:** withdrawn

The sample turnsheet shows RACE #2 with PLAYER ID #22, but A6.0 put players 16 to 30 in race 1.
The A6.0 table was a transcription error; corrected, it numbers races from 1, so players 16 to 30 are in race 2 and the sample agrees.

### 7. Standard of living: divided or multiplied by 4

- **Rules:** [A7.0](manual.md#rule-A7.0), [R1.0](manual.md#rule-R1.0), [V1.0](variants.md#rule-V1.0)
- **Kind:** contradiction

The glossary defines SOL as total CNGD paid ÷ total POP, then ÷ 4.
R1.0 says the total is multiplied by 4, "which makes the rate annual".
The Maxi-Challenge colony points in V1.0 depend on which is right.

- **Resolved:** #26, in part. Neither formula is right: SOL is calculated quarterly, and total CNGD paid is only part of the calculation.
  R1.0 now reports the SOL as the rules calculate it, with no formula of its own ([R1.0](manual.md#rule-R1.0)).
  The glossary formula stays until the rules define SOL (errata 76).

### 8. Abbreviations: should or must ✅

- **Rules:** [A7.0](manual.md#rule-A7.0), [S2.0](manual.md#rule-S2.0)
- **Kind:** contradiction

The glossary says words in it "should be abbreviated" in orders; S2.0 says they "must be abbreviated".

- **Resolved:** #28. Glossary terms must be abbreviated in orders; the glossary now says so and cites S2.0 ([A7.0](manual.md#rule-A7.0)).
  S2.0 now says an order that writes one out in full, such as "missiles-6", is rejected with error E01 ([S2.0](manual.md#rule-S2.0)).

### 9. Life support in orbiting colonies ✅

- **Rules:** [A7.0](manual.md#rule-A7.0), [G6.1](manual.md#rule-G6.1)
- **Kind:** contradiction

The glossary says LFS serve "ships and ESC's".
G6.1 says only OPC's do not require LFS, so OBC's need them too.

- **Resolved:** #30. Every s/c except OPC's requires LFS; the glossary now says so and cites G6.1 ([A7.0](manual.md#rule-A7.0)).

### 76. Standard of living is not defined in the rules

- **Rules:** [A7.0](manual.md#rule-A7.0), [G2.1](manual.md#rule-G2.1), [G3.7](manual.md#rule-G3.7), [G5.1](manual.md#rule-G5.1), [N1.2](manual.md#rule-N1.2), [R1.0](manual.md#rule-R1.0), [V1.0](variants.md#rule-V1.0)
- **Kind:** gap

Births (G2.1), rebels (G3.7, N1.2), and Maxi-Challenge colony points (V1.0) depend on the standard of living (SOL), but no rule defines it.
Only the glossary gives a formula, and it is not the whole calculation.
The rules should define SOL, calculated quarterly, with total CNGD paid (G5.1) as one part, and the glossary should cite that rule.

### 77. Rebel-free population codes are not in the glossary

- **Rules:** [A7.0](manual.md#rule-A7.0), [K3.2](manual.md#rule-K3.2), [S2.0](manual.md#rule-S2.0)
- **Kind:** gap

K3.2 has a TFR leave rebels behind by changing the last letter of the population code to X, as in PRX-3 for PRO-3.
The glossary does not list these codes (PRX, SLX, CNX, and the rest), although S2.0 requires the words in orders to be abbreviated as the glossary shows them.

## B. How to Play

### 10. Second TL check ✅

- **Rules:** [B3.17.6](manual.md#rule-B3.17.6), [J4.1](manual.md#rule-J4.1)
- **Kind:** gap

The production stage has "TL increases (1st check)", but no stage has a second check.

- **Resolved:** #32. RSCH is applied to TL once per turn, never twice, during the production stage ([J4.1](manual.md#rule-J4.1)).
  B3.17.6 is now "TL increases", without "(1st check)" ([B3.17.6](manual.md#rule-B3.17.6)).

### 11. End of the game on a racial victory ✅

- **Rules:** [B5.1](manual.md#rule-B5.1), [B5.2](manual.md#rule-B5.2)
- **Kind:** gap

B5.1 says the game is over on an individual victory; B5.2 says a racial victory "is declared" but not whether the game ends.
Nothing says which applies when both are met on the same turn.

- **Resolved:** #38. A racial victory ends the game ([B5.2](manual.md#rule-B5.2)).
  The Moderator selects one victory condition, individual or racial, when the game is set up; a game never uses both ([B5.0](manual.md#rule-B5.0)).
  The variants say that their victory conditions replace those of the standard game ([V1.0](variants.md#rule-V1.0), [V2.0](variants.md#rule-V2.0)).

## C. Movement and Navigation

### 12. Over-jump chances exceed 100% ✅

- **Rules:** [C3.1.1](manual.md#rule-C3.1.1)
- **Kind:** contradiction

The outcomes are exclusive (melt, blow up, or arrive intact), but from a ratio of 5 the chances add to more than 100%: 40% + 65% at 5, up to 90% + 100% at 10.
The chart also stops at a ratio of 10.

- **Resolved:** #40. The computer rolls in turn: first for blowing up, then, if the ship survives, for melting ([C3.1.1](manual.md#rule-C3.1.1)).
  The ratio is the light years divided by the lowest HDRV TL on the ship ([C1.0](manual.md#rule-C1.0)), rounded up; the chart rows are 1 to 10, and a JMP with a ratio above 10 fails with E20.

### 13. Distance of a move within a star system ✅

- **Rules:** [C3.2](manual.md#rule-C3.2), [C3.3](manual.md#rule-C3.3)
- **Kind:** contradiction

C3.2 says interplanetary moves are always counted as 0.1 light years.
C3.3 counts a move between the stars of a multiple star system as 0.2.

- **Resolved:** #6. A move within a solar system, including to or from orbit 0, is .1 light years; a move between solar systems passes through orbit 0 and is .2 light years ([C3.3](manual.md#rule-C3.3)).
  C3.2 now cites C3.3.

### 67. Arrival in orbit 0

- **Rules:** [C3.2](manual.md#rule-C3.2), [A3.1](manual.md#rule-A3.1)
- **Kind:** gap

C3.2 says a ship moving to another orbit arrives 5 to 10 distance units from the planet and is told who controls it.
Orbit 0 has no planet, and the rules do not say where a ship arrives there or what it is told.

### 68. Seeing ships in orbit 0

- **Rules:** [A3.1](manual.md#rule-A3.1), [M2.1](manual.md#rule-M2.1), [M2.2](manual.md#rule-M2.2), [M2.3](manual.md#rule-M2.3), [S10.1](manual.md#rule-S10.1)
- **Kind:** gap

Ships from other star systems always arrive in orbit 0 (A3.1).
A ship in orbit 0 gets a probe report of orbit 0 every turn (M2.1), but nothing else in the star system can learn what is there.
Orbit 0 can not be the target of an orbit probe (M2.1), a s/c probe needs both s/c's in the same orbit (M2.2), and a system probe reports planets and stars, not s/c's (M2.3).
The rules do not say whether colonies and ships in orbits 1 to 10 should see ships in orbit 0, so ten ships could gather there unseen by everyone else in the star system.
The list format of [S2.5](manual.md#rule-S2.5) makes `77, PRB, 3, [0].` a well-formed order, but no rule says what it does: M2.1 forbids orbit 0 as a target, and orbit 0 belongs to the star system, not to star 3 (A3.1).

### 71. Placement of arriving and new ships ✅

- **Rules:** [C3.2](manual.md#rule-C3.2), [F4.1](manual.md#rule-F4.1)
- **Kind:** ambiguity

Arriving ships are placed "between 5 and 10 distance units from the planet" and new ships "between 2 and 3", without saying how the distance is measured or how the ship's tactical coordinates are chosen.

- **Resolved:** #8. Each tactical coordinate of an arriving ship is chosen at random from -10 to -5 and 5 to 10, and of a newly set up ship from -3, -2, 2, and 3 ([D6.3.4](manual.md#rule-D6.3.4)).

## D. Combat

### 14. Effect of choosing a target

- **Rules:** [D6.2](manual.md#rule-D6.2)
- **Kind:** ambiguity

"Specifying a target will increase the chance of hitting the target area by 50%" does not say whether the 50% is added or multiplied, or what the base chance is.

### 15. Colony positions in bombardment

- **Rules:** [D6.3.1](manual.md#rule-D6.3.1)
- **Kind:** contradiction

The table puts colonies 1 to 3 distance units apart, but the same rule says all colonies are at position 0/0/0.
The table uses "ORB", which is not defined (the glossary uses OBC), and lists ORB to ESC and OPC but not the reverse.

### 16. Commitment percentage names MSS

- **Rules:** [D6.3.2](manual.md#rule-D6.3.2)
- **Kind:** ambiguity

The rule speaks of "multiple-TL EWP's and MSS's", then applies the percentage to "each MSL and EWP".

### 17. What defends against energy beams

- **Rules:** [D9.1](manual.md#rule-D9.1), [E4.0](manual.md#rule-E4.0), [E5.2](manual.md#rule-E5.2), [E6.0](manual.md#rule-E6.0)
- **Kind:** contradiction

D9.1 says EWP's and ANM's "defend against the energy beams and MSS's".
In subject E, ANM's and EWP's defend against MSS's, and only ESH's defend against beams.

### 18. Surrender ratio

- **Rules:** [D9.6](manual.md#rule-D9.6), [D10.0](manual.md#rule-D10.0)
- **Kind:** ambiguity, gap

D9.6 triggers surrender when the ratio "is 6 to 1", not at least 6 to 1.
D10.0 transfers the s/c when the defending troops are eliminated, but does not say what happens when the defenders surrender.

### 19. After the battle

- **Rules:** [D10.0](manual.md#rule-D10.0)
- **Kind:** ambiguity

"The victor WTD's troops on the turn following the victory" does not say whether this is automatic or needs a WTD order.
"Unfinished battles will continue on the following turn" does not say whether the INV and support orders must be written again.

## E. Weapons and Defenses

### 20. Hit fractions above 1

- **Rules:** [E4.2](manual.md#rule-E4.2), [E5.2](manual.md#rule-E5.2)
- **Kind:** gap

HP is "the fraction of ANM that hit", (2^AT ÷ 2^MT) x .55, which is above 1 when the ANM's TL is higher than the MSS's.
The EWP formula, x 0.3, is above 1 when the EWP's TL is two or more higher.
Neither rule caps the result.

### 21. Energy of an EWP

- **Rules:** [E5.1](manual.md#rule-E5.1), [R3.0](manual.md#rule-R3.0)
- **Kind:** contradiction

E5.1 gives each EWP 10 x TL energy units; R3.0 gives 10 x TL^2.
The example in E6.0 uses TL-1, where both give 10.

### 70. Energy weapon damage divisor not bounded

- **Rules:** [E5.1](manual.md#rule-E5.1), [E3.1](manual.md#rule-E3.1)
- **Kind:** gap

The damage formula divides by "D + SP/10 - S", which is 0 or negative when the attacker's sensor TL is at least the distance plus a tenth of the target's speed, such as when two ships share tactical coordinates.
E3.1 uses 1 in place of the same expression when it is less than 1; E5.1 does not say what to use.

## F. Ships and Colonies

### 22. Volume of structural units

- **Rules:** [F3.1](manual.md#rule-F3.1), [R3.0](manual.md#rule-R3.0)
- **Kind:** ambiguity

Structural units must enclose the volume of the s/c's units, and R3.0 gives STUN, LTSU, and SLSU a volume.
The rules do not say whether the structural units must enclose themselves.
R3.0's footnote, that assembled STUN, LTSU, and SLSU are "all -1", may be meant to answer this, but its meaning is unclear.

### 23. Spare transports in a set-up

- **Rules:** [F4.7](manual.md#rule-F4.7)
- **Kind:** contradiction

TPT's listed in a STP but not needed "are used by the establishing s/c for other work", yet "All the TPT in the STP return to the new s/c".

### 24. Restrictions "listed below" for add-ons

- **Rules:** [F5.2](manual.md#rule-F5.2), [F5.2.1](manual.md#rule-F5.2.1), [F5.7](manual.md#rule-F5.7), [F5.8](manual.md#rule-F5.8)
- **Kind:** ambiguity

F5.2 says an ADN is allowed "so long as the restrictions listed below are met", but the rule below it, F5.2.1, lists reasons an ADN fails; the restrictions are in F5.7 and F5.8.

### 25. Losses when junking

- **Rules:** [F6.0](manual.md#rule-F6.0), [F10.3](manual.md#rule-F10.3), [F10.5](manual.md#rule-F10.5)
- **Kind:** gap

A JNK dis-assembles all the assembled items of a s/c, but the rules do not say whether the 10% dis-assembly loss applies, or how many CNW and TPT it needs.

### 26. Factory groups allowed in a merge

- **Rules:** [F8.0](manual.md#rule-F8.0), [S5.8](manual.md#rule-S5.8)
- **Kind:** contradiction

F8.0 says the two s/c's factory groups "must not exceed 25"; S5.8 says they "must total less than 25".

## G. Population

### 27. Who counts as unemployable

- **Rules:** [G1.1](manual.md#rule-G1.1), [G1.5](manual.md#rule-G1.5), [G1.6](manual.md#rule-G1.6), [G1.8](manual.md#rule-G1.8)
- **Kind:** contradiction

G1.1 defines UEM as "the entire population that is not USK, PRO, or SLD", which would include SPYS, CNW, and TRN.

### 28. Rebels among soldiers

- **Rules:** [G1.7](manual.md#rule-G1.7), [N1.0](manual.md#rule-N1.0)
- **Kind:** contradiction

Both rules say rebels are found in every group "except spies and soldiers", then define rebel soldiers as the soldiers willing to rebel.

### 29. Trainees without enough professionals

- **Rules:** [G1.8](manual.md#rule-G1.8)
- **Kind:** gap

Each 100 TRN need one PRO to train them, but the rules do not say what happens when there are too few PRO.

### 30. When soldiers retire

- **Rules:** [G1.4](manual.md#rule-G1.4), [G2.3](manual.md#rule-G2.3)
- **Kind:** gap

5% of soldiers retire "on every fourth turn", but the rules do not say which turns.

### 31. Source of new unemployables in combat

- **Rules:** [G2.1](manual.md#rule-G2.1)
- **Kind:** contradiction

G2.1 says UEM increase from "SLD's captured in combat", then that 30% of all combat casualties become UEM as wounded.

### 32. Normal death rate

- **Rules:** [G3.9](manual.md#rule-G3.9), [G6.2](manual.md#rule-G6.2)
- **Kind:** contradiction

G3.9 gives the death rate as 0.625% per turn; G6.2 calls the normal rate 0.0625%.

### 33. Unstated formulas

- **Rules:** [G2.1](manual.md#rule-G2.1), [G3.9](manual.md#rule-G3.9), [H3.6](manual.md#rule-H3.6), [N1.1.1](manual.md#rule-N1.1.1), [L3.0](manual.md#rule-L3.0)
- **Kind:** gap

Several rules give a range or a direction but not the calculation:
the birth rate between 0.25% and 2.5% (G2.1);
how much the OPC death rate rises above the habitability limit (G3.9);
how many turns retooling takes (H3.6);
the rebel increases, which N1.0 calls approximations;
and market prices, which L3.0 says are "known only to the computer".

## H. Production and Industry

### 34. Orbit 11 ✅

- **Rules:** [H1.3.2](manual.md#rule-H1.3.2), [A3.0](manual.md#rule-A3.0)
- **Kind:** contradiction

Hydroponic farms may not be assembled "in colonies in orbits 6 - 11", but orbits only go to 10.

- **Resolved:** #2. H1.3.2 now says "orbits 6 - 10".

### 35. Shutting down part of the farms

- **Rules:** [H1.6](manual.md#rule-H1.6), [S8.5](manual.md#rule-S8.5), [A7.0](manual.md#rule-A7.0)
- **Kind:** contradiction

H1.6 and the glossary say SHT shuts down all the farms in a s/c, and that a portion can not be shut down.
S8.5's example shuts down only the FRM-2.

### 36. Factory shortages

- **Rules:** [H3.9](manual.md#rule-H3.9)
- **Kind:** contradiction

H3.9 says factory groups move "as many items through its WIP as there are resources, labor, and fuel", then that processing stops entirely at the first shortage, and is "not done" at all while the shortage lasts.

### 37. Limits on mine and factory groups

- **Rules:** [H2.4](manual.md#rule-H2.4), [H3.0](manual.md#rule-H3.0), [R2.0](manual.md#rule-R2.0)
- **Kind:** contradiction

H2.4 allows 40 mine groups per colony and H3.0 allows 25 factory groups per colony.
Error codes E08 and E12 say the *player* already has 40 MIN groups or 25 FCT groups.

### 38. Retooling exceptions

- **Rules:** [H3.5](manual.md#rule-H3.5), [H3.6](manual.md#rule-H3.6), [S8.1](manual.md#rule-S8.1), [S8.2](manual.md#rule-S8.2)
- **Kind:** contradiction

S8.1 names RSCH as the only change that needs no RETL; H3.6 also exempts switching between STUN, LTSU, and SLSU.
S8.2 requires combined groups to have the same type of work in process; H3.5 requires only the same item.

## J. Technology and Research

### 39. Trading TL

- **Rules:** [J1.0](manual.md#rule-J1.0), [J2.0](manual.md#rule-J2.0), [J4.0](manual.md#rule-J4.0), [L2.0](manual.md#rule-L2.0), [L4.0](manual.md#rule-L4.0), [S2.3](manual.md#rule-S2.3)
- **Kind:** contradiction

J1.0, J2.0, and S2.3 treat a TL as something a s/c can sell or transfer, with examples `29, SEL, , TL-5, 50.5.` and `29, TFR , TL-7, 28.`
J4.0 says there are three ways to raise a TL, all through RSCH, and L2.0 says TL's can not be sold.
The SEL example also gives a price, which L4.0 says SEL orders never have.

### 40. Units without a TL

- **Rules:** [J3.0](manual.md#rule-J3.0), [S2.4](manual.md#rule-S2.4)
- **Kind:** gap

J3.0's list of units without a TL does not include RSCH.

### 41. Which TL research raises ✅

- **Rules:** [J4.0](manual.md#rule-J4.0), [J4.1](manual.md#rule-J4.1), [J4.2](manual.md#rule-J4.2)
- **Kind:** ambiguity

J4.0 says research raises a s/c's TL, and RSCH can be transferred to ships, but J4.1 says the computer raises "the TL of the colony".

- **Resolved:** #34. Any s/c raises its TL by assembling RSCH with an ASM order naming the TL ([J4.1](manual.md#rule-J4.1), [S6.1](manual.md#rule-S6.1)).

### 79. RSCH applied before it can be transferred ✅

- **Rules:** [B3.17.6](manual.md#rule-B3.17.6), [J4.1](manual.md#rule-J4.1), [J4.2](manual.md#rule-J4.2), [K5.0](manual.md#rule-K5.0)
- **Kind:** contradiction

J4.1 has the computer raise the TL automatically once enough RSCH has been built, using up the RSCH.
J4.2 and K5.0 let a s/c transfer RSCH to another s/c, such as one of the player's ships.
If RSCH were applied automatically, a colony could never build up RSCH to transfer to her ships.
See also errata 41.

- **Resolved:** #34. RSCH is no longer applied automatically: it accumulates until the player assembles it with an ASM order naming the target TL, such as 75, ASM, TL-3 ([J4.1](manual.md#rule-J4.1), [S6.1](manual.md#rule-S6.1)).
  The TL is raised at B3.17.6, one level at a time toward the TL named, as far as the RSCH pay for; the rest stay accumulated, and several TL's may be gained in one turn.
  A second ASM order for TL in the same turn fails with E01.

### 80. ASM order for a TL that can not be reached ✅

- **Rules:** [J4.1](manual.md#rule-J4.1), [S6.1](manual.md#rule-S6.1), [R2.0](manual.md#rule-R2.0)
- **Kind:** gap

J4.1 does not say what happens to an ASM order for TL that names the s/c's current TL or a lower one, or a TL above 10, where the RSCH table ends.
Such an order should fail with error E01.

- **Resolved:** #36. An ASM order naming the s/c's current TL, a lower TL, or a TL above 10 fails with E01 ([J4.1](manual.md#rule-J4.1)).

### 81. ASM order for TL without enough RSCH ✅

- **Rules:** [J4.1](manual.md#rule-J4.1), [S6.1](manual.md#rule-S6.1), [R2.0](manual.md#rule-R2.0)
- **Kind:** gap

J4.1 raises the TL as far as the RSCH pay for, but does not say whether an order that falls short of the TL named is an error.
The order should fail with error E02 when the RSCH do not pay for the TL named.
It is still carried out in part when the RSCH pay for at least one level: the s/c gains those levels, and the order is reported with E02.

- **Resolved:** #36. The order fails with E02 when the RSCH do not pay for the TL named, but the s/c still gains the levels they pay for ([J4.1](manual.md#rule-J4.1)).

### 82. TL in a multiple ASM order ✅

- **Rules:** [J4.1](manual.md#rule-J4.1), [S6.1](manual.md#rule-S6.1), [S6.1.1](manual.md#rule-S6.1.1)
- **Kind:** gap

S6.1.1 does not say whether a multiple ASM order may include a TL line.
TL should never be allowed in a multiple ASM order.

- **Resolved:** #36. TL is never allowed in a multiple ASM order; a TL line fails with E01, and the rest of the order is still processed ([S6.1.1](manual.md#rule-S6.1.1)).

## L. Markets and Trade

### 42. Selling population

- **Rules:** [L2.0](manual.md#rule-L2.0), [F10.4](manual.md#rule-F10.4)
- **Kind:** contradiction

L2.0 says all units, "even population units", can be sold, then that only NON and UNA can be sold; POP are neither.

## M. Exploration and Sensors

### 43. Sensors per probe

- **Rules:** [M3.0](manual.md#rule-M3.0)
- **Kind:** contradiction

M3.0 allows each SEN as many probes as its TL, and its example has 3 SEN-5 make 15 probes.
The same rule says "the ratio of SEN's to s/c's probed is one to one; the ratio of sensors to orbits probed is one to one".

## N. Espionage and Rebellion

### 44. Rebellion threshold

- **Rules:** [N1.3](manual.md#rule-N1.3)
- **Kind:** ambiguity

A rebellion takes place if rebels and rebel soldiers are "equal to 60%" of the population, not at least 60%.

### 45. Losing rebels

- **Rules:** [N1.4](manual.md#rule-N1.4)
- **Kind:** contradiction

If the rebels lose, "70% of their survivors become loyal", and "All losing SLD and rebel soldier survivors become UEM's".

### 46. Support order examples

- **Rules:** [N1.5](manual.md#rule-N1.5), [S4.10](manual.md#rule-S4.10), [S4.11](manual.md#rule-S4.11)
- **Kind:** example

The examples `95, DTS, 99.` and `95, OTS, 99, 0.` have no quantity lines and no `1, END`, which S4.10 and S4.11 require.
The text calls 95 a player; in the orders it is a s/c.

### 47. When transferred spies can be assigned

- **Rules:** [N2.1](manual.md#rule-N2.1), [N2.2](manual.md#rule-N2.2), [B3.6](manual.md#rule-B3.6), [B3.11](manual.md#rule-B3.11)
- **Kind:** ambiguity

N2.2 says spies can be assigned "on the turn following the TFR", but the transfer stage comes before the spy move stage, and N2.1 says a SPM takes effect immediately.

### 48. Regents dis-assembling spies

- **Rules:** [N2.9](manual.md#rule-N2.9)
- **Kind:** ambiguity

"A Regent can dis-assemble any group G spies in his s/c's" could include spies belonging to other Rulers.

## R. Annexes

### 49. Consumer goods composition

- **Rules:** [R3.0](manual.md#rule-R3.0)
- **Kind:** contradiction

CNGD are 0.2 METS and 0.3 NMTS, but their total mass is 0.6.
In every other row the composition adds up to the mass.

### 50. Missile launcher fuel

- **Rules:** [R3.0](manual.md#rule-R3.0), [D6.3.4](manual.md#rule-D6.3.4), [G6.1](manual.md#rule-G6.1)
- **Kind:** contradiction

R3.0 gives MSL no fuel use, but D6.3.4 says MSL's used defensively never use more fuel than needed.
R3.0's no-fuel footnote for orbiting colonies covers farms and factories but not LFS, which G6.1 also exempts.

## S. Orders

### 51. Orders written for foreign s/c's

- **Rules:** [S2.0](manual.md#rule-S2.0), [S11.1](manual.md#rule-S11.1), [R2.0](manual.md#rule-R2.0)
- **Kind:** contradiction

S2.0 says the s/c at the start of every order must belong to the player.
SPM orders are written for the s/c the spies are in, which may be foreign (S11.1, R2.0).

### 52. Sample news release is two lines long

- **Rules:** [S3.0](manual.md#rule-S3.0), [S2.0](manual.md#rule-S2.0)
- **Kind:** example

The sample turnsheet's first NSR runs onto a second line, but S2.0 limits order lines to 80 characters.

### 53. Raiding a ship with assault weapons

- **Rules:** [S4.9](manual.md#rule-S4.9), [E1.0](manual.md#rule-E1.0), [D2.2](manual.md#rule-D2.2)
- **Kind:** example

The RAD example raids ship 200 with 15,000 ASW-2, but ASW can not be used against ships.

### 54. Partial withdrawal

- **Rules:** [S4.12](manual.md#rule-S4.12), [D5.0](manual.md#rule-D5.0)
- **Kind:** contradiction

S4.12 calls WTD "an all-or-nothing order"; D5.0 lets players withdraw "all or part of their forces".

### 55. Who can be given permission to colonize

- **Rules:** [S5.1](manual.md#rule-S5.1), [F4.9](manual.md#rule-F4.9)
- **Kind:** gap

The PTC format names the "ship ID requesting permission", but colonies can also set up colonies at their location.

### 56. Set-up example notes

- **Rules:** [S5.3](manual.md#rule-S5.3)
- **Kind:** example

The notes describe 5,000 FCT-1 and 6,000 FCT-1 that are not in the example, apparently copied from the ADN example in S5.4.

### 57. Add-on examples

- **Rules:** [S5.4](manual.md#rule-S5.4)
- **Kind:** example, ambiguity

S5.4's first example calls s/c 205 a colony; its second example, which was S5.4.1 until #12, calls 205 to 210 ships.
S5.4 does not say whether each target of an ADN order receives the listed quantities or they are shared.

- **Resolved:** #12, in part. Each target receives the full quantities, supplied in the order listed when units run short ([S5.4](manual.md#rule-S5.4)).
  The example naming s/c 205 as both a colony and a ship is still open.

### 58. Multiple DAS item count

- **Rules:** [S6.2.1](manual.md#rule-S6.2.1)
- **Kind:** example

The example `75, DAS, 4, M.` is followed by five item lines.

### 59. Multiple APU quantity

- **Rules:** [S7.4.2](manual.md#rule-S7.4.2)
- **Kind:** example

The example allows 300,500 SLSU; the notes say 300,300.

### 60. SPM format without a quantity

- **Rules:** [S11.1](manual.md#rule-S11.1)
- **Kind:** example

The last SPM format has no quantity, but its examples have one.

### 61. Move example outside the cluster ✅

- **Rules:** [S14.1](manual.md#rule-S14.1), [A2.1](manual.md#rule-A2.1)
- **Kind:** example

The MOV example moves to 12,28,-32, but relative coordinates in a 30-light-year cluster can not reach -32.

- **Resolved:** #3. The MOV example now moves to 12,8,-3.

### 69. Star letters in probe orders ✅

- **Rules:** [S10.1](manual.md#rule-S10.1), [A3.1](manual.md#rule-A3.1)
- **Kind:** ambiguity

S10.1 names the star by letter and lets it be left out, in which case star A is assumed.
Once stars are numbered, the star can not be told from the orbits: `77, PRB, 3, 1, 2.` could be orbits 1 and 2 of star 3, or orbits 3, 1, and 2 of star 1.
S10.1 also uses orbit 0 to mean orbits 1 to 10 of the star, while A3.1 uses 0 for orbit 0 of the star system.

- **Resolved:** #9. The star is required and the orbits are a list ([S2.5](manual.md#rule-S2.5)); `[*]` is short for orbits 1 to 10 of the star ([S10.1](manual.md#rule-S10.1)).

### 72. Star letters in move orders ✅

- **Rules:** [S14.1](manual.md#rule-S14.1), [S14.2](manual.md#rule-S14.2), [A2.1](manual.md#rule-A2.1), [A2.2](manual.md#rule-A2.2)
- **Kind:** ambiguity

S14.1 names the star by letter, as in `995, MOV, 3, B.`, and leaves it out outside a multiple star system without saying which star is meant.
Once stars are numbered, `995, MOV, 3, 2.` is two numbers and a move to another star system is three, so only the count tells the formats apart.
S14.1 has no format for a move to orbit 0, and S14.1 and S14.2 write coordinates as `12,8,-3` rather than `(12,8,-3)` (A2.1).

- **Resolved:** #10. MOV and JMP write their destinations as designations: `(x,y,z,N,O)` for an orbit and `(x,y,z,0)` for orbit 0 of the ship's own star system, and `(x,y,z)` for another star system ([S14.1](manual.md#rule-S14.1), [S14.2](manual.md#rule-S14.2)).
  The star is always given; an orbit or orbit 0 of another star system fails with error E20, and `(x,y,z)` naming the ship's own star system is valid and moves it to orbit 0.

### 73. Jumping to the ship's own star system

- **Rules:** [S14.2](manual.md#rule-S14.2), [C3.1](manual.md#rule-C3.1), [C3.1.1](manual.md#rule-C3.1.1), [C3.2](manual.md#rule-C3.2), [C3.3](manual.md#rule-C3.3)
- **Kind:** gap

S14.2 says a JMP order naming the star system the ship is in is valid, and the ship moves to its orbit 0.
C3.1 says jumps are not made within a star system.
The rules do not say whether such an order is handled as a jump or as a move: whether it uses 40 FUEL per light year of a zero-length jump or the .1 light years of a move to orbit 0 (C3.3), whether it can over-jump (C3.1.1), and whether the ship is in hyper space for it (C3.2).

### 74. Duplicates in probe lists

- **Rules:** [S10.1](manual.md#rule-S10.1), [S2.5](manual.md#rule-S2.5), [M2.1](manual.md#rule-M2.1), [M2.2](manual.md#rule-M2.2)
- **Kind:** gap

S2.5 leaves it to each order's rule to say what an item listed more than once does.
S10.1 does not say, for either an orbit probe such as `77, PRB, 3, [4, 4].` or a s/c probe such as `77, PRB, S/C, [78, 78].`, whether the repeat is an error, is ignored, or makes a second probe and uses a second sensor.

### 75. Placement of the REC cancel rule

- **Rules:** [S7.2.2](manual.md#rule-S7.2.2), [S7.2.3](manual.md#rule-S7.2.3), [S7.4.2](manual.md#rule-S7.4.2), [S7.4.3](manual.md#rule-S7.4.3)
- **Kind:** structure

APU's cancel rule, S7.4.3, follows its multiple APU rule, S7.4.2.
REC's cancel rule, S7.2.2, comes before its multiple REC rule, S7.2.3.
REC should mirror APU, with the cancel rule after the multiple rule.

### 78. E numbers in quantities

- **Rules:** [S2.1](manual.md#rule-S2.1), [S3.0](manual.md#rule-S3.0), [S6.1](manual.md#rule-S6.1), [S6.1.1](manual.md#rule-S6.1.1), [S6.2.1](manual.md#rule-S6.2.1), [S7.2](manual.md#rule-S7.2), [S7.3.2](manual.md#rule-S7.3.2), [S12.2](manual.md#rule-S12.2)
- **Kind:** contradiction

S2.1 lets players write quantities as E numbers, such as 4E7 for 40,000,000, and the order examples in S3.0, S6.1, S6.1.1, S6.2.1, S7.2, S7.3.2, and S12.2 use them.
The new game engine does not accept E numbers.
S2.1 should drop them, and the examples should write their quantities out.

## V. Variants

### 62. Races in Maxi-Challenge

- **Rules:** [V1.0](variants.md#rule-V1.0), [A6.0](manual.md#rule-A6.0)
- **Kind:** gap

Maxi-Challenge has 20 players, each starting with a whole planet, but the rules do not say how they are grouped into races.
Item 7 applies the standard transfer and add-on rules, which depend on race.

### 63. Planet points in the standard game

- **Rules:** [V1.0](variants.md#rule-V1.0), [B5.0](manual.md#rule-B5.0)
- **Kind:** contradiction

Item 9.c.iv says bitter-end planet points "are counted the same as in EMPYREAN CHALLENGE", but the standard game has no planet points.

### 64. Cumulative points

- **Rules:** [V1.0](variants.md#rule-V1.0)
- **Kind:** gap

Head Start points "are not cumulative" (item 10.D), which implies standard Maxi-Challenge points are, but item 9 does not say so.

### 65. Starting factories

- **Rules:** [V1.1](variants.md#rule-V1.1)
- **Kind:** ambiguity

FCT group #1 has 3,750,000 FCT-1, but the assembled units table does not list it.
The sheet says "Both your home planet and your orbiting colony have TL-1"; TL belongs to s/c's, not planets.

### 66. Ten Planet War rules not given

- **Rules:** [V2.0](variants.md#rule-V2.0), [N1.4](manual.md#rule-N1.4)
- **Kind:** gap

Item 9 refers to the Ten Planet War pre-game turn sheet, which is not in the rules.
There are no Independents in the game (item 3), but N1.4 gives a s/c that rebels to an Independent in some cases.
