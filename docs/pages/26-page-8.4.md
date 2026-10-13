<!-- Page 8.4 | source: EC Rules 1980 Even Pages.pdf, p13 -->

### 8.3.3 CAPACITY OF A FACTORY GROUP

One FCT (factory unit) produces 5 x its TL MU per turn; 20 MU x its TL per year.
This annual production in mass units, times the number of factory units in the group, divided by the mass units per item, will give the quantity of an item to be produced per year by a FCT group.
For example: A FCT group of 50,000 FCT-1 is set up to build LFS-2.
20 (mass units per year) times 50,000 (number of FCT units in the group) divided by 16 (a LFS-2 is 16 mass units) will equal 62,500 LFS-2 produced per year, or 15,625 LFS-2 produced per turn.

### 8.3.4 WORK IN PROCESS

Work in process (WIP) includes all items in the process of being manufactured.
Using the example in 8.3.3. of 50,000 FCT-1 being ASM'd (on turn 3) to build 62,500 LFS-2, the printout will report the WIP in this way:

| TURN | WIP 1/4 COMP. | WIP 1/2 COMP. | WIP 3/4 COMP. |
|------|---------------|---------------|---------------|
| 3    | 0             | 0             | 0             |
| 4    | 62,500 LFS-2  | 0             | 0             |
| 5    | 0             | 62,500 LFS-2  | 0             |
| 6    | 0             |               | 62,500 LFS-2  |

Note that the FCT group does not complete 1/4 of the LFS-2 per turn (15,625 in other words), but instead will get the entire 62,500 one quarter of the way to being complete.
On turn 7 of the example, 62,500 LFS-2 will show up on the storage report on the printout, and the WIP will look like it did on turn 3.

Let's say that we assembled this group on turn three, and assembled more FCT units to the group on turn 4, and turn 5 and turn 6.
The printout will show:

| TURN | WIP1/4 COMP. | WIP 1/2 COMP. | WIP 3/4 COMP. |
|------|--------------|---------------|---------------|
| 3    | 0            | 0             | 0             |
| 4    | 62,500 LFS-2 | 0             | 0             |
| 5    | 62,500 LFS-2 | 62,500 LFS-2  | 0             |
| 6    | 62,500 LFS-2 | 62,500 LFS-2  | 62,500 LFS-2  |

Starting on turn 7, 62,500 LFS-2 are added to storage each turn.

### 8.3.5 BCH, COM, AND DAS ORDERS

Once ordered to manufacture an item, a factory group will continue to do so, unless ordered to build something else with a build change order (BCH - see 8.3.6, Retooling), or to shut down (a BCH, SHT order).
Once ordered to shut down, a FCT group (still assembled) remains shut down, unless ordered to start up (with a BCH, STU order).
One final way to stop a factory from producing is to disassemble it with a DAS (dis-assembly) order.
This is explained in Chapter 9, Assembly.
Dis-assembled factory units go into storage.
A combine (COM) order combines two factory groups into one; both groups must be manufacturing the same item.

### 8.3.6 RETOOLING

A FCT group may be changed from building one item to building another, but it must retool first with a BCH, RETL order, with the following exceptions.

* In the case of switching from making an item to making research points, no retool order is needed (switching from research to an item *does* require a retool order.)
