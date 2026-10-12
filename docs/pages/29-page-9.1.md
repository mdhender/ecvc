<!-- Page 9.1 | source: EC Rules 1980 Odd Pages.pdf, p15 -->

# 9. ASSEMBLY

## 9.1 ASSEMBLY AND DISASSEMBLY

Assembly (ASM) orders are used in two ways: to assemble special purpose population groups (CNW's and SPYS), and to assemble unassembled items.

### 9.1.1 ASSEMBLING SPECIAL PURPOSE POPULATION GROUPS

When an ASM order is given for a spy unit, one PRO unit and one SLD unit are taken from their POP segments and joined to form one group spy unit.
When an ASM order is given for a CNW unit, one PRO unit and one USK unit are taken from their population segments and formed into one construction worker unit.

### 9.1.2 ASSEMBLING UNASSEMBLED ITEMS

Unassembled items are "assembly type" items that have been just manufactured or disassembled.
Assembly type items work only when they have been assembled with an ASM (assembly) order; they are called assembled items when assembled.
When they have been disassembled with a DAS (dis-assembly) order, the items do not function, and they are then called unassembled items.
*Unassembled items go into storage automatically*.
The following items are assembly type items: AUT, ESH, EWP, FCT, FRM, HEN, LFS, LTSU, MIN, MSL, SEN, SPD, STUN, and SLSU.
An ASM order takes an unassembled item from storage, assembles it, and makes it work.

### 9.1.3 DISASSEMBLING ASSEMBLED ITEMS

Dis-assembly (DAS) orders are used to reverse assembly orders.
That is, they disassemble items and put them into storage, and are also used to break up SPYS and CNW's.
Note: only group G SPYS can be DAS'd.
Dis-assembly of non-population units causes a 10% *LOSS*.
For instance, if 5,000 EWP-2 are dis-assembled then 500 will be lost and 4,500 will appear in storage under "un-assembled items" in the storage section of the printout.
There is no loss in disassembling population units.
When determining the 10% loss, fractions are rounded down.

### 9.1.4 NON-ASSEMBLY ITEMS

Along with unassembled items (UNA), non-assembly items (NON) are also kept in storage.
NON, however, perform their functions without being assembled.
NON can not be assembled or dis-assembled.
The following items are NON: TPT, MSS, METS, NMTS, FUEL, FOOD, ASW, ASC, ANM, CNGD, MRB, MTSP.
NON are taken by the computer from storage automatically as used per turn.

### 9.1.5 USE OF CONSTRUCTION WORKERS

Dis-assembly requires 1 CNW per 500 mass units being dis-assembled.
Assembly requires 1 CNW per 500 mass units being assembled per turn.
If a s/c has 5,000 EWP-2 in storage, it would require 200 CNW ((20 x 5000) ÷ 500) to ASM them.

### 9.1.6 REGENTS

A Regent is allowed to ASM spies, but not to issue spy movement (SPM) orders.
All spies assembled by a Regent will be under the control of his Ruler.
