<!-- Page 8.5 | source: EC Rules 1980 Odd Pages.pdf, p14 -->

### 8.3.6 RETOOLING, cont.

* Also, in the case of switching from one type of structural unit (STUN, LTSU, SLSU) to another, no retool order is needed.
* If the FCT units in a group are occupied with WIP, they will not retool, even though the BCH, RETL order is accepted and acknowledged on the printout.
  As the FCT are freed from WIP, they retool themselves.

In order to determine the number of FCT that will be retooled on a given turn, determine the total mass of all the items in WIP as if they were complete, and divide by 20 times the TL of the FCT.
Subtract this result from the quantity of FCT in the FCT group; the result is the number of FCT that will be retooled on a given turn.
A FCT group must retool when changing to building the same item at a higher TL.
Retooling uses 0.01 METS and 0.01 NMTS per FCT in the group being retooled.
Retooled FCT's are shown in WIP.

### 8.3.7 RESEARCH AND TL

A factory group ordered to build research (RSCH) will build one research point per FCT times the FCT's TL per game year, divided by four for the amount per turn.
A FCT group may not build any item of a higher TL than that of the s/c it is in.
RSCH and TL's are further explained in Chapter 10, Technological Levels.

### 8.3.8 STUN, LTSU, AND SLSU

STUN are only built in ESC's and OPC's.
STUN can not be built in OBC's.
An attempt to do so will result in the computer changing the STUN to either LTSU or SLSU.

* OBC's TL 1-4 build LTSU, so the computer would change the STUN to LTSU.
* OBC's TL5-10 build SLSU, so the computer would change the STUN to SLSU.
* And if one tried to have an OBC-7, for instance, build LTSU, the computer would automatically change the LTSU to SLSU.

In other words, ordering a heavier type of structural unit than what should have been ordered will cause the computer to correct it to the appropriate lighter type.
But ordering a *lighter* structural unit than what should have been ordered will cause the order to abort.

### 8.3.9 SHORTAGES AND FACTORY GROUP NUMBERS

FCT groups will move as many items through its WIP as there are resources, labor, and fuel to do so.
The computer processes the manufacturing group by group in *group number order*, and within each group starting with WIP 3/4, WIP 1/2, then WIP 1/4.
When the shortage occurs, the computer will cease to work on the portion it was processing, and not do any more processing.
If the shortage has been taken care of on the next turn, the computer will process as normal, starting with FCT group #1, WIP 3/4.
If the shortage still exists, processing will not be done.
There is no way for a player to change a particular FCT group number of a FCT group to another number; if there is a shortage, the player should issue a BCH, SHT to his less necessary FCT groups.
Although the player can not assign a group # to a FCT group when it is initially assembled, he can determine what number the computer assigns to it.
The computer assigns #1 to the first FCT group ASM order it encounters, #2 to the second and so on.
If a player DAS's a FCT group, that number remains unassigned until a new ASM is ordered.

### 8.3.10 AUTOMATION

Automation units (AUT) are used to replace USK for FRM's, MIN's, and FCT's.
The
