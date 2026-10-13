# Phase 4 edits

This is the reviewed list of changes made in phase 4 (Connect) of [REORG.md](REORG.md): sentences that relied on the rule book's order or numbering.
`tools/reorg/build.py` applies these edits after copying the rule book text, and `tools/reorg/check.py` accepts them as the only differences from `docs/rulebook.md`.

## How to read it

- Each `###` heading names the manual rule that holds the line.
- In each `diff` block, the `-` line is the line as the build first writes it, and the `+` lines replace it.
  A `-` line with no `+` line deletes it.
- A replaced reference keeps the original in a comment, such as `[G2.2](#rule-G2.2)<!-- was 5.2.2 -->`.
  The build marks the rule book's own links the same way, such as `[S4.4](#rule-S4.4)<!-- was 17.4.4 -->`.
- A reference to a whole rule book chapter points to the rule the sentence is about when there is one, and to the subject otherwise.

## Edits

### A2.2

```diff
-There is an orbit 0 surrounding the entire star system and its planets, which serves all the stars of a multiple star system, and it will be explained later.
+There is an orbit 0 surrounding the entire star system and its planets, which serves all the stars of a multiple star system, and it is explained in [A3.0](#rule-A3.0)<!-- was it will be explained later -->.
```

### A3.0

```diff
-If there are two or more stars in a coordinate point, orbit 0 surrounds the stars and the planets, as explained above.
+If there are two or more stars in a coordinate point, orbit 0 surrounds the stars and the planets, as explained in [A2.2](#rule-A2.2)<!-- was as explained above -->.
```

### A4.2

```diff
-(Further explained in section 5.3).
+(Further explained in [G3.0](#rule-G3.0)<!-- was section 5.3 -->).
```

### A7.0

```diff
-| AME  | After-maneuver energy-weapon fire | See Combat (15).                                   |
+| AME  | After-maneuver energy-weapon fire | See Combat ([D6.1.3](#rule-D6.1.3)<!-- was 15 -->).                                   |
```

```diff
-| AMM  | After-maneuver missile fire       | See Combat (15).                                   |
+| AMM  | After-maneuver missile fire       | See Combat ([D6.1.4](#rule-D6.1.4)<!-- was 15 -->).                                   |
```

```diff
-| DTS   | Defensive troop support | See Combat (15).                                    |
+| DTS   | Defensive troop support | See Combat ([D4.0](#rule-D4.0)<!-- was 15 -->).                                    |
```

```diff
-| INV  | Invade | See Combat (15). |
+| INV  | Invade | See Combat ([D2.0](#rule-D2.0)<!-- was 15 -->). |
```

```diff
-| OTS  | Offensive troop support | See Combat (15).                    |
+| OTS  | Offensive troop support | See Combat ([D4.0](#rule-D4.0)<!-- was 15 -->).                    |
```

```diff
-| PME   | Pre-maneuver energy weapon fire | See Combat (15).                                                          |
+| PME   | Pre-maneuver energy weapon fire | See Combat ([D6.1.1](#rule-D6.1.1)<!-- was 15 -->).                                                          |
```

```diff
-| PMM   | Pre-maneuver missile fire       | See Combat (15).                                                          |
+| PMM   | Pre-maneuver missile fire       | See Combat ([D6.1.2](#rule-D6.1.2)<!-- was 15 -->).                                                          |
```

```diff
-| RAD   | Raid           | See Combat (15).                                           |
+| RAD   | Raid           | See Combat ([D3.0](#rule-D3.0)<!-- was 15 -->).                                           |
```

### B2.0

The free probe report is described in A2.3, now in another subject.

```diff
-The printout also shows her player ID#, her home colony's ID#, her race number, and a free magnitude-10 probe report as mentioned previously.
+The printout also shows her player ID#, her home colony's ID#, her race number, and a free magnitude-10 probe report as mentioned in [A2.3](#rule-A2.3)<!-- was as mentioned previously -->.
```

### B3.0

```diff
-Combat is the only exception; see 15.9 for details.
+Combat is the only exception; see [D9.0](#rule-D9.0)<!-- was 15.9 --> for details.
```

### B4.1

Chapter 17 is subject S.

```diff
-A Regent may use any of the orders listed in Chapter 17, with the following exceptions: A Regent cannot fulfill the victory conditions.
+A Regent may use any of the orders listed in subject [S](#s-orders)<!-- was Chapter 17 -->, with the following exceptions: A Regent cannot fulfill the victory conditions.
```

```diff
-\*\* The s/c is gifted back to the Ruler during the disassembly stage, (16.2.4, step 5).
+\*\* The s/c is gifted back to the Ruler during the disassembly stage, ([B3.4.5](#rule-B3.4.5)<!-- was 16.2.4, step 5 -->).
```

