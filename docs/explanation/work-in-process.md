# About work in process

Factories in Empyrean Challenge do not turn raw materials into finished goods on the turn they are ordered.
Everything a factory group builds spends at least four turns as work in process (WIP) before it reaches the s/c's inventory ([H3.0](../manual.md#rule-H3.0), [H3.4](../manual.md#rule-H3.4)).
This page explains how that pipeline behaves and why so many of the factory rules follow from it.

The pipeline described here is how manufacturing looks from the outside.
It is not a requirement for how the game engine works inside, or for how the printout reports WIP.

This page explains the proposed manufacturing pipeline - it's not authoritative.
Where it and the [manual](../manual.md) differ, the manual is right.
The proposal is logged in [errata 91](../errata.md#91-the-production-pipeline), [92](../errata.md#92-group-numbers-are-reused), and [93](../errata.md#93-research-laboratories).

## A year in four turns

A turn is a quarter of a game year ([A5.0](../manual.md#rule-A5.0)), and no item can be built in less than a year ([H3.0](../manual.md#rule-H3.0)).
WIP is how the game squares a quarterly turn with a yearly build time.

The capacity rule is stated by the year.
One FCT converts 20 MU times its TL of metallics and non-metallics each year into units of the same total mass ([H3.3](../manual.md#rule-H3.3)).
Factories build everything except population, food, and resources ([H3.0](../manual.md#rule-H3.0)).
Mass is conserved: the unit characteristics give each item's mass as the sum of its METS and NMTS ([R3.0](../manual.md#rule-R3.0)).
A load is split between METS and NMTS in the proportions of the item's inputs.
So a FCT-1 building LFS-2, at 6 METS and 10 NMTS each, takes 20 MU in that same proportion, 7.5 METS and 12.5 NMTS, and turns it into 1.25 LFS-2 a year.
Small groups pay more than this for the same load ([Why small groups cost more](#why-small-groups-cost-more)).

## Each FCT carries its own load

The pipeline belongs to the individual FCT, not to the group.
A FCT takes on a load of 20 times its TL in MU, carries it through four steps, and only then takes on another.
Four rules shape that journey.

1. The pipeline takes at least four turns of work to complete.
2. The pipeline does not start until the FCT has the required MU of metallics and non-metallics at the beginning of a turn.
3. Once a FCT claims its metallics and non-metallics, it holds them until the pipeline is complete.
4. The pipeline does not advance unless the FCT has the fuel and labor it needs at the beginning of a turn.

The steps are numbered WIP-0 to WIP-4.
WIP-0 is a load that has been claimed but not yet worked; WIP-1, WIP-2, and WIP-3 are a quarter, a half, and three quarters complete; WIP-4 is finished.
The printout's three WIP columns, 1/4, 1/2, and 3/4 complete, are WIP-1, WIP-2, and WIP-3.

## A turn in the factory

Manufacturing happens in the production stage, after farms and mines and before people are paid ([B3.17](../manual.md#rule-B3.17)).
Every order has been processed by then, including the ASM orders of the assembly stage ([B3.8](../manual.md#rule-B3.8)), so a group assembled this turn claims its first loads this turn.
It runs in four stages.

### Resources

First, metallics and non-metallics are handed out.
Factory groups are served in order of seniority, the first created first, which is the order of their group numbers.
Within a group, only FCT that are idle and hold no load are served, from the highest TL down.
A FCT that can not be given its full load, and the waste that goes with it, is skipped, and the distribution moves on to the next.

A group's WIP capacity is the total of its FCT's loads, 20 MU times the TL for each FCT.
The loads its FCT carry and its stockpile of WIP-4 share that capacity.
A FCT claims a load only if the whole load fits in what is left of that capacity.

The metallics and non-metallics a FCT claims leave inventory.
The load becomes its WIP-0, and the waste is lost.
The load keeps the mass and volume of the resources it was made from, so starting work neither frees nor uses enclosure.

### Staff and power

Next, the groups are staffed and powered, in the same order.
Staff is labor: PRO, and USK, AUT, or both ([H3.1](../manual.md#rule-H3.1), [H3.10](../manual.md#rule-H3.10)).
Power is fuel.

Labor is allocated to a group before fuel.
Each FCT needs one PRO and three USK, each times the group's labor efficiency factor ([H3.1](../manual.md#rule-H3.1)), and that is what the group needs to run at 100%; when there is less, the group runs at the share it can staff.
The group then claims fuel for every FCT that holds WIP and is staffed.
A FCT with no load claims none.

When staff or fuel is short, each goes in the same order: by group seniority, then by TL, and then to the most advanced work first, WIP-3, then WIP-2, WIP-1, and WIP-0.
Every FCT that ends this stage with a load, staff, and power works.

Staff is not assigned to a group for good.
It is drawn from the s/c's pool of USK and AUT each turn and returned at the end of the turn, not at the end of manufacturing.

A FCT that lacks a load, staff, or power is idle for the rest of the turn.

### Processing

Every FCT that is not idle advances its load one step: WIP-0 becomes WIP-1, WIP-1 becomes WIP-2, WIP-2 becomes WIP-3, and WIP-3 becomes WIP-4.
A WIP-4 load passes at once from the FCT to its group's stockpile, and the FCT is free to claim a new load on the next turn.
Since the load already counted against the group's capacity, the stockpile always has room for it.
A group's loads and stockpile together never exceed its capacity, so no FCT is ever left holding WIP-3 it can not pass on.

### Output

Last, the group converts its stockpile of WIP-4 into as many of its target units as it can.
It converts no more than the s/c has room for: a conversion that would exceed the s/c's enclosure capacity ([F3.2.3](../manual.md#rule-F3.2.3)) is not made, and the WIP-4 is held.
Whatever WIP-4 is left over stays in the group's stockpile for a later turn.
The units made are added to the s/c's inventory.

## Following a group through the year

Take a group of 50,000 FCT-1 building LFS-2, with resources, staff, and power to spare.
On its first turn of work every FCT claims 20 MU, and the group holds 1,000,000 MU of work.

| TURN OF WORK | WIP-1 (1/4)  | WIP-2 (1/2)  | WIP-3 (3/4)  | OUTPUT       |
|--------------|--------------|--------------|--------------|--------------|
| 1            | 1,000,000 MU |      0       |      0       |      0       |
| 2            |      0       | 1,000,000 MU |      0       |      0       |
| 3            |      0       |      0       | 1,000,000 MU |      0       |
| 4            |      0       |      0       |      0       | 62,500 LFS-2 |

On the fourth turn the loads reach WIP-4, the group turns 1,000,000 MU into 62,500 LFS-2, and every FCT is empty again.
On the fifth turn they all claim new loads and the cycle repeats.
This is the pattern in the first example in [H3.4](../manual.md#rule-H3.4): the group does not finish a quarter of its year's output each turn, but takes it all a quarter of the way at a time.

A group whose FCT all start together delivers in a lump every fourth turn.
Its output is steady only when its FCT are spread across the steps.
That happens when FCT are added to the group on different turns, as in the second example in [H3.4](../manual.md#rule-H3.4), and it also happens when resources are short: the FCT that are skipped one turn start on a later one, and from then on they finish on a different turn from the rest.

## Why the load is claimed up front

Claiming a whole load before starting, and holding it, means a FCT never starts work it can not finish for want of materials.
A shortage of metallics or non-metallics delays new work; it never strands work already under way.

Fuel and labor are different, because they are needed every turn.
When staff or fuel runs short, sending it to the most advanced work first means the loads closest to finishing are the last to stop.

The cost of this is that a FCT's materials are tied up for the whole year.
WIP is not directly accessible to the player: it can not be traded, transferred, or used by another group.
The only way to get the materials back is to disassemble the FCT, which junks its WIP ([Losing FCT](#losing-fct)).

## Stalls

A FCT that holds WIP but has not been assigned staff and power for the turn is stalled.
A stall loses nothing.
The FCT keeps its WIP exactly as it is and waits for staff and power to return, then carries on from the same step.
Stalls are why the pipeline takes at least four turns of work rather than exactly four turns.

A stall costs time, not materials.
Because the load was claimed up front, a FCT that stalls at WIP-2 needs nothing more than staff and power to finish; it never has to find its metallics and non-metallics again.

## When the s/c is full

A full s/c backs the pipeline up from the far end.
The group stops converting WIP-4 it has no room to store, so the WIP-4 builds up in the stockpile.
The stockpile shares the group's capacity with the loads, so every MU it holds is an MU no FCT can claim.
Work already under way carries on and finishes into the stockpile, but empty FCT take on new loads only while there is room for them.
Once the stockpile fills the group's capacity, no FCT can claim a load until the s/c has room for the group's output again.

Take a group of 4 FCT-1, with a WIP capacity of 80 MU, in a s/c with no room for its output.
FCT A begins the turn empty, B, C, and D hold WIP-3, and the stockpile holds 10 MU of WIP-4.
The group holds 70 MU, so only 10 MU of its capacity is left, and A's load of 20 MU does not fit; A stays empty.
B, C, and D finish, and the stockpile grows to 70 MU.
On the next turn only 10 MU is left again, so none of the four can claim a load, and the group stands idle until the s/c has room.

An idle FCT with no load claims no fuel, so a group stopped by a full s/c uses no power.
The load keeps the volume of its inputs, so WIP takes the same room in the s/c at every step.
The space a full s/c lacks is the room for the finished units.

## Why the group keeps a stockpile

A FCT's load is measured in mass, not in units, and the two rarely line up.
A FCT-1 makes 20 MU a year; a SEN-1 has a mass of 3,000 MU.
No single FCT-1 could ever finish a sensor.

Pooling finished loads at the group solves that.
The group makes whole units from the stockpile, and a fraction of a unit waits for the next turn's loads.
For the same reason, the group as a whole sets the output, and every FCT in a group builds the same item ([H3.0](../manual.md#rule-H3.0)).

The stockpile is also the buffer between the factory and storage.
It lets work under way finish when the s/c is full, and its share of the group's capacity is what stops new work.

## Why small groups cost more

Small factory groups are less efficient than large ones ([H3.2](../manual.md#rule-H3.2)).
The proposed rules split the efficiency factor in two, one for labor and one for materials, both set by the number of FCT in the group.

| Number of FCT's in Group | Efficiency Factor (Labor) | Efficiency Factor (Materials) |
|--------------------------|---------------------------|-------------------------------|
|       1 ... 4            | 6                         | 3.00                          |
|       5 ... 49           | 5                         | 2.50                          |
|      50 ... 499          | 4                         | 2.00                          |
|     500 ... 4,999        | 3                         | 1.75                          |
|   5,000 ... 49,999       | 2                         | 1.50                          |
|  50,000 ... 199,999      | 1                         | 1.25                          |
| 200,000 ... infinity     | 0.5                       | 1.00                          |

The labor factor multiplies the PRO and USK each FCT needs.
The materials factor multiplies the METS and NMTS a FCT must claim for its load.
Only the load itself goes into WIP; the rest is waste, removed from inventory when the load is claimed.

An item that takes 3 METS and 1 NMTS costs a group of 4 FCT, with a materials factor of 3, 9 METS and 3 NMTS a unit.
The extra 6 METS and 2 NMTS are waste.
A group of 200,000 FCT or more pays exactly the item's inputs and wastes nothing.

The materials factor is never below 1, so mass is never created: the units made weigh what the load weighs, and a small group pays for its smallness in waste.

## Losing FCT

DAS orders are processed in the dis-assembly stage, before production ([B3.4.1](../manual.md#rule-B3.4.1)).
A disassembled FCT can not take its WIP into storage, so its WIP is junked: converted back to metallics and non-metallics in the item's proportions, with 90% of them returned to inventory ([errata 25](../errata.md#25-losses-when-junking)).
Removing FCT also lowers the group's WIP capacity, and both its capacity and the room left in it are worked out again.
The FCT that remain keep their loads, which still fit, since each load is exactly its FCT's share of the capacity.
Any WIP-4 that would take the loads and stockpile together above the new capacity is excess, and it is junked too.
That keeps the group within its capacity, so its remaining FCT can always pass their WIP-3 on.
Most of the materials come back, but the work done on them does not, and nor does the waste paid when the load was claimed.
This is the only way a player can recover materials held as WIP, and the only way to trade the FCT that held them.

FCT destroyed in combat are treated the same way.
Combat comes first in the turn ([B3.1](../manual.md#rule-B3.1)), so the destroyed FCT's WIP and any excess WIP-4 are junked, and the group's capacity worked out again, before it manufactures.

## Combining groups

FCT own their WIP, so a COM order ([S8.2](../manual.md#rule-S8.2)) leaves every load from WIP-0 to WIP-3 where it is: each FCT brings its load into the combined group.
The combined group owns both groups' stockpiles of WIP-4.
COM orders are processed in the dis-assembly stage, before production ([B3.4.6](../manual.md#rule-B3.4.6)), so the stockpiles combined are those left at the end of the previous turn's manufacturing.

## Why retooling waits

The retooling rules in [H3.6](../manual.md#rule-H3.6) follow from the same picture.
A FCT that holds a load does not retool, even though the BCH, RETL order is accepted; it retools itself once its load is finished.

The formula for how many FCT retool on a turn is the pipeline written as arithmetic.
Take the mass of everything in WIP as if it were complete and divide by 20 times the FCT's TL.
Since each FCT carries a load of 20 MU times its TL, the quotient is the number of FCT that still hold one.
Subtract it from the size of the group, and what is left is the FCT that are free to retool.

## Research

Factories do not build research in the proposed rules.
RSCH has no mass ([R3.0](../manual.md#rule-R3.0)) and needs no metallics or non-metallics ([J4.1](../manual.md#rule-J4.1)), so it would never fill a load or pass through the pipeline.
Instead, laboratory (LAB) units, assembled into laboratory groups, build it.

A LAB has the same mass, volume, and other characteristics as a FCT of the same TL.
Each LAB produces 0.25 times its TL in RSCH for each turn it is allocated labor and fuel; a turn without them is simply a turn without research, with no WIP to stall or hold.
Laboratories produce just after factories in the turn, and their labor and fuel are allocated the same way: senior groups first, and within a group from the highest TL down.

Moving research out of the factories takes it out of the pipeline's rules altogether.
A FCT is never switched to or from research, so it never has to finish its WIP before research or retool after it.

## Farms and mines

Farms and mines are the other production units, and neither has a pipeline.
A FRM produces food and a MIN extracts ORE on the turn they work, with nothing held over: 25 food per FRM-1 or 5 times the TL for higher farms ([H1.1](../manual.md#rule-H1.1)), and 25 times the TL in ORE per MIN ([H2.1](../manual.md#rule-H2.1)).
Their output is stated per turn, where a factory's is stated per year, and it needs no materials, so there is no load to claim and nothing to carry.

They draw on the same staff and power as factories.
Each FRM and MIN needs one PRO and three USK ([H1.4](../manual.md#rule-H1.4), [H2.3](../manual.md#rule-H2.3)), AUT can stand in for the USK ([H3.10](../manual.md#rule-H3.10)), and both use fuel ([H1.5](../manual.md#rule-H1.5), [H2.3](../manual.md#rule-H2.3)).
Because they come first in the production stage, farms, then mines, then factories ([B3.17](../manual.md#rule-B3.17)), farms and mines have first claim on the s/c's labor and fuel.
Staff returns to the pool only at the end of the turn, not at the end of farming or mining, so a worker on a farm is not free to work in a mine or a factory later in the same turn.
A shortage falls on the factories before it falls on food or ore.

Within farming and within mining, labor and fuel are allocated in the factory order: senior groups first, and within a group from the highest TL down.

The order also links them to the pipeline.
Mines produce before factories, so METS and NMTS mined on a turn are in inventory when the factories hand out loads that same turn.

Without WIP, a shortage of labor or fuel costs a farm or mine only that turn's output ([H1.2](../manual.md#rule-H1.2), [H2.2](../manual.md#rule-H2.2)).
There is no work to stall, and the next turn starts afresh.
Some of the units can produce while the rest stand idle; the ones that produce are those reached first in that order.

A lack of room is handled at the source rather than by a stockpile.
Food that does not fit is thrown out ([H1.2](../manual.md#rule-H1.2)).
Mines extract only the ORE whose refined gold or fuel will fit, while METS and NMTS are stored outside the colony walls and never run short of room ([H2.2](../manual.md#rule-H2.2)).
A factory, by contrast, holds its finished work in its stockpile and stops taking new loads.

## Why seniority matters

Every allocation in production, of resources, staff, and fuel, serves the oldest group first.
Seniority is group number: a new group always gets a higher number than any before it, and a number is never reused, so the lowest number is always the oldest group.
In a shortage the newest groups go without, and a player can not renumber or reorder the groups.
The tool the manual offers is to shut down the less necessary groups with BCH, SHT ([H3.9](../manual.md#rule-H3.9)), which takes them out of the queue and leaves more for the rest.
