<!-- Page - | source: EC Rules 1980 Even Pages.pdf, p32 -->

### 17.4.48 DISASSEMBLY ORDERS (DAS)

- Format: S/C ID#, DAS, qty, item.
- Example: 100, DAS, 400, MSL-1.
- Example: 100, DAS, 1,000, SPYS.
- Notes: This format is used to either disassemble SPYS or CNW's, or to take items out of use and put them into storage.

- Format: S/C ID#, DAS, qty, "FCT"-TL#, FCT group #.
- Example: 99, DAS, 10,000, FCT-3, 5.
- Notes: This format takes FCT's from an existing FCT group and puts them into storage.
  In this case, 10,000 FCT-3 are taken from FCT group #5 and put into storage.

- Format: S/C ID#, DAS, qty, "MIN"-TL#, *group #*.
- Example: 37, das, 25,000, MIN-2, 8.
- Notes; This format takes MIN's out of an existing MIN *group* and puts them into storage.
  Please use the group #, not the deposit location.

#### 17.4.48.1 Multiple DAS Orders

- Format: S/C ID#, DAS, qty of unit types, "M".
- Example:
  ```text
  75, DAS, 4, M.
  30, SPYS.
  4E9, CNW-3.
  1,000, MSL-2.
  50,000, FCT-4,7.
  3,000, MIN-6, 4.
  ```

\* All orders above were additional.
This page revised 5/9/81.