### C2.0

```diff
-They are used in combat, however, See 15.9.2 for details.
+They are used in combat, however, See [D9.2](#rule-D9.2)<!-- was 15.9.2 --> for details.
```

### C3.1

Chapter 14 as a whole is subject M; the sentence is about system probes, M2.3.

```diff
-(See Chapter 14 for more information).
+(See [M2.3](#rule-M2.3)<!-- was Chapter 14 --> for more information).
```

### D6.1.1

```diff
-This is explained in 15.6.2, Targets.
+This is explained in [D6.2](#rule-D6.2)<!-- was 15.6.2 -->, Targets.
```

### D9.7.3

```diff
-Casualties from a raid are computed as above and then multiplied by a fraction.
+Casualties from a raid are computed as in [D9.7.2](#rule-D9.7.2)<!-- was as above --> and then multiplied by a fraction.
```

### E4.1

```diff
-Besides defending against bombardment, as explained above, ANM's are also used defending against invasions and raids.
+Besides defending against bombardment, as explained in [E4.0](#rule-E4.0)<!-- was as explained above -->, ANM's are also used defending against invasions and raids.
```

### E5.2

```diff
-If the s/c faces both a bombardment and an invasion, the EWP's are fired in both cases, following the combat execution sequence detailed in section 15.9
+If the s/c faces both a bombardment and an invasion, the EWP's are fired in both cases, following the combat execution sequence detailed in [D9.0](#rule-D9.0)<!-- was section 15.9 -->
```

### F3.1

```diff
-The total volume units times the STRUCTURE RATIO, (see 7.3.1.1), gives the s/c structural requirement.
+The total volume units times the STRUCTURE RATIO, (see [F3.1.1](#rule-F3.1.1)<!-- was 7.3.1.1 -->), gives the s/c structural requirement.
```

### F3.1.1

The summary is now annex R3.0.

```diff
-For the number of volume units per item see the UNIT CHARACTERISTICS SUMMARY on the back cover.
+For the number of volume units per item see the UNIT CHARACTERISTICS SUMMARY in [R3.0](#rule-R3.0)<!-- was on the back cover -->.
```

### F4.4

The summary is now annex R3.0.

```diff
-The section entitled Personnel Requirements/Unit on the Unit Characteristics Summary, shown on the back cover, gives this information.
+The section entitled Personnel Requirements/Unit on the Unit Characteristics Summary, shown in [R3.0](#rule-R3.0)<!-- was on the back cover -->, gives this information.
```

### F5.4

```diff
-See 7.4.6.
+See [F4.6](#rule-F4.6)<!-- was 7.4.6 -->.
```

### F5.5

```diff
-See 7.4.7.
+See [F4.7](#rule-F4.7)<!-- was 7.4.7 -->.
```

### F5.6

```diff
-All rules regarding assemblies and set-ups apply to ADN's too, (see 7.4.8) with the addition that factories in an ADN can also be ordered to be added-on to an existing factory group.
+All rules regarding assemblies and set-ups apply to ADN's too, (see [F4.8](#rule-F4.8)<!-- was 7.4.8 -->) with the addition that factories in an ADN can also be ordered to be added-on to an existing factory group.
```

### F9.0

```diff
-Controlling planets is the object of the game (see chapter 22, Victory Conditions).
+Controlling planets is the object of the game (see [B5.0](#rule-B5.0)<!-- was chapter 22 -->, Victory Conditions).
```

### G3.1

```diff
-See 5.2.2.
+See [G2.2](#rule-G2.2)<!-- was 5.2.2 -->.
```

### G3.7

Written as "(see N2.0, Espionage)" to match "(see 8.3, Manufacturing)".

```diff
-Rebel decreases are caused by the Ruler ordering his spies to convert those rebels into loyal population units (see 19. Espionage), and by improved standard of living.
+Rebel decreases are caused by the Ruler ordering his spies to convert those rebels into loyal population units (see [N2.0](#rule-N2.0), Espionage<!-- was 19. Espionage -->), and by improved standard of living.
```

### G4.1

```diff
-If the rationed amount of food is less than 1/16 of a food unit per POP per turn, the computer will divide the food equally, and check for starvation, according to the Starvation Rule below.
+If the rationed amount of food is less than 1/16 of a food unit per POP per turn, the computer will divide the food equally, and check for starvation, according to the Starvation Rule ([G4.1.1](#rule-G4.1.1))<!-- was below -->.
```

### H1.0

Chapter 9 is F10.0 and F11.0; these references are about assembly, F10.0.

