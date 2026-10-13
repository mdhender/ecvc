# Rule book to manual mapping

This is the working mapping from `docs/rulebook.md` to `docs/manual.md`, as described in phase 1 of [REORG.md](REORG.md).
The move script reads the tables in this file.

## How to read it

Each subject has one table, sorted by manual ID, so the tables show the outline of the manual.

- **Manual ID** is the new rule ID.
- **Title** is the rule book heading, unless the notes say it was renamed.
- **Rule book** is the section number the text comes from.
  It is blank for new headings.
- **Notes** flag rows for review.

"Heading only" means the rule book heading has no text of its own, so the manual rule is a heading over its subordinate rules.

## How topics were chosen

- A rule book chapter's second-level sections become topics: 13.1 HYPER DRIVES becomes C1.0, and 13.3.1 JUMPS becomes C3.1.
- A chapter with introductory text of its own (1, 18, 20) becomes a single topic, and chapter 19 follows chapter 18 into subject N.
- Subordinate rules keep their rule book order and relative numbering.
- Gaps left by deleted rules are closed up; deleted rules are listed under [No manual ID](#no-manual-id).
- Orders are grouped by intent, and related orders sit together within a group, such as ASM with DAS, and BCH with COM.
- B1.0 is reserved for the walkthrough written in phase 6.

## A. General rules and definitions

| Manual ID | Title                          | Rule book | Notes                                             |
|-----------|--------------------------------|-----------|---------------------------------------------------|
| A1.0      | INTRODUCTION                   | 1         |                                                   |
| A2.0      | COORDINATES                    | 3.1       |                                                   |
| A2.1      | COMPUTER MAP                   | 3.1.1     |                                                   |
| A2.2      | MULTIPLE STAR SYSTEMS          | 3.1.2     |                                                   |
| A2.3      | COORDINATES ON THE PRINTOUT    | 3.1.3     |                                                   |
| A3.0      | SOLAR SYSTEMS                  | 3.2       |                                                   |
| A4.0      | PLANETS                        | 3.3       |                                                   |
| A4.1      | TYPES OF PLANETS               | 3.3.1     |                                                   |
| A4.1.1    | Gas Giants                     | 3.3.1.1   |                                                   |
| A4.1.2    | Terrestrial                    | 3.3.1.2   |                                                   |
| A4.1.3    | Asteroids                      | 3.3.1.3   |                                                   |
| A4.2      | HABITABILITY NUMBERS           | 3.3.2     |                                                   |
| A4.3      | RESOURCE DEPOSITS              | 3.3.3     |                                                   |
| A5.0      | TIME SCALE                     | 3.4       |                                                   |
| A6.0      | INITIAL PRINTOUT AND TURNSHEET | 3.5       | Starting the game; could move to B.               |
| A7.0      | RACE NUMBERS                   | 3.6       |                                                   |
| A8.0      | GLOSSARY                       | 4         | Letter subheadings (A through W) stay unnumbered. |

## B. How to play

| Manual ID | Title               | Rule book | Notes                                                                              |
|-----------|---------------------|-----------|------------------------------------------------------------------------------------|
| B1.0      | HOW TO PLAY         |           | New: the walkthrough written in phase 6.                                           |
| B2.0      | TURN SEQUENCE       | 16.1      | Takes the text of 16.1 DESCRIPTION. Stage steps are anchored as B2.n.k (REORG.md). |
| B2.1      | COMBAT STAGE        | 16.2.1    |                                                                                    |
| B2.2      | PRE SET-UP STAGE    | 16.2.2    |                                                                                    |
| B2.3      | SET-UP STAGE        | 16.2.3    |                                                                                    |
| B2.4      | DIS-ASSEMBLY STAGE  | 16.2.4    |                                                                                    |
| B2.5      | PRE-TRANSFER STAGE  | 16.2.5    |                                                                                    |
| B2.6      | TRANSFER STAGE      | 16.2.6    |                                                                                    |
| B2.7      | BUILD CHANGE STAGE  | 16.2.7    |                                                                                    |
| B2.8      | ASSEMBLY STAGE      | 16.2.8    |                                                                                    |
| B2.9      | MARKET STAGE        | 16.2.9    |                                                                                    |
| B2.10     | SURVEY STAGE        | 16.2.10   |                                                                                    |
| B2.11     | SPY MOVE STAGE      | 16.2.11   |                                                                                    |
| B2.12     | DRAFT STAGE         | 16.2.12   |                                                                                    |
| B2.13     | PAY CHANGE STAGE    | 16.2.13   |                                                                                    |
| B2.14     | NAMING STAGE        | 16.2.14   |                                                                                    |
| B2.15     | SHIP MOVEMENT STAGE | 16.2.15   |                                                                                    |
| B2.16     | RESTART STAGE       | 16.2.16   |                                                                                    |
| B2.17     | PRODUCTION STAGE    | 16.2.17   |                                                                                    |
| B2.18     | ESPIONAGE STAGE     | 16.2.18   |                                                                                    |
| B2.19     | REBELLION STAGE     | 16.2.19   |                                                                                    |
| B2.20     | POP INCREASE STAGE  | 16.2.20   |                                                                                    |
| B2.21     | NEWS RELEASE STAGE  | 16.2.21   |                                                                                    |
| B2.22     | PROBE STAGE         | 16.2.22   |                                                                                    |
| B3.0      | AUXILIARY PLAYERS   | 21        | Heading only. Title typo fixed (AUXILLARY). Regents also in F10.6, N2.9, F4.3.2.   |
| B3.1      | REGENTS             | 21.1      |                                                                                    |
| B3.2      | INDEPENDENTS        | 21.2      |                                                                                    |
| B4.0      | VICTORY CONDITIONS  | 22        | Heading only.                                                                      |
| B4.1      | INDIVIDUAL VICTORY  | 22.1      |                                                                                    |
| B4.2      | RACIAL VICTORY      | 22.2      |                                                                                    |

## C. Movement and navigation

| Manual ID | Title              | Rule book  | Notes                                               |
|-----------|--------------------|------------|-----------------------------------------------------|
| C1.0      | HYPER DRIVES       | 13.1       |                                                     |
| C2.0      | SPACE DRIVES       | 13.2       |                                                     |
| C3.0      | MOVEMENT           | 13.3       |                                                     |
| C3.1      | JUMPS              | 13.3.1     |                                                     |
| C3.1.1    | Over-jumping       | 13.3.1.1   |                                                     |
| C3.1.1.1  | Chart              | 13.3.1.1.1 | Chart; candidate to fold into C3.1.1 without an ID. |
| C3.2      | MOVES              | 13.3.2     |                                                     |
| C3.2.1    | Interstellar Moves | 13.3.2.1   |                                                     |
| C3.3      | FUEL USE           | 13.3.4     | Renumbered; 13.3.3 is deleted.                      |

## D. Combat

| Manual ID | Title                                               | Rule book  | Notes                                                                   |
|-----------|-----------------------------------------------------|------------|-------------------------------------------------------------------------|
| D1.0      | COMBAT OPTIONS                                      | 15.1       | Heading only.                                                           |
| D1.1      | INVADE                                              | 15.1.1     |                                                                         |
| D1.2      | RAID                                                | 15.1.2     |                                                                         |
| D1.3      | SUPPORT                                             | 15.1.3     |                                                                         |
| D1.4      | WITHDRAW                                            | 15.1.4     |                                                                         |
| D1.5      | BOMBARD                                             | 15.1.5     |                                                                         |
| D1.6      | MANEUVER                                            | 15.1.6     |                                                                         |
| D2.0      | INVASION                                            | 15.2       |                                                                         |
| D2.1      | TROOPS                                              | 15.2.3     | TROOPS stays with invasion; ASW and ASC move to E.                      |
| D3.0      | RAIDS                                               | 15.3       |                                                                         |
| D4.0      | SUPPORT                                             | 15.4       |                                                                         |
| D5.0      | WITHDRAWAL                                          | 15.5       |                                                                         |
| D6.0      | BOMBARDMENT                                         | 15.6       | Heading only.                                                           |
| D6.1      | TYPES OF BOMBARDMENT ORDERS                         | 15.6.1     | Heading only.                                                           |
| D6.1.1    | Pre-Maneuver Energy Weapon Fire                     | 15.6.1.1   |                                                                         |
| D6.1.2    | Pre-Maneuver Missile Fire                           | 15.6.1.2   |                                                                         |
| D6.1.3    | After-Maneuver Energy Weapon Fire.                  | 15.6.1.3   |                                                                         |
| D6.1.4    | After-Maneuver Missile Fire.                        | 15.6.1.4   |                                                                         |
| D6.2      | TARGETS                                             | 15.6.2     |                                                                         |
| D6.2.1    | Types of Targets                                    | 15.6.2.1   |                                                                         |
| D6.3      | BOMBARDMENT MISCELLANEOUS                           | 15.6.6     | Heading only.                                                           |
| D6.3.1    | Distances and Speed                                 | 15.6.6.1   |                                                                         |
| D6.3.2    | Commitment Percentage                               | 15.6.6.2   |                                                                         |
| D6.3.3    | Weighted Average                                    | 15.6.6.3   |                                                                         |
| D6.3.4    | More Miscellaneous                                  | 15.6.6.5   | Renumbered; 15.6.6.4 is deleted.                                        |
| D7.0      | COMBAT ORDERS ARE FORBIDDEN ON THE TURN 0 TURNSHEET | 15.7       | No body text; the title is the rule. Keep it verbatim.                  |
| D8.0      | MILITARY SUPPLIES                                   | 15.8       | Heading only. REORG.md listed MTSP under E; supplies fit combat better. |
| D8.1      | WHAT THEY ARE AND WHO RECEIVES THEM                 | 15.8.1     |                                                                         |
| D8.2      | EFFECTS OF A SHORTAGE OF MTSP                       | 15.8.2     |                                                                         |
| D8.3      | EXTRA MTSP PROVISIONS                               | 15.8.3     |                                                                         |
| D9.0      | COMBAT EXECUTION SEQUENCE                           | 15.9       |                                                                         |
| D9.1      | PRE-MANEUVER FIRE                                   | 15.9.1     |                                                                         |
| D9.2      | SHIP MANEUVERS                                      | 15.9.2     |                                                                         |
| D9.3      | POST-MANEUVER FIRE                                  | 15.9.3     |                                                                         |
| D9.4      | TROOP MOVEMENT                                      | 15.9.4     |                                                                         |
| D9.5      | DEFENSIVE WEAPONS VS TROOPS                         | 15.9.5     |                                                                         |
| D9.6      | SURRENDER CHECK                                     | 15.9.6     |                                                                         |
| D9.7      | INVASION CASUALTIES                                 | 15.9.7     |                                                                         |
| D9.7.1    | Calculating Combat Factors                          | 15.9.7.1   | Heading only.                                                           |
| D9.7.1.1  | Troops with MTSP                                    | 15.9.7.1.1 |                                                                         |
| D9.7.1.2  | Troops with no MTSP                                 | 15.9.7.1.2 |                                                                         |
| D9.7.2    | Determining Unit Losses in Combat                   | 15.9.7.2   |                                                                         |
| D9.7.3    | Determining Unit Losses in Raids                    | 15.9.7.3   |                                                                         |
| D10.0     | MISSION COMPLETION                                  | 15.10      |                                                                         |

## E. Weapons and defenses

| Manual ID | Title                             | Rule book  | Notes                                               |
|-----------|-----------------------------------|------------|-----------------------------------------------------|
| E1.0      | ASSAULT WEAPONS                   | 15.2.1     |                                                     |
| E2.0      | ASSAULT CRAFT                     | 15.2.2     |                                                     |
| E2.1      | Transports-Fuel                   | 15.2.2.1   | Invasion procedure, not a weapon rule; consider D2. |
| E3.0      | MISSILES AND MISSILE LAUNCHERS    | 15.6.3     |                                                     |
| E3.1      | Missile Hits                      | 15.6.3.1   |                                                     |
| E4.0      | ANTI-MISSILES                     | 15.6.4     |                                                     |
| E4.1      | Example                           | 15.6.4.1   | Example; candidate to fold into E4.0 without an ID. |
| E4.2      | Used against an invasion          | 15.6.4.2   |                                                     |
| E4.3      | Anti-missile Hits                 | 15.6.4.3   |                                                     |
| E5.0      | ENERGY WEAPONS AND ENERGY SHIELDS | 15.6.5     | Heading only.                                       |
| E5.1      | Offense                           | 15.6.5.1   |                                                     |
| E5.2      | Defense                           | 15.6.5.2   |                                                     |
| E5.3      | Energy Shields                    | 15.6.5.3   | Energy shields could be their own topic, E6.0.      |
| E5.3.1    | Example                           | 15.6.5.3.1 | Example; candidate to fold into E5.3 without an ID. |

## F. Ships and colonies

| Manual ID | Title                                        | Rule book | Notes                                                                                                         |
|-----------|----------------------------------------------|-----------|---------------------------------------------------------------------------------------------------------------|
| F1.0      | TYPES                                        | 7.1       |                                                                                                               |
| F2.0      | LOCATION RESTRICTIONS                        | 7.2       | Heading only.                                                                                                 |
| F2.1      | OPEN COLONIES                                | 7.2.1     |                                                                                                               |
| F2.2      | ENCLOSED SURFACE COLONIES                    | 7.2.2     |                                                                                                               |
| F2.3      | ORBITING COLONIES                            | 7.2.3     |                                                                                                               |
| F2.4      | SHIPS                                        | 7.2.4     |                                                                                                               |
| F3.0      | STRUCTURAL REQUIREMENTS                      | 7.3       | Heading only.                                                                                                 |
| F3.1      | DEFINITION                                   | 7.3.1     |                                                                                                               |
| F3.1.1    | STRUCTURE RATIO                              | 7.3.1.1   |                                                                                                               |
| F3.2      | STRUCTURAL REQUIREMENT EXCEEDED              | 7.3.2     |                                                                                                               |
| F4.0      | SET UPS                                      | 7.4       | Heading only.                                                                                                 |
| F4.1      | DESCRIPTION                                  | 7.4.1     |                                                                                                               |
| F4.2      | S/C ID NUMBERS                               | 7.4.2     |                                                                                                               |
| F4.3      | SET UP RESTRICTIONS                          | 7.4.3     |                                                                                                               |
| F4.3.1    | Restrictions on Type of S/C                  | 7.4.3.1   |                                                                                                               |
| F4.3.2    | Restrictions Ruler - Regent                  | 7.4.3.2   |                                                                                                               |
| F4.3.3    | Permission to Colonize                       | 7.4.3.3   |                                                                                                               |
| F4.3.4    | Failures to Set Up                           | 7.4.3.4   |                                                                                                               |
| F4.3.5    | SET-UPS FOR OTHER PLAYERS                    | 7.4.3.5   |                                                                                                               |
| F4.4      | PERSONNEL                                    | 7.4.4     |                                                                                                               |
| F4.5      | HOW STP ORDERS WORK                          | 7.4.5     |                                                                                                               |
| F4.6      | CONSTRUCTION WORKERS AND SET-UPS             | 7.4.6     |                                                                                                               |
| F4.7      | TRANSPORTS AND SET-UPS                       | 7.4.7     |                                                                                                               |
| F4.8      | ASSEMBLIES AND SET-UPS                       | 7.4.8     |                                                                                                               |
| F4.9      | SET-UP LOCATIONS                             | 7.4.9     |                                                                                                               |
| F5.0      | ADD-ONS                                      | 7.5       | Heading only.                                                                                                 |
| F5.1      | DESCRIPTION                                  | 7.5.1     |                                                                                                               |
| F5.2      | ADN RESTRICTIONS                             | 7.5.2     |                                                                                                               |
| F5.2.1    | ADN Abortions                                | 7.5.2.1   |                                                                                                               |
| F5.3      | HOW ADN ORDERS WORK                          | 7.5.3     |                                                                                                               |
| F5.4      | CONSTRUCTION WORKERS AND ADD-ONS             | 7.5.4     |                                                                                                               |
| F5.5      | TRANSPORTS AND ADD-ONS                       | 7.5.5     |                                                                                                               |
| F5.6      | ASSEMBLIES AND ADD-ONS                       | 7.5.6     |                                                                                                               |
| F5.7      | ADD-ON LOCATIONS                             | 7.5.7     |                                                                                                               |
| F5.8      | SPECIAL RULES                                | 7.5.8     |                                                                                                               |
| F6.0      | JUNKING                                      | 7.6       |                                                                                                               |
| F7.0      | GIFTS                                        | 7.7       |                                                                                                               |
| F8.0      | MERGING                                      | 7.8       |                                                                                                               |
| F9.0      | CONTROL OF PLANETS                           | 7.9       |                                                                                                               |
| F10.0     | ASSEMBLY AND DISASSEMBLY                     | 9.1       | Mixes cadres (SPYS, CNW) with item assembly. Moved as is; the cadre rules are reworked after manual-baseline. |
| F10.1     | ASSEMBLING SPECIAL PURPOSE POPULATION GROUPS | 9.1.1     |                                                                                                               |
| F10.2     | ASSEMBLING UNASSEMBLED ITEMS                 | 9.1.2     |                                                                                                               |
| F10.3     | DISASSEMBLING ASSEMBLED ITEMS                | 9.1.3     |                                                                                                               |
| F10.4     | NON-ASSEMBLY ITEMS                           | 9.1.4     |                                                                                                               |
| F10.5     | USE OF CONSTRUCTION WORKERS                  | 9.1.5     |                                                                                                               |
| F10.6     | REGENTS                                      | 9.1.6     | Duplicates N2.9 REGENTS.                                                                                      |
| F10.7     | MISCELLANEOUS                                | 9.1.7     |                                                                                                               |
| F11.0     | SCRAP                                        | 9.2       |                                                                                                               |

## G. Population

| Manual ID | Title                               | Rule book | Notes                                                 |
|-----------|-------------------------------------|-----------|-------------------------------------------------------|
| G1.0      | TYPES OF POPULATION UNITS           | 5.1       | Heading only.                                         |
| G1.1      | UNEMPLOYABLES (UEM)                 | 5.1.1     |                                                       |
| G1.2      | UNSKILLED WORKERS (USK)             | 5.1.2     |                                                       |
| G1.3      | PROFESSIONALS (PRO)                 | 5.1.3     |                                                       |
| G1.4      | SOLDIERS (SLD)                      | 5.1.4     |                                                       |
| G1.5      | SPIES (SPYS)                        | 5.1.5     |                                                       |
| G1.6      | CONSTRUCTION WORKERS (CNW)          | 5.1.6     |                                                       |
| G1.7      | REBELS                              | 5.1.7     |                                                       |
| G1.8      | TRAINEES (TRN)                      | 5.1.8     |                                                       |
| G1.9      | POPULATION UNITS (POP)              | 5.1.9     |                                                       |
| G2.0      | POPULATION INCREASES                | 5.2       | Heading only.                                         |
| G2.1      | UNEMPLOYABLE INCREASES              | 5.2.1     |                                                       |
| G2.2      | UNSKILLED INCREASES                 | 5.2.2     |                                                       |
| G2.3      | PROFESSIONAL INCREASES              | 5.2.3     |                                                       |
| G2.4      | SOLDIER INCREASES                   | 5.2.4     |                                                       |
| G2.5      | SPY INCREASES                       | 5.2.5     |                                                       |
| G2.6      | CONSTRUCTION WORKER INCREASES       | 5.2.6     |                                                       |
| G2.7      | REBEL (AND REBEL SOLDIER) INCREASES | 5.2.7     | Cross-reference N1 (rebellion).                       |
| G2.8      | TRAINEE INCREASES                   | 5.2.8     |                                                       |
| G3.0      | POPULATION DECREASES                | 5.3       | Heading only.                                         |
| G3.1      | UNEMPLOYABLE DECREASES              | 5.3.1     |                                                       |
| G3.2      | UNSKILLED DECREASES                 | 5.3.2     |                                                       |
| G3.3      | PROFESSIONAL DECREASES              | 5.3.3     |                                                       |
| G3.4      | SOLDIER DECREASES                   | 5.3.4     |                                                       |
| G3.5      | SPY DECREASES                       | 5.3.5     |                                                       |
| G3.6      | CONSTRUCTION WORKER DECREASES       | 5.3.6     |                                                       |
| G3.7      | REBEL DECREASES                     | 5.3.7     | Cross-reference N1 (rebellion).                       |
| G3.8      | TRAINEE DECREASES                   | 5.3.8     |                                                       |
| G3.9      | DEATH RATE                          | 5.3.9     |                                                       |
| G4.0      | FOOD                                | 6.1       | Heading only.                                         |
| G4.1      | CONSUMPTION                         | 6.1.1     |                                                       |
| G4.1.1    | Starvation Rule                     | 6.1.1.1   |                                                       |
| G4.1.1.1  | Example                             | 6.1.1.1.1 | Example; candidate to fold into G4.1.1 without an ID. |
| G4.2      | RATION PERCENTAGE                   | 6.1.2     |                                                       |
| G5.0      | CONSUMER GOODS                      | 6.2       | Heading only.                                         |
| G5.1      | CONSUMPTION                         | 6.2.1     |                                                       |
| G5.2      | BACK PAY                            | 6.2.2     |                                                       |
| G6.0      | LIFE SUPPORT                        | 6.3       | Heading only.                                         |
| G6.1      | CONSUMPTION                         | 6.3.1     |                                                       |
| G6.2      | DEATH RATE AFFECTED                 | 6.3.2     |                                                       |

## H. Production and industry

| Manual ID | Title                                | Rule book | Notes                              |
|-----------|--------------------------------------|-----------|------------------------------------|
| H1.0      | FARMING                              | 8.1       |                                    |
| H1.1      | AMOUNT OF FOOD PRODUCED              | 8.1.1     |                                    |
| H1.2      | EFFECT OF SHORTAGES                  | 8.1.2     |                                    |
| H1.3      | TYPES OF FARMS                       | 8.1.3     | Heading only.                      |
| H1.3.1    | FRM-1                                | 8.1.3.1   |                                    |
| H1.3.2    | FRM-2 through FRM-5                  | 8.1.3.2   |                                    |
| H1.3.3    | FRM-6 through FRM-10                 | 8.1.3.3   |                                    |
| H1.4      | PERSONNEL REQUIRED                   | 8.1.4     |                                    |
| H1.5      | FUEL USE                             | 8.1.5     |                                    |
| H1.6      | SHUT DOWNS AND START UPS             | 8.1.6     |                                    |
| H1.7      | QUANTITY OF FARMS ALLOWED PER PLANET | 8.1.7     |                                    |
| H2.0      | MINING                               | 8.2       |                                    |
| H2.1      | AMOUNT OF RESOURCES MINED            | 8.2.1     |                                    |
| H2.2      | EFFECT OF SHORTAGES                  | 8.2.2     |                                    |
| H2.3      | FUEL AND PERSONNEL REQUIRED          | 8.2.3     |                                    |
| H2.4      | QUANTITY OF MINES ALLOWED            | 8.2.4     |                                    |
| H2.5      | MCH, DEP, AND DAS ORDERS             | 8.2.5     |                                    |
| H3.0      | MANUFACTURING                        | 8.3       |                                    |
| H3.1      | FUEL AND PERSONNEL REQUIREMENTS      | 8.3.1     |                                    |
| H3.2      | EFFICIENCY FACTOR - COST             | 8.3.2     |                                    |
| H3.3      | CAPACITY OF A FACTORY GROUP          | 8.3.3     |                                    |
| H3.4      | WORK IN PROCESS                      | 8.3.4     |                                    |
| H3.5      | BCH, COM, AND DAS ORDERS             | 8.3.5     |                                    |
| H3.6      | RETOOLING                            | 8.3.6     |                                    |
| H3.7      | RESEARCH AND TL                      | 8.3.7     | Cross-reference J4 (improving TL). |
| H3.8      | STUN, LTSU, AND SLSU                 | 8.3.8     |                                    |
| H3.9      | SHORTAGES AND FACTORY GROUP NUMBERS  | 8.3.9     |                                    |
| H3.10     | AUTOMATION                           | 8.3.10    |                                    |

## J. Technology and research

| Manual ID | Title                    | Rule book | Notes                                |
|-----------|--------------------------|-----------|--------------------------------------|
| J1.0      | TL OF SHIPS AND COLONIES | 10.1      |                                      |
| J2.0      | TL OF FACTORIES          | 10.2      |                                      |
| J3.0      | UNIT TL                  | 10.3      |                                      |
| J4.0      | IMPROVING TL             | 10.4      |                                      |
| J4.1      | RESEARCH POINTS          | 10.4.1    |                                      |
| J4.2      | TRANSFERRING RSCH        | 10.4.2    | Cross-reference K5 (RSCH transfers). |
| J4.3      | BUYING AND SELLING RSCH  | 10.4.3    | Cross-reference L (market).          |

## K. Transfers and logistics

| Manual ID | Title                        | Rule book | Notes                                                    |
|-----------|------------------------------|-----------|----------------------------------------------------------|
| K1.0      | TRANSFERS AND PICK-UPS       | 11.1      |                                                          |
| K2.0      | TRANSPORTS                   | 11.2      |                                                          |
| K2.1      | TRANSPORT CAPACITY           | 11.2.1    |                                                          |
| K2.2      | TRANSFERRING TRANSPORTS      | 11.2.2    |                                                          |
| K3.0      | REBEL PICK-UPS AND TRANSFERS | 11.3      |                                                          |
| K3.1      | X OPTION                     | 11.3.1    |                                                          |
| K3.2      | TFR's of Population          | 17.4.24.3 | Moved from 17.4.24.3: a transfer rule, not order syntax. |
| K4.0      | SHORTAGES                    | 11.4      |                                                          |
| K5.0      | RSCH                         | 11.5      |                                                          |
| K6.0      | JETTISONS                    | 11.6      |                                                          |

## L. Markets and trade

| Manual ID | Title                      | Rule book | Notes                                                                     |
|-----------|----------------------------|-----------|---------------------------------------------------------------------------|
| L1.0      | WHO GETS THE MARKET REPORT | 12.1.1    | 12.1 FOR ALL GAMES is dropped; it only survived because 12.2 was deleted. |
| L2.0      | HOW THE MARKET WORKS       | 12.1.2    |                                                                           |
| L3.0      | PRICES                     | 12.1.3    |                                                                           |
| L3.1      | Price of Unemployables     | 12.1.3.1  |                                                                           |
| L4.0      | BIDS                       | 12.1.4    |                                                                           |

## M. Exploration and sensors

| Manual ID | Title         | Rule book | Notes                                             |
|-----------|---------------|-----------|---------------------------------------------------|
| M1.0      | SURVEYS       | 14.1      |                                                   |
| M2.0      | PROBES        | 14.2      |                                                   |
| M2.1      | ORBIT PROBES  | 14.2.1    |                                                   |
| M2.1.1    | Log Base 10   | 14.2.1.1  | Table; candidate to fold into M2.1 without an ID. |
| M2.2      | S/C PROBES    | 14.2.2    |                                                   |
| M2.3      | SYSTEM PROBES | 14.2.3    |                                                   |
| M3.0      | SENSORS       | 14.3      |                                                   |

## N. Espionage and rebellion

| Manual ID | Title                       | Rule book | Notes                                                                                   |
|-----------|-----------------------------|-----------|-----------------------------------------------------------------------------------------|
| N1.0      | REBELLION                   | 18        | Chapter 18 has intro text, so the chapter is one topic.                                 |
| N1.1      | INCREASES                   | 18.1      |                                                                                         |
| N1.1.1    | REBEL INCREASE CHART        | 18.1.1    |                                                                                         |
| N1.1.2    | REBEL SOLDIER INCREASES     | 18.1.2    |                                                                                         |
| N1.2      | DECREASES                   | 18.2      |                                                                                         |
| N1.3      | REBELLION                   | 18.3      |                                                                                         |
| N1.4      | AFTERMATH                   | 18.4      |                                                                                         |
| N1.5      | SUPPORT DURING REBELLION    | 18.5      |                                                                                         |
| N2.0      | ESPIONAGE                   | 19        | Heading only. Chapter 19 is one topic, to match N1.                                     |
| N2.1      | GENERAL RULES               | 19.1      |                                                                                         |
| N2.2      | GROUP G SPYS                | 19.2      |                                                                                         |
| N2.2.1    | CASUALTIES                  | 19.2.1    | The unnumbered heading GROUP G SPYS, CONT. follows this rule; its text belongs to N2.2. |
| N2.3      | GROUP A SPYS                | 19.3      |                                                                                         |
| N2.4      | GROUP B SPYS                | 19.4      |                                                                                         |
| N2.5      | GROUP C SPYS                | 19.5      |                                                                                         |
| N2.6      | GROUP D SPYS                | 19.6      |                                                                                         |
| N2.6.1    | ASSASSINATION CASUALTIES    | 19.6.1    |                                                                                         |
| N2.7      | GROUP E SPYS                | 19.7      |                                                                                         |
| N2.8      | GROUP F SPYS                | 19.8      |                                                                                         |
| N2.8.1    | SECTIONS OF GROUP F REPORTS | 19.8.1    |                                                                                         |
| N2.9      | REGENTS                     | 19.9      | Duplicates F10.6 REGENTS.                                                               |

## P. Diplomacy and communications

| Manual ID | Title               | Rule book | Notes                                                   |
|-----------|---------------------|-----------|---------------------------------------------------------|
| P1.0      | COMMUNICATIONS      | 20        | Chapter 20 has intro text, so the chapter is one topic. |
| P1.1      | NEWS SERVICE        | 20.1      |                                                         |
| P1.1.1    | NEWS RELEASES       | 20.1.1    |                                                         |
| P1.2      | DIPLOMATIC MESSAGES | 20.2      |                                                         |

## R. Reference material

| Manual ID | Title                              | Rule book | Notes                                                                                                      |
|-----------|------------------------------------|-----------|------------------------------------------------------------------------------------------------------------|
| R1.0      | APPENDIX I: MAXI-CHALLENGE         | App. I    | Variant rules.                                                                                             |
| R2.0      | APPENDIX II: THE TEN PLANET WAR    | App. II   | Variant rules.                                                                                             |
| R3.0      | MAXI-CHALLENGE PRE-GAME TURN SHEET |           | Its four subheadings (POPULATION, NON-ASSEMBLY UNITS, UNASSEMBLED UNITS, ASSEMBLED UNITS) stay unnumbered. |
| R4.0      | PRINT OUT INTERPRETATION           |           |                                                                                                            |
| R5.0      | ERROR MESSAGES                     |           | Could move to S.                                                                                           |
| R6.0      | UNIT CHARACTERISTICS SUMMARY       |           |                                                                                                            |

## S. Orders

| Manual ID | Title                                          | Rule book   | Notes                               |
|-----------|------------------------------------------------|-------------|-------------------------------------|
| S1.0      | HOW THE TURN SHEET SHOULD LOOK                 | 17.1        | Chapter 17 heading is dropped.      |
| S2.0      | GENERAL RULES ON WRITING ORDERS                | 17.2        |                                     |
| S2.1      | ZEROS                                          | 17.2.1      |                                     |
| S2.2      | COMMAS                                         | 17.2.2      |                                     |
| S2.3      | TL'S                                           | 17.2.3      |                                     |
| S2.4      | RACE NUMBERS AND TL NUMBERS                    | 17.2.4      |                                     |
| S3.0      | SAMPLE TURNSHEET                               | 17.3        |                                     |
| S4.0      | COMBAT ORDERS                                  |             | New group heading.                  |
| S4.1      | TACTICAL MANEUVER ORDERS (TMV)                 | 17.4.1      |                                     |
| S4.2      | CLOSE ORDERS (CLS)                             | 17.4.2      |                                     |
| S4.3      | RUN ORDERS (RUN)                               | 17.4.3      |                                     |
| S4.4      | PRE-MANEUVER ENERGY WEAPON FIRE ORDERS (PME)   | 17.4.4      |                                     |
| S4.5      | PRE-MANEUVER MISSILE FIRE ORDERS (PMM)         | 17.4.5      |                                     |
| S4.6      | AFTER-MANEUVER ENERGY WEAPON FIRE ORDERS (AME) | 17.4.6      |                                     |
| S4.7      | AFTER-MANEUVER MISSILE FIRE ORDERS (AMM)       | 17.4.7      |                                     |
| S4.8      | INVASION ORDERS (INV)                          | 17.4.8      |                                     |
| S4.9      | RAID ORDERS (RAD)                              | 17.4.9      |                                     |
| S4.10     | DEFENSIVE TROOP SUPPORT ORDERS (DTS)           | 17.4.10     |                                     |
| S4.11     | OFFENSIVE TROOP SUPPORT ORDERS (OTS)           | 17.4.11     |                                     |
| S4.12     | WITHDRAW ORDERS (WTD)                          | 17.4.12     |                                     |
| S5.0      | SHIP AND COLONY ORDERS                         |             | New group heading.                  |
| S5.1      | PERMISSION TO COLONIZE ORDERS (PTC)            | 17.4.13     |                                     |
| S5.2      | ALLOW ADD-ON ORDERS (AAN)                      | 17.4.14     |                                     |
| S5.2.1    | Multiple Target AAN Orders                     | 17.4.14.1   |                                     |
| S5.3      | SET UP ORDERS (STP)                            | 17.4.15     |                                     |
| S5.4      | ADD-ON ORDERS (ADN)                            | 17.4.16     |                                     |
| S5.4.1    | Multiple Target ADN Orders                     | 17.4.16.1   |                                     |
| S5.5      | JUNK ORDERS (JNK)                              | 17.4.17     |                                     |
| S5.5.1    | Multiple Target JNK Orders                     | 17.4.17.1   |                                     |
| S5.6      | GIVE ORDERS (GIV)                              | 17.4.18     |                                     |
| S5.7      | ACCEPT ORDERS (ACP)                            | 17.4.19     |                                     |
| S5.8      | MERGE ORDERS (MRG)                             | 17.4.20     |                                     |
| S5.9      | CONTROL ORDERS (CON)                           | 17.4.44     |                                     |
| S5.10     | UNCONTROL ORDERS (UNC)                         | 17.4.45     |                                     |
| S6.0      | ASSEMBLY AND SCRAP ORDERS                      |             | New group heading.                  |
| S6.1      | ASSEMBLY ORDERS (ASM)                          | 17.4.32     |                                     |
| S6.1.1    | Multiple ASM Orders                            | 17.4.32.1   |                                     |
| S6.2      | DISASSEMBLY ORDERS (DAS)                       | 17.4.50     |                                     |
| S6.2.1    | Multiple DAS Orders                            | 17.4.50.1   |                                     |
| S6.3      | SCRAP ORDERS (SCR)                             | 17.4.23     |                                     |
| S6.3.1    | Multiple Scrap Orders                          | 17.4.23.1   |                                     |
| S7.0      | TRANSFER ORDERS                                |             | New group heading.                  |
| S7.1      | TRANSFER ORDERS (TFR)                          | 17.4.24     |                                     |
| S7.1.1    | Multiple Target TFR Orders                     | 17.4.24.1   |                                     |
| S7.1.2    | Multiple TFR Orders                            | 17.4.24.2   |                                     |
| S7.2      | RECEIVE ORDERS (REC)                           | 17.4.25     |                                     |
| S7.2.1    | Multiple Target REC Orders                     | 17.4.25.1   |                                     |
| S7.2.2    | To Cancel Receive Orders                       | 17.4.25.2   | Order persistence; could move to K. |
| S7.2.3    | Multiple REC Orders                            | 17.4.25.3   |                                     |
| S7.3      | PICK UP ORDERS (PUP)                           | 17.4.26     |                                     |
| S7.3.1    | Multiple Target PUP Orders                     | 17.4.26.1   |                                     |
| S7.3.2    | Multiple PUP Orders                            | 17.4.26.2   |                                     |
| S7.4      | ALLOW PICK UP ORDERS (APU)                     | 17.4.27     |                                     |
| S7.4.1    | Multiple Target APU Orders                     | 17.4.27.1   |                                     |
| S7.4.1.1  | Cancelling APU orders                          | 17.4.27.1.1 | Order persistence; could move to K. |
| S7.4.2    | Multiple APU orders                            | 17.4.27.2   |                                     |
| S8.0      | PRODUCTION ORDERS                              |             | New group heading.                  |
| S8.1      | BUILD CHANGE ORDERS (BCH)                      | 17.4.28     |                                     |
| S8.2      | COMBINE ORDERS (COM)                           | 17.4.21     |                                     |
| S8.3      | MINE CHANGE ORDERS (MCH)                       | 17.4.29     |                                     |
| S8.4      | DEPOSIT ORDERS (DEP)                           | 17.4.22     |                                     |
| S8.5      | SHUT DOWN ORDERS (SHT)                         | 17.4.30     |                                     |
| S8.6      | START UP ORDERS (STU)                          | 17.4.31     |                                     |
| S9.0      | MARKET ORDERS                                  |             | New group heading.                  |
| S9.1      | BUY ORDERS (BUY)                               | 17.4.33     |                                     |
| S9.2      | SELL ORDERS (SEL)                              | 17.4.34     |                                     |
| S10.0     | EXPLORATION ORDERS                             |             | New group heading.                  |
| S10.1     | PROBE ORDERS (PRB)                             | 17.4.35     |                                     |
| S10.2     | SURVEY ORDERS (SUR)                            | 17.4.36     |                                     |
| S11.0     | ESPIONAGE ORDERS                               |             | New group heading.                  |
| S11.1     | SPY MOVE ORDERS (SPM)                          | 17.4.37     |                                     |
| S12.0     | POPULATION ORDERS                              |             | New group heading.                  |
| S12.1     | DRAFT ORDERS (DRF)                             | 17.4.40     |                                     |
| S12.2     | DISBAND ORDERS (DSB)                           | 17.4.41     |                                     |
| S12.3     | PAY ORDERS (PAY)                               | 17.4.42     |                                     |
| S12.4     | RATION ORDERS (RTN)                            | 17.4.43     |                                     |
| S13.0     | NAMING AND NEWS ORDERS                         |             | New group heading.                  |
| S13.1     | NAME ORDERS (NAM)                              | 17.4.46     |                                     |
| S13.2     | PLAYER NAME ORDERS (NOM)                       | 17.4.47     |                                     |
| S13.3     | PLANET NAME ORDERS (NAP)                       | 17.4.48     |                                     |
| S13.4     | NEWS RELEASE ORDERS (NSR)                      | 17.4.49     |                                     |
| S14.0     | MOVEMENT ORDERS                                |             | New group heading.                  |
| S14.1     | MOVE ORDERS (MOV)                              | 17.4.38     |                                     |
| S14.2     | JUMP ORDERS (JMP)                              | 17.4.39     |                                     |

## No manual ID

| Rule book | Title                                            | Reason                                                    |
|-----------|--------------------------------------------------|-----------------------------------------------------------|
| 2         | HISTORY OF THE EMPYREAN CLUSTER                  | Unnumbered introductory material.                         |
| 3         | GAME SET UP                                      | Chapter heading with no text; its sections become topics. |
| 5         | POPULATION UNITS                                 | Chapter heading with no text; its sections become topics. |
| 6         | BASIC NEEDS (FOOD, CONSUMER GOODS, LIFE SUPPORT) | Chapter heading with no text; its sections become topics. |
| 7         | SHIPS AND COLONIES                               | Chapter heading with no text; its sections become topics. |
| 8         | PRODUCTION                                       | Chapter heading with no text; its sections become topics. |
| 9         | ASSEMBLY                                         | Chapter heading with no text; its sections become topics. |
| 10        | TECHNOLOGICAL LEVELS                             | Chapter heading with no text; its sections become topics. |
| 11        | TRANSFERS                                        | Chapter heading with no text; its sections become topics. |
| 12        | MARKET                                           | Chapter heading with no text; its sections become topics. |
| 12.1      | FOR ALL GAMES OF EMPYREAN CHALLENGE              | Dropped; see L1.0.                                        |
| 12.2      | HOME MARKET (DELETED)                            | Deleted.                                                  |
| 13        | SHIP MOVEMENT                                    | Chapter heading with no text; its sections become topics. |
| 13.3.3    | COMBAT (DELETED)                                 | Deleted.                                                  |
| 14        | SURVEYS AND PROBES                               | Chapter heading with no text; its sections become topics. |
| 15        | COMBAT                                           | Chapter heading with no text; its sections become topics. |
| 15.6.6.4  | Sample Bombardment (DELETED)                     | Deleted.                                                  |
| 16        | TURN SEQUENCE                                    | Chapter heading with no text; its sections become topics. |
| 16.2      | STAGES                                           | Heading only; stages become B2.1 to B2.22.                |
| 17        | WRITING ORDERS                                   | Chapter heading with no text; its sections become topics. |
| 17.4      | ORDER FORMATS AND EXAMPLES                       | Heading only; orders become S4 to S14.                    |
|           | FOREWORD                                         | Unnumbered front matter.                                  |
|           | TABLE OF CONTENTS                                | Regenerated for the manual.                               |
