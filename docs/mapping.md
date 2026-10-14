# Rule book to manual mapping

This is the working mapping from `docs/rulebook.md` to `docs/manual.md` and `docs/variants.md`, as described in phase 1 of [REORG.md](REORG.md).
The move script reads the tables in this file.

## How to read it

Each subject has one table, sorted by manual ID, so the tables show the outline of the manual.

- **Manual ID** is the new rule ID.
- **Title** is the manual title: the rule book heading in title case, unless the notes say it was renamed.
- **Rule book** is the section number the text comes from.
  It is blank for new headings and for headings the rule book does not number.
- **Notes** flag rows for review.

"Heading only" means the rule book heading has no text of its own, so the manual rule is a heading over its subordinate rules.

## How topics were chosen

- A rule book chapter's second-level sections become topics: 13.1 HYPER DRIVES becomes C1.0, and 13.3.1 JUMPS becomes C3.1.
- A chapter with introductory text of its own (1, 18, 20) becomes a single topic, and chapter 19 follows chapter 18 into subject N.
- Subordinate rules keep their rule book order and relative numbering.
- Examples, charts, and tables are folded into the rule they illustrate, with no ID of their own.
- Gaps left by deleted and folded rules are closed up; both are listed under [No manual ID](#no-manual-id).
- Orders are grouped by intent, and related orders sit together within a group, such as ASM with DAS, and BCH with COM.
- B1.0 points to the tutorial written in phase 6, `docs/tutorials/first-turn.md`.
- Subject R holds the annexes.
- The variant games go in a separate document under subject V, so their IDs stay unique across both documents.

## A. General Rules and Definitions

| Manual ID | Title                       | Rule book | Notes                                                           |
|-----------|-----------------------------|-----------|-----------------------------------------------------------------|
| A1.0      | Introduction                | 1         |                                                                 |
| A2.0      | Coordinates                 | 3.1       | Heading only.                                                   |
| A2.1      | Computer Map                | 3.1.1     |                                                                 |
| A2.2      | Multiple Star Systems       | 3.1.2     |                                                                 |
| A2.3      | Coordinates on the Printout | 3.1.3     |                                                                 |
| A3.0      | Solar Systems               | 3.2       |                                                                 |
| A4.0      | Planets                     | 3.3       | Heading only.                                                   |
| A4.1      | Types of Planets            | 3.3.1     |                                                                 |
| A4.1.1    | Gas Giants                  | 3.3.1.1   |                                                                 |
| A4.1.2    | Terrestrial                 | 3.3.1.2   |                                                                 |
| A4.1.3    | Asteroids                   | 3.3.1.3   |                                                                 |
| A4.2      | Habitability Numbers        | 3.3.2     |                                                                 |
| A4.3      | Resource Deposits           | 3.3.3     |                                                                 |
| A5.0      | Time Scale                  | 3.4       |                                                                 |
| A6.0      | Race Numbers                | 3.6       |                                                                 |
| A7.0      | Glossary                    | 4         | Heading only. Letter subheadings (A through W) stay unnumbered. |

## B. How to Play

| Manual ID | Title                          | Rule book | Notes                                                                              |
|-----------|--------------------------------|-----------|------------------------------------------------------------------------------------|
| B1.0      | How to Play                    |           | New: points to the tutorial docs/tutorials/first-turn.md, written in phase 6.      |
| B2.0      | Initial Printout and Turnsheet | 3.5       | Moved from A: starting the game.                                                   |
| B3.0      | Turn Sequence                  | 16.1      | Takes the text of 16.1 DESCRIPTION. Stage steps are anchored as B3.n.k (REORG.md). |
| B3.1      | Combat Stage                   | 16.2.1    |                                                                                    |
| B3.2      | Pre Set-Up Stage               | 16.2.2    |                                                                                    |
| B3.3      | Set-Up Stage                   | 16.2.3    |                                                                                    |
| B3.4      | Dis-Assembly Stage             | 16.2.4    |                                                                                    |
| B3.5      | Pre-Transfer Stage             | 16.2.5    |                                                                                    |
| B3.6      | Transfer Stage                 | 16.2.6    |                                                                                    |
| B3.7      | Build Change Stage             | 16.2.7    |                                                                                    |
| B3.8      | Assembly Stage                 | 16.2.8    |                                                                                    |
| B3.9      | Market Stage                   | 16.2.9    |                                                                                    |
| B3.10     | Survey Stage                   | 16.2.10   |                                                                                    |
| B3.11     | Spy Move Stage                 | 16.2.11   |                                                                                    |
| B3.12     | Draft Stage                    | 16.2.12   |                                                                                    |
| B3.13     | Pay Change Stage               | 16.2.13   |                                                                                    |
| B3.14     | Naming Stage                   | 16.2.14   |                                                                                    |
| B3.15     | Ship Movement Stage            | 16.2.15   |                                                                                    |
| B3.16     | Restart Stage                  | 16.2.16   |                                                                                    |
| B3.17     | Production Stage               | 16.2.17   |                                                                                    |
| B3.18     | Espionage Stage                | 16.2.18   |                                                                                    |
| B3.19     | Rebellion Stage                | 16.2.19   |                                                                                    |
| B3.20     | POP Increase Stage             | 16.2.20   |                                                                                    |
| B3.21     | News Release Stage             | 16.2.21   |                                                                                    |
| B3.22     | Probe Stage                    | 16.2.22   |                                                                                    |
| B4.0      | Auxiliary Players              | 21        | Heading only. Title typo fixed (AUXILLARY).                                        |
| B4.1      | Regents                        | 21.1      | Restates the spy rule in F10.6 and N2.9.                                           |
| B4.2      | Independents                   | 21.2      |                                                                                    |
| B5.0      | Victory Conditions             | 22        | Heading only.                                                                      |
| B5.1      | Individual Victory             | 22.1      |                                                                                    |
| B5.2      | Racial Victory                 | 22.2      |                                                                                    |

## C. Movement and Navigation

| Manual ID | Title              | Rule book | Notes                            |
|-----------|--------------------|-----------|----------------------------------|
| C1.0      | Hyper Drives       | 13.1      |                                  |
| C2.0      | Space Drives       | 13.2      |                                  |
| C3.0      | Movement           | 13.3      |                                  |
| C3.1      | Jumps              | 13.3.1    |                                  |
| C3.1.1    | Over-Jumping       | 13.3.1.1  | Takes the chart from 13.3.1.1.1. |
| C3.2      | Moves              | 13.3.2    |                                  |
| C3.2.1    | Interstellar Moves | 13.3.2.1  |                                  |
| C3.3      | Fuel Use           | 13.3.4    | Renumbered; 13.3.3 is deleted.   |

## D. Combat

| Manual ID | Title                                               | Rule book  | Notes                                                                   |
|-----------|-----------------------------------------------------|------------|-------------------------------------------------------------------------|
| D1.0      | Combat Options                                      | 15.1       | Heading only.                                                           |
| D1.1      | Invade                                              | 15.1.1     |                                                                         |
| D1.2      | Raid                                                | 15.1.2     |                                                                         |
| D1.3      | Support                                             | 15.1.3     |                                                                         |
| D1.4      | Withdraw                                            | 15.1.4     |                                                                         |
| D1.5      | Bombard                                             | 15.1.5     |                                                                         |
| D1.6      | Maneuver                                            | 15.1.6     |                                                                         |
| D2.0      | Invasion                                            | 15.2       |                                                                         |
| D2.1      | Transports-Fuel                                     | 15.2.2.1   | Moved from E (15.2.2.1): invasion procedure, not a weapon rule.         |
| D2.2      | Troops                                              | 15.2.3     | Troops stay with invasion; ASW and ASC move to E.                       |
| D3.0      | Raids                                               | 15.3       |                                                                         |
| D4.0      | Support                                             | 15.4       |                                                                         |
| D5.0      | Withdrawal                                          | 15.5       |                                                                         |
| D6.0      | Bombardment                                         | 15.6       | Heading only.                                                           |
| D6.1      | Types of Bombardment Orders                         | 15.6.1     | Heading only.                                                           |
| D6.1.1    | Pre-Maneuver Energy Weapon Fire                     | 15.6.1.1   |                                                                         |
| D6.1.2    | Pre-Maneuver Missile Fire                           | 15.6.1.2   |                                                                         |
| D6.1.3    | After-Maneuver Energy Weapon Fire                   | 15.6.1.3   |                                                                         |
| D6.1.4    | After-Maneuver Missile Fire                         | 15.6.1.4   |                                                                         |
| D6.2      | Targets                                             | 15.6.2     |                                                                         |
| D6.2.1    | Types of Targets                                    | 15.6.2.1   |                                                                         |
| D6.3      | Bombardment Miscellaneous                           | 15.6.6     | Heading only.                                                           |
| D6.3.1    | Distances and Speed                                 | 15.6.6.1   |                                                                         |
| D6.3.2    | Commitment Percentage                               | 15.6.6.2   |                                                                         |
| D6.3.3    | Weighted Average                                    | 15.6.6.3   |                                                                         |
| D6.3.4    | More Miscellaneous                                  | 15.6.6.5   | Renumbered; 15.6.6.4 is deleted.                                        |
| D7.0      | Combat Orders Are Forbidden on the Turn 0 Turnsheet | 15.7       | No body text; the title is the rule. Keep its wording.                  |
| D8.0      | Military Supplies                                   | 15.8       | Heading only. REORG.md listed MTSP under E; supplies fit combat better. |
| D8.1      | What They Are and Who Receives Them                 | 15.8.1     |                                                                         |
| D8.2      | Effects of a Shortage of MTSP                       | 15.8.2     |                                                                         |
| D8.3      | Extra MTSP Provisions                               | 15.8.3     |                                                                         |
| D9.0      | Combat Execution Sequence                           | 15.9       |                                                                         |
| D9.1      | Pre-Maneuver Fire                                   | 15.9.1     |                                                                         |
| D9.2      | Ship Maneuvers                                      | 15.9.2     |                                                                         |
| D9.3      | Post-Maneuver Fire                                  | 15.9.3     |                                                                         |
| D9.4      | Troop Movement                                      | 15.9.4     |                                                                         |
| D9.5      | Defensive Weapons vs Troops                         | 15.9.5     |                                                                         |
| D9.6      | Surrender Check                                     | 15.9.6     |                                                                         |
| D9.7      | Invasion Casualties                                 | 15.9.7     |                                                                         |
| D9.7.1    | Calculating Combat Factors                          | 15.9.7.1   | Heading only.                                                           |
| D9.7.1.1  | Troops with MTSP                                    | 15.9.7.1.1 |                                                                         |
| D9.7.1.2  | Troops with No MTSP                                 | 15.9.7.1.2 |                                                                         |
| D9.7.2    | Determining Unit Losses in Combat                   | 15.9.7.2   |                                                                         |
| D9.7.3    | Determining Unit Losses in Raids                    | 15.9.7.3   |                                                                         |
| D10.0     | Mission Completion                                  | 15.10      |                                                                         |

## E. Weapons and Defenses

| Manual ID | Title                          | Rule book | Notes                                                      |
|-----------|--------------------------------|-----------|------------------------------------------------------------|
| E1.0      | Assault Weapons                | 15.2.1    |                                                            |
| E2.0      | Assault Craft                  | 15.2.2    |                                                            |
| E3.0      | Missiles and Missile Launchers | 15.6.3    |                                                            |
| E3.1      | Missile Hits                   | 15.6.3.1  |                                                            |
| E4.0      | Anti-Missiles                  | 15.6.4    | Takes the example from 15.6.4.1.                           |
| E4.1      | Used Against an Invasion       | 15.6.4.2  | Renumbered; 15.6.4.1 is folded into E4.0.                  |
| E4.2      | Anti-Missile Hits              | 15.6.4.3  |                                                            |
| E5.0      | Energy Weapons                 | 15.6.5    | Heading only. Renamed: shields moved to E6.0.              |
| E5.1      | Offense                        | 15.6.5.1  |                                                            |
| E5.2      | Defense                        | 15.6.5.2  |                                                            |
| E6.0      | Energy Shields                 | 15.6.5.3  | Moved up from 15.6.5.3. Takes the example from 15.6.5.3.1. |

## F. Ships and Colonies

| Manual ID | Title                                        | Rule book | Notes                                                                                                         |
|-----------|----------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| F1.0      | Types                                        | 7.1       |                                                                                                               |
| F2.0      | Location Restrictions                        | 7.2       | Heading only.                                                                                                 |
| F2.1      | Open Colonies                                | 7.2.1     |                                                                                                               |
| F2.2      | Enclosed Surface Colonies                    | 7.2.2     |                                                                                                               |
| F2.3      | Orbiting Colonies                            | 7.2.3     |                                                                                                               |
| F2.4      | Ships                                        | 7.2.4     |                                                                                                               |
| F3.0      | Structural Requirements                      | 7.3       | Heading only.                                                                                                 |
| F3.1      | Definition                                   | 7.3.1     |                                                                                                               |
| F3.1.1    | Structure Ratio                              | 7.3.1.1   |                                                                                                               |
| F3.2      | Enclosure Capacity Exceeded                  | 7.3.2     | Renamed for errata 90 (#66).                                                                                   |
| F4.0      | Set Ups                                      | 7.4       | Heading only.                                                                                                 |
| F4.1      | Description                                  | 7.4.1     |                                                                                                               |
| F4.2      | S/C ID Numbers                               | 7.4.2     |                                                                                                               |
| F4.3      | Set Up Restrictions                          | 7.4.3     |                                                                                                               |
| F4.3.1    | Restrictions on Type of S/C                  | 7.4.3.1   |                                                                                                               |
| F4.3.2    | Restrictions Ruler - Regent                  | 7.4.3.2   |                                                                                                               |
| F4.3.3    | Permission to Colonize                       | 7.4.3.3   |                                                                                                               |
| F4.3.4    | Failures to Set Up                           | 7.4.3.4   |                                                                                                               |
| F4.3.5    | Set-Ups for Other Players                    | 7.4.3.5   |                                                                                                               |
| F4.4      | Personnel                                    | 7.4.4     |                                                                                                               |
| F4.5      | How STP Orders Work                          | 7.4.5     |                                                                                                               |
| F4.6      | Construction Workers and Set-Ups             | 7.4.6     |                                                                                                               |
| F4.7      | Transports and Set-Ups                       | 7.4.7     |                                                                                                               |
| F4.8      | Assemblies and Set-Ups                       | 7.4.8     |                                                                                                               |
| F4.9      | Set-Up Locations                             | 7.4.9     |                                                                                                               |
| F5.0      | Add-Ons                                      | 7.5       | Heading only.                                                                                                 |
| F5.1      | Description                                  | 7.5.1     |                                                                                                               |
| F5.2      | ADN Restrictions                             | 7.5.2     |                                                                                                               |
| F5.2.1    | ADN Abortions                                | 7.5.2.1   |                                                                                                               |
| F5.3      | How ADN Orders Work                          | 7.5.3     |                                                                                                               |
| F5.4      | Construction Workers and Add-Ons             | 7.5.4     |                                                                                                               |
| F5.5      | Transports and Add-Ons                       | 7.5.5     |                                                                                                               |
| F5.6      | Assemblies and Add-Ons                       | 7.5.6     |                                                                                                               |
| F5.7      | Add-On Locations                             | 7.5.7     |                                                                                                               |
| F5.8      | Special Rules                                | 7.5.8     |                                                                                                               |
| F6.0      | Junking                                      | 7.6       |                                                                                                               |
| F7.0      | Gifts                                        | 7.7       |                                                                                                               |
| F8.0      | Merging                                      | 7.8       |                                                                                                               |
| F9.0      | Control of Planets                           | 7.9       |                                                                                                               |
| F10.0     | Assembly and Disassembly                     | 9.1       | Mixes cadres (SPYS, CNW) with item assembly. Moved as is; the cadre rules are reworked after manual-baseline. |
| F10.1     | Assembling Special Purpose Population Groups | 9.1.1     |                                                                                                               |
| F10.2     | Assembling Unassembled Items                 | 9.1.2     |                                                                                                               |
| F10.3     | Disassembling Assembled Items                | 9.1.3     |                                                                                                               |
| F10.4     | Non-Assembly Items                           | 9.1.4     |                                                                                                               |
| F10.5     | Use of Construction Workers                  | 9.1.5     |                                                                                                               |
| F10.6     | Regents                                      | 9.1.6     | Spy rule restated in N2.9 and B4.1.                                                                           |
| F10.7     | Miscellaneous                                | 9.1.7     |                                                                                                               |
| F11.0     | Scrap                                        | 9.2       |                                                                                                               |

## G. Population

| Manual ID | Title                               | Rule book | Notes                             |
|-----------|-------------------------------------|-----------|-----------------------------------|
| G1.0      | Types of Population Units           | 5.1       | Heading only.                     |
| G1.1      | Unemployables (UEM)                 | 5.1.1     |                                   |
| G1.2      | Unskilled Workers (USK)             | 5.1.2     |                                   |
| G1.3      | Professionals (PRO)                 | 5.1.3     |                                   |
| G1.4      | Soldiers (SLD)                      | 5.1.4     |                                   |
| G1.5      | Spies (SPYS)                        | 5.1.5     |                                   |
| G1.6      | Construction Workers (CNW)          | 5.1.6     |                                   |
| G1.7      | Rebels                              | 5.1.7     |                                   |
| G1.8      | Trainees (TRN)                      | 5.1.8     |                                   |
| G1.9      | Population Units (POP)              | 5.1.9     |                                   |
| G2.0      | Population Increases                | 5.2       | Heading only.                     |
| G2.1      | Unemployable Increases              | 5.2.1     |                                   |
| G2.2      | Unskilled Increases                 | 5.2.2     |                                   |
| G2.3      | Professional Increases              | 5.2.3     |                                   |
| G2.4      | Soldier Increases                   | 5.2.4     |                                   |
| G2.5      | Spy Increases                       | 5.2.5     |                                   |
| G2.6      | Construction Worker Increases       | 5.2.6     |                                   |
| G2.7      | Rebel (and Rebel Soldier) Increases | 5.2.7     | Cross-reference N1 (rebellion).   |
| G2.8      | Trainee Increases                   | 5.2.8     |                                   |
| G3.0      | Population Decreases                | 5.3       | Heading only.                     |
| G3.1      | Unemployable Decreases              | 5.3.1     |                                   |
| G3.2      | Unskilled Decreases                 | 5.3.2     |                                   |
| G3.3      | Professional Decreases              | 5.3.3     |                                   |
| G3.4      | Soldier Decreases                   | 5.3.4     |                                   |
| G3.5      | Spy Decreases                       | 5.3.5     |                                   |
| G3.6      | Construction Worker Decreases       | 5.3.6     |                                   |
| G3.7      | Rebel Decreases                     | 5.3.7     | Cross-reference N1 (rebellion).   |
| G3.8      | Trainee Decreases                   | 5.3.8     |                                   |
| G3.9      | Death Rate                          | 5.3.9     |                                   |
| G4.0      | Food                                | 6.1       | Heading only.                     |
| G4.1      | Consumption                         | 6.1.1     |                                   |
| G4.1.1    | Starvation Rule                     | 6.1.1.1   | Takes the example from 6.1.1.1.1. |
| G4.2      | Ration Percentage                   | 6.1.2     |                                   |
| G5.0      | Consumer Goods                      | 6.2       | Heading only.                     |
| G5.1      | Consumption                         | 6.2.1     |                                   |
| G5.2      | Back Pay                            | 6.2.2     |                                   |
| G6.0      | Life Support                        | 6.3       | Heading only.                     |
| G6.1      | Consumption                         | 6.3.1     |                                   |
| G6.2      | Death Rate Affected                 | 6.3.2     |                                   |

## H. Production and Industry

| Manual ID | Title                                | Rule book | Notes                              |
|-----------|--------------------------------------|-----------|------------------------------------|
| H1.0      | Farming                              | 8.1       |                                    |
| H1.1      | Amount of Food Produced              | 8.1.1     |                                    |
| H1.2      | Effect of Shortages                  | 8.1.2     |                                    |
| H1.3      | Types of Farms                       | 8.1.3     | Heading only.                      |
| H1.3.1    | FRM-1                                | 8.1.3.1   |                                    |
| H1.3.2    | FRM-2 Through FRM-5                  | 8.1.3.2   |                                    |
| H1.3.3    | FRM-6 Through FRM-10                 | 8.1.3.3   |                                    |
| H1.4      | Personnel Required                   | 8.1.4     |                                    |
| H1.5      | Fuel Use                             | 8.1.5     |                                    |
| H1.6      | Shut Downs and Start Ups             | 8.1.6     |                                    |
| H1.7      | Quantity of Farms Allowed per Planet | 8.1.7     |                                    |
| H2.0      | Mining                               | 8.2       |                                    |
| H2.1      | Amount of Resources Mined            | 8.2.1     |                                    |
| H2.2      | Effect of Shortages                  | 8.2.2     |                                    |
| H2.3      | Fuel and Personnel Required          | 8.2.3     |                                    |
| H2.4      | Quantity of Mines Allowed            | 8.2.4     |                                    |
| H2.5      | MCH, DEP, and DAS Orders             | 8.2.5     |                                    |
| H3.0      | Manufacturing                        | 8.3       |                                    |
| H3.1      | Fuel and Personnel Requirements      | 8.3.1     |                                    |
| H3.2      | Efficiency Factor - Cost             | 8.3.2     |                                    |
| H3.3      | Capacity of a Factory Group          | 8.3.3     |                                    |
| H3.4      | Work in Process                      | 8.3.4     |                                    |
| H3.5      | BCH, COM, and DAS Orders             | 8.3.5     |                                    |
| H3.6      | Retooling                            | 8.3.6     |                                    |
| H3.7      | Research and TL                      | 8.3.7     | Cross-reference J4 (improving TL). |
| H3.8      | STUN, STUL, and STUS                 | 8.3.8     | Renamed by errata 89.               |
| H3.9      | Shortages and Factory Group Numbers  | 8.3.9     |                                    |
| H3.10     | Automation                           | 8.3.10    |                                    |

## J. Technology and Research

| Manual ID | Title                    | Rule book | Notes                                |
|-----------|--------------------------|-----------|--------------------------------------|
| J1.0      | TL of Ships and Colonies | 10.1      |                                      |
| J2.0      | TL of Factories          | 10.2      |                                      |
| J3.0      | Unit TL                  | 10.3      |                                      |
| J4.0      | Improving TL             | 10.4      |                                      |
| J4.1      | Research Points          | 10.4.1    |                                      |
| J4.2      | Transferring RSCH        | 10.4.2    | Cross-reference K5 (RSCH transfers). |
| J4.3      | Buying and Selling RSCH  | 10.4.3    | Cross-reference L (market).          |

## K. Transfers and Logistics

| Manual ID | Title                        | Rule book | Notes                                                    |
|-----------|------------------------------|-----------|----------------------------------------------------------|
| K1.0      | Transfers and Pick-Ups       | 11.1      |                                                          |
| K2.0      | Transports                   | 11.2      |                                                          |
| K2.1      | Transport Capacity           | 11.2.1    |                                                          |
| K2.2      | Transferring Transports      | 11.2.2    |                                                          |
| K3.0      | Rebel Pick-Ups and Transfers | 11.3      |                                                          |
| K3.1      | X Option                     | 11.3.1    |                                                          |
| K3.2      | TFR's of Population          | 17.4.24.3 | Moved from 17.4.24.3: a transfer rule, not order syntax. |
| K4.0      | Shortages                    | 11.4      |                                                          |
| K5.0      | RSCH                         | 11.5      |                                                          |
| K6.0      | Jettisons                    | 11.6      |                                                          |

## L. Markets and Trade

| Manual ID | Title                      | Rule book | Notes                                                                     |
|-----------|----------------------------|-----------|---------------------------------------------------------------------------|
| L1.0      | Who Gets the Market Report | 12.1.1    | 12.1 FOR ALL GAMES is dropped; it only survived because 12.2 was deleted. |
| L2.0      | How the Market Works       | 12.1.2    |                                                                           |
| L3.0      | Prices                     | 12.1.3    |                                                                           |
| L3.1      | Price of Unemployables     | 12.1.3.1  |                                                                           |
| L4.0      | Bids                       | 12.1.4    |                                                                           |

## M. Exploration and Sensors

| Manual ID | Title         | Rule book | Notes                          |
|-----------|---------------|-----------|--------------------------------|
| M1.0      | Surveys       | 14.1      |                                |
| M2.0      | Probes        | 14.2      |                                |
| M2.1      | Orbit Probes  | 14.2.1    | Takes the table from 14.2.1.1. |
| M2.2      | S/C Probes    | 14.2.2    |                                |
| M2.3      | System Probes | 14.2.3    |                                |
| M3.0      | Sensors       | 14.3      |                                |

## N. Espionage and Rebellion

| Manual ID | Title                       | Rule book | Notes                                                                        |
|-----------|-----------------------------|-----------|------------------------------------------------------------------------------|
| N1.0      | Rebellion                   | 18        | Chapter 18 has intro text, so the chapter is one topic.                      |
| N1.1      | Increases                   | 18.1      | Heading only.                                                                |
| N1.1.1    | Rebel Increase Chart        | 18.1.1    |                                                                              |
| N1.1.2    | Rebel Soldier Increases     | 18.1.2    |                                                                              |
| N1.2      | Decreases                   | 18.2      |                                                                              |
| N1.3      | Rebellion                   | 18.3      |                                                                              |
| N1.4      | Aftermath                   | 18.4      |                                                                              |
| N1.5      | Support During Rebellion    | 18.5      |                                                                              |
| N2.0      | Espionage                   | 19        | Heading only. Chapter 19 is one topic, to match N1.                          |
| N2.1      | General Rules               | 19.1      |                                                                              |
| N2.2      | Group G SPYS                | 19.2      |                                                                              |
| N2.2.1    | Casualties                  | 19.2.1    |                                                                              |
| N2.3      | Group A SPYS                | 19.3      |                                                                              |
| N2.4      | Group B SPYS                | 19.4      |                                                                              |
| N2.5      | Group C SPYS                | 19.5      |                                                                              |
| N2.6      | Group D SPYS                | 19.6      |                                                                              |
| N2.6.1    | Assassination Casualties    | 19.6.1    |                                                                              |
| N2.7      | Group E SPYS                | 19.7      |                                                                              |
| N2.8      | Group F SPYS                | 19.8      |                                                                              |
| N2.8.1    | Sections of Group F Reports | 19.8.1    |                                                                              |
| N2.9      | Regents                     | 19.9      | Repeats the spy rule in F10.6 and B4.1, and adds DAS, PUP, and TFR of spies. |

## P. Diplomacy and Communications

| Manual ID | Title               | Rule book | Notes                                                   |
|-----------|---------------------|-----------|---------------------------------------------------------|
| P1.0      | Communications      | 20        | Chapter 20 has intro text, so the chapter is one topic. |
| P1.1      | News Service        | 20.1      |                                                         |
| P1.1.1    | News Releases       | 20.1.1    |                                                         |
| P1.2      | Diplomatic Messages | 20.2      |                                                         |

## R. Annexes

| Manual ID | Title                        | Rule book | Notes          |
|-----------|------------------------------|-----------|----------------|
| R1.0      | Print Out Interpretation     |           |                |
| R2.0      | Error Messages               |           | Its own annex. |
| R3.0      | Unit Characteristics Summary |           |                |

## S. Orders

| Manual ID | Title                                          | Rule book   | Notes                               |
|-----------|------------------------------------------------|-------------|-------------------------------------|
| S1.0      | How the Turn Sheet Should Look                 | 17.1        | Chapter 17 heading is dropped.      |
| S2.0      | General Rules on Writing Orders                | 17.2        |                                     |
| S2.1      | Zeros                                          | 17.2.1      |                                     |
| S2.2      | Commas                                         | 17.2.2      |                                     |
| S2.3      | TL's                                           | 17.2.3      |                                     |
| S2.4      | Race Numbers and TL Numbers                    | 17.2.4      |                                     |
| S3.0      | Sample Turnsheet                               | 17.3        |                                     |
| S4.0      | Combat Orders                                  |             | New group heading.                  |
| S4.1      | Tactical Maneuver Orders (TMV)                 | 17.4.1      |                                     |
| S4.2      | Close Orders (CLS)                             | 17.4.2      |                                     |
| S4.3      | Run Orders (RUN)                               | 17.4.3      |                                     |
| S4.4      | Pre-Maneuver Energy Weapon Fire Orders (PME)   | 17.4.4      |                                     |
| S4.5      | Pre-Maneuver Missile Fire Orders (PMM)         | 17.4.5      |                                     |
| S4.6      | After-Maneuver Energy Weapon Fire Orders (AME) | 17.4.6      |                                     |
| S4.7      | After-Maneuver Missile Fire Orders (AMM)       | 17.4.7      |                                     |
| S4.8      | Invasion Orders (INV)                          | 17.4.8      |                                     |
| S4.9      | Raid Orders (RAD)                              | 17.4.9      |                                     |
| S4.10     | Defensive Troop Support Orders (DTS)           | 17.4.10     |                                     |
| S4.11     | Offensive Troop Support Orders (OTS)           | 17.4.11     |                                     |
| S4.12     | Withdraw Orders (WTD)                          | 17.4.12     |                                     |
| S5.0      | Ship and Colony Orders                         |             | New group heading.                  |
| S5.1      | Permission to Colonize Orders (PTC)            | 17.4.13     |                                     |
| S5.2      | Allow Add-On Orders (AAN)                      | 17.4.14     |                                     |
| S5.3      | Set Up Orders (STP)                            | 17.4.15     |                                     |
| S5.4      | Add-On Orders (ADN)                            | 17.4.16     |                                     |
| S5.5      | Junk Orders (JNK)                              | 17.4.17     |                                     |
| S5.6      | Give Orders (GIV)                              | 17.4.18     |                                     |
| S5.7      | Accept Orders (ACP)                            | 17.4.19     |                                     |
| S5.8      | Merge Orders (MRG)                             | 17.4.20     |                                     |
| S5.9      | Control Orders (CON)                           | 17.4.44     |                                     |
| S5.10     | Uncontrol Orders (UNC)                         | 17.4.45     |                                     |
| S6.0      | Assembly and Scrap Orders                      |             | New group heading.                  |
| S6.1      | Assembly Orders (ASM)                          | 17.4.32     |                                     |
| S6.1.1    | Multiple ASM Orders                            | 17.4.32.1   |                                     |
| S6.2      | Disassembly Orders (DAS)                       | 17.4.50     |                                     |
| S6.2.1    | Multiple DAS Orders                            | 17.4.50.1   |                                     |
| S6.3      | Scrap Orders (SCR)                             | 17.4.23     |                                     |
| S6.3.1    | Multiple Scrap Orders                          | 17.4.23.1   |                                     |
| S7.0      | Transfer Orders                                |             | New group heading.                  |
| S7.1      | Transfer Orders (TFR)                          | 17.4.24     |                                     |
| S7.1.2    | Multiple TFR Orders                            | 17.4.24.2   |                                     |
| S7.2      | Receive Orders (REC)                           | 17.4.25     |                                     |
| S7.2.2    | To Cancel Receive Orders                       | 17.4.25.2   | Order persistence; could move to K. |
| S7.2.3    | Multiple REC Orders                            | 17.4.25.3   |                                     |
| S7.3      | Pick Up Orders (PUP)                           | 17.4.26     |                                     |
| S7.3.2    | Multiple PUP Orders                            | 17.4.26.2   |                                     |
| S7.4      | Allow Pick Up Orders (APU)                     | 17.4.27     |                                     |
| S7.4.2    | Multiple APU Orders                            | 17.4.27.2   |                                     |
| S7.4.3    | Cancelling APU Orders                          | 17.4.27.1.1 | Order persistence; could move to K. |
| S8.0      | Production Orders                              |             | New group heading.                  |
| S8.1      | Build Change Orders (BCH)                      | 17.4.28     |                                     |
| S8.2      | Combine Orders (COM)                           | 17.4.21     |                                     |
| S8.3      | Mine Change Orders (MCH)                       | 17.4.29     |                                     |
| S8.4      | Deposit Orders (DEP)                           | 17.4.22     |                                     |
| S8.5      | Shut Down Orders (SHT)                         | 17.4.30     |                                     |
| S8.6      | Start Up Orders (STU)                          | 17.4.31     |                                     |
| S9.0      | Market Orders                                  |             | New group heading.                  |
| S9.1      | Buy Orders (BUY)                               | 17.4.33     |                                     |
| S9.2      | Sell Orders (SEL)                              | 17.4.34     |                                     |
| S10.0     | Exploration Orders                             |             | New group heading.                  |
| S10.1     | Probe Orders (PRB)                             | 17.4.35     |                                     |
| S10.2     | Survey Orders (SUR)                            | 17.4.36     |                                     |
| S11.0     | Espionage Orders                               |             | New group heading.                  |
| S11.1     | Spy Move Orders (SPM)                          | 17.4.37     |                                     |
| S12.0     | Population Orders                              |             | New group heading.                  |
| S12.1     | Draft Orders (DRF)                             | 17.4.40     |                                     |
| S12.2     | Disband Orders (DSB)                           | 17.4.41     |                                     |
| S12.3     | Pay Orders (PAY)                               | 17.4.42     |                                     |
| S12.4     | Ration Orders (RTN)                            | 17.4.43     |                                     |
| S13.0     | Naming and News Orders                         |             | New group heading.                  |
| S13.1     | Name Orders (NAM)                              | 17.4.46     |                                     |
| S13.2     | Player Name Orders (NOM)                       | 17.4.47     |                                     |
| S13.3     | Planet Name Orders (NAP)                       | 17.4.48     |                                     |
| S13.4     | News Release Orders (NSR)                      | 17.4.49     |                                     |
| S14.0     | Movement Orders                                |             | New group heading.                  |
| S14.1     | Move Orders (MOV)                              | 17.4.38     |                                     |
| S14.2     | Jump Orders (JMP)                              | 17.4.39     |                                     |

## V. Variants

These rules go in `docs/variants.md`, not the manual.

| Manual ID | Title                              | Rule book | Notes                                                                                                                                   |
|-----------|------------------------------------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------|
| V1.0      | Maxi-Challenge                     | App. I    | Renamed from APPENDIX I: MAXI-CHALLENGE.                                                                                                |
| V1.1      | Maxi-Challenge Pre-Game Turn Sheet |           | Unnumbered in the rule book. Its four subheadings (POPULATION, NON-ASSEMBLY UNITS, UNASSEMBLED UNITS, ASSEMBLED UNITS) stay unnumbered. |
| V2.0      | The Ten Planet War                 | App. II   | Renamed from APPENDIX II: THE TEN PLANET WAR.                                                                                           |

## No manual ID

| Rule book  | Title                                            | Reason                                                    |
|------------|--------------------------------------------------|-----------------------------------------------------------|
| 2          | History of the Empyrean Cluster                  | Unnumbered introductory material.                         |
| 3          | Game Set Up                                      | Chapter heading with no text; its sections become topics. |
| 5          | Population Units                                 | Chapter heading with no text; its sections become topics. |
| 6          | Basic Needs (Food, Consumer Goods, Life Support) | Chapter heading with no text; its sections become topics. |
| 6.1.1.1.1  | Example                                          | Folded into G4.1.1 as an unnumbered label.                |
| 7          | Ships and Colonies                               | Chapter heading with no text; its sections become topics. |
| 8          | Production                                       | Chapter heading with no text; its sections become topics. |
| 9          | Assembly                                         | Chapter heading with no text; its sections become topics. |
| 10         | Technological Levels                             | Chapter heading with no text; its sections become topics. |
| 11         | Transfers                                        | Chapter heading with no text; its sections become topics. |
| 12         | Market                                           | Chapter heading with no text; its sections become topics. |
| 12.1       | For All Games of Empyrean Challenge              | Dropped; see L1.0.                                        |
| 12.2       | Home Market (DELETED)                            | Deleted.                                                  |
| 13         | Ship Movement                                    | Chapter heading with no text; its sections become topics. |
| 13.3.1.1.1 | Chart                                            | Folded into C3.1.1 as an unnumbered label.                |
| 13.3.3     | Combat (DELETED)                                 | Deleted.                                                  |
| 14         | Surveys and Probes                               | Chapter heading with no text; its sections become topics. |
| 14.2.1.1   | Log Base 10                                      | Folded into M2.1 as an unnumbered label.                  |
| 15         | Combat                                           | Chapter heading with no text; its sections become topics. |
| 15.6.4.1   | Example                                          | Folded into E4.0 as an unnumbered label.                  |
| 15.6.5.3.1 | Example                                          | Folded into E6.0 as an unnumbered label.                  |
| 15.6.6.4   | Sample Bombardment (DELETED)                     | Deleted.                                                  |
| 16         | Turn Sequence                                    | Chapter heading with no text; its sections become topics. |
| 16.2       | Stages                                           | Heading only; stages become B3.1 to B3.22.                |
| 17         | Writing Orders                                   | Chapter heading with no text; its sections become topics. |
| 17.4       | Order Formats and Examples                       | Heading only; orders become S4 to S14.                    |
| 17.4.14.1  | Multiple Target AAN Orders                       | Folded into S5.2 by #12.                                  |
| 17.4.16.1  | Multiple Target ADN Orders                       | Folded into S5.4 by #12.                                  |
| 17.4.17.1  | Multiple Target JNK Orders                       | Folded into S5.5 by #12.                                  |
| 17.4.24.1  | Multiple Target TFR Orders                       | Folded into S7.1 by #13.                                  |
| 17.4.25.1  | Multiple Target REC Orders                       | Folded into S7.2 by #13.                                  |
| 17.4.26.1  | Multiple Target PUP Orders                       | Folded into S7.3 by #13.                                  |
| 17.4.27.1  | Multiple Target APU Orders                       | Folded into S7.4 by #13.                                  |
|            | Foreword                                         | Unnumbered front matter.                                  |
|            | Table of Contents                                | Regenerated for the manual.                               |