```diff
-This is done with an ASM (assembly) order, and is explained in detail in Chapter 9, Assembly.
+This is done with an ASM (assembly) order, and is explained in detail in [F10.0](#rule-F10.0)<!-- was Chapter 9 -->, Assembly.
```

### H1.7

```diff
-And there is no limit to FRM's of any TL in ships, enclosed surface colonies, or orbiting colonies, providing there is enough space for them, and the restrictions in 8.1.3 are observed.
+And there is no limit to FRM's of any TL in ships, enclosed surface colonies, or orbiting colonies, providing there is enough space for them, and the restrictions in [H1.3](#rule-H1.3)<!-- was 8.1.3 --> are observed.
```

### H2.0

```diff
-This is done with an ASM (assembly) order, and is explained in Chapter 9, Assembly.
+This is done with an ASM (assembly) order, and is explained in [F10.0](#rule-F10.0)<!-- was Chapter 9 -->, Assembly.
```

### H2.5

```diff
-This is explained fully in Chapter 9, Assembly.
+This is explained fully in [F10.0](#rule-F10.0)<!-- was Chapter 9 -->, Assembly.
```

The MCH order is S8.3.

```diff
-Examples of MCH orders are shown in Chapter 17, Order Writing.
+Examples of MCH orders are shown in [S8.3](#rule-S8.3)<!-- was Chapter 17, Order Writing -->.
```

### H3.0

```diff
-In order for a factory unit to work, it must be taken from storage and assembled into a FCT group, as is explained in Chapter 9, Assembly.
+In order for a factory unit to work, it must be taken from storage and assembled into a FCT group, as is explained in [F10.0](#rule-F10.0)<!-- was Chapter 9 -->, Assembly.
```

### H3.1

```diff
-Each FCT requires one PRO times the efficiency factor (see 8.3.2) and three USK times the efficiency factor.
+Each FCT requires one PRO times the efficiency factor (see [H3.2](#rule-H3.2)<!-- was 8.3.2 -->) and three USK times the efficiency factor.
```

### H3.2

The summary is now annex R3.0.

```diff
-The quantity of METS and NMTS required to build an item, (see the back cover, UNIT CHARACTERISTICS SUMMARY), is multiplied by the FCT group's efficiency factor.
+The quantity of METS and NMTS required to build an item, (see [R3.0](#rule-R3.0)<!-- was the back cover -->, UNIT CHARACTERISTICS SUMMARY), is multiplied by the FCT group's efficiency factor.
```

### H3.4

Drops the stray period after 8.3.3.

```diff
-Using the example in 8.3.3. of 50,000 FCT-1 being ASM'd (on turn 3) to build 62,500 LFS-2, the printout will report the WIP in this way:
+Using the example in [H3.3](#rule-H3.3)<!-- was 8.3.3. --> of 50,000 FCT-1 being ASM'd (on turn 3) to build 62,500 LFS-2, the printout will report the WIP in this way:
```

### H3.5

```diff
-Once ordered to manufacture an item, a factory group will continue to do so, unless ordered to build something else with a build change order (BCH - see 8.3.6, Retooling), or to shut down (a BCH, SHT order).
+Once ordered to manufacture an item, a factory group will continue to do so, unless ordered to build something else with a build change order (BCH - see [H3.6](#rule-H3.6)<!-- was 8.3.6 -->, Retooling), or to shut down (a BCH, SHT order).
```

```diff
-This is explained in Chapter 9, Assembly.
+This is explained in [F10.0](#rule-F10.0)<!-- was Chapter 9 -->, Assembly.
```

### H3.7

Chapter 10 is subject J.

```diff
-RSCH and TL's are further explained in Chapter 10, Technological Levels.
+RSCH and TL's are further explained in subject [J](#j-technology-and-research)<!-- was Chapter 10 -->, Technological Levels.
```

### J2.0

```diff
-More about transferring and selling TL's and RSCH in section 10.4, IMPROVING TL.
+More about transferring and selling TL's and RSCH in [J4.0](#rule-J4.0)<!-- was section 10.4 -->, IMPROVING TL.
```

### J4.2

```diff
-TFR'ing RSCH requires TPT's, but RSCH do not use up any TPT capacity (see 11.1).
+TFR'ing RSCH requires TPT's, but RSCH do not use up any TPT capacity (see [K1.0](#rule-K1.0)<!-- was 11.1 -->).
```

### K1.0

```diff
-Gold and RSCH do not require a REC order (see 11.5).
+Gold and RSCH do not require a REC order (see [K5.0](#rule-K5.0)<!-- was 11.5 -->).
```

```diff
-Group G spies may be TFR'd into any s/c, and PUP'd back out of it, to conduct espionage; they remain under their Ruler's control (see 19.2).
+Group G spies may be TFR'd into any s/c, and PUP'd back out of it, to conduct espionage; they remain under their Ruler's control (see [N2.2](#rule-N2.2)<!-- was 19.2 -->).
```

### K3.0

```diff
-See Chapter 18, Rebellion, for further details regarding rebels.
+See [N1.0](#rule-N1.0)<!-- was Chapter 18 -->, Rebellion, for further details regarding rebels.
```

### N2.6

The SPM order is S11.1.

```diff
-Examples of this are shown in the SPM orders in Chapter 17, Writing Orders.
+Examples of this are shown in the SPM orders in [S11.1](#rule-S11.1)<!-- was Chapter 17, Writing Orders -->.
```

### N2.7

```diff
-More about this is covered in Chapter 18, Rebellion.
+More about this is covered in [N1.0](#rule-N1.0)<!-- was Chapter 18 -->, Rebellion.
```

### S2.2

```diff
-The sample turnsheet, section 17.3, has examples of this.
+The sample turnsheet, [S3.0](#rule-S3.0)<!-- was section 17.3 -->, has examples of this.
```

### S7.1

```diff
-  Group G SPYS may be TFR'd into a foreign s/c to conduct espionage, but they remain under their Ruler's control (see 11.1).
+  Group G SPYS may be TFR'd into a foreign s/c to conduct espionage, but they remain under their Ruler's control (see [K1.0](#rule-K1.0)<!-- was 11.1 -->).
```

### S7.2

```diff
-  REC orders are used only for TFR's from another Ruler of the same race, or his Regent (see 11.1).
+  REC orders are used only for TFR's from another Ruler of the same race, or his Regent (see [K1.0](#rule-K1.0)<!-- was 11.1 -->).
```

### S7.3

```diff
-  Nothing can be PUP'd from a Ruler of another race, except the player's own group G SPYS (see 11.1).
+  Nothing can be PUP'd from a Ruler of another race, except the player's own group G SPYS (see [K1.0](#rule-K1.0)<!-- was 11.1 -->).
```

### S7.4

```diff
-  APU orders are used only for PUP's by another Ruler of the same race, or his Regent (see 11.1).
+  APU orders are used only for PUP's by another Ruler of the same race, or his Regent (see [K1.0](#rule-K1.0)<!-- was 11.1 -->).
```

### V1.0

```diff
-   (See 8.3, Manufacturing).
+   (See [H3.0](manual.md#rule-H3.0)<!-- was 8.3 -->, Manufacturing).
```

```diff
-7. TFR, APU, REC, ADN, and STP orders are handled as in the standard rules (see 7.4.3.5, 7.5.8, and 11.1).
+7. TFR, APU, REC, ADN, and STP orders are handled as in the standard rules (see [F4.3.5](manual.md#rule-F4.3.5)<!-- was 7.4.3.5 -->, [F5.8](manual.md#rule-F5.8)<!-- was 7.5.8 -->, and [K1.0](manual.md#rule-K1.0)<!-- was 11.1 -->).
```

### V2.0

```diff
-10. The efficiency factor (see 8.3, Manufacturing) is always 1 when calculating cost, and is never less than 1 when calculating personnel requirements.
+10. The efficiency factor (see [H3.0](manual.md#rule-H3.0)<!-- was 8.3 -->, Manufacturing) is always 1 when calculating cost, and is never less than 1 when calculating personnel requirements.
```

```diff
-11. TFR, APU, REC, ADN, and STP orders are handled as in the standard rules (see 7.4.3.5, 7.5.8, and 11.1).
+11. TFR, APU, REC, ADN, and STP orders are handled as in the standard rules (see [F4.3.5](manual.md#rule-F4.3.5)<!-- was 7.4.3.5 -->, [F5.8](manual.md#rule-F5.8)<!-- was 7.5.8 -->, and [K1.0](manual.md#rule-K1.0)<!-- was 11.1 -->).
```

## Reviewed, not changed

These lines refer to other text by position or by name, but still read correctly in the manual.

- C3.1.1 "The following chart shows the odds.": the chart is folded into the same rule.
- D2.2 "(see MTSP)": refers to the glossary term, which is unchanged.
- F4.3 and F5.2 "restrictions listed below": the restrictions follow in the same rule or its subordinate rules.
- J4.1, N1.0, N2.8.1, P1.0, R1.0 "below", and S10.1 "The above examples": the text referred to is in the same rule.
- A7.0 and R1.0 "listed in the Glossary": the glossary is A7.0, and the name still fits.
- A7.0 "the text of this rule book" and the Foreword "this rule book": they refer to the book, not a section.
