<!-- Page - | source: EC Rules 1980 Back Cover.pdf, p1 -->

# PRINT OUT INTERPRETATION

Most of the printout is in easy to understand terms, with the exceptions of the abbreviations listed in the Glossary, the error messages, orbit probes, and the three headings shown below.

1. Space Available is the number of additional volume units a s/c can hold.
2. Transport Not Used is the total unused carrying capacity of all of the TPT's in the s/c measured in mass units.
3. Standard of Living is the total CNGD's paid divided by the total population and multiplied by 4 (which makes the rate annual).
4. *Orbit Probes:*

```text
                                                          tactical
Format:   S/C type  S/C name (S/C ID#)  mass=log base 10  coordinates
Example:  SHP       VEGA-5   (356)      M=6               9/-28/13
          OPC       BADSHOT  (28)       M=8               0/0/0
```

# ERROR MESSAGES

An error message is the error code at the end of an order that failed.
The failed orders are separated into two headings on the printout.
Most orders that fail are shown under the heading "Special Messages".
Each s/c a player has gets its own report on the printout.
Special Messages are messages from that particular s/c to the player.
Since most orders are for a s/c owned by the player, most orders that fail would be shown under Special Messages.
Some orders are for a foreign s/c, like SPM orders.
These orders that fail show up under the heading, "Player's Special Messages".
The error code at the end of a failed order explains why the order failed.

- E01: Format error.
  This error also includes mis-spellings and undefined errors.
- E02: Quantity error.
  E02 may mean lack of fuel for TPT's involved, but in most cases refers to the quantity of the object of the order.
- E03: The player does not own the s/c or planet necessary.
- E04: The s/c does not exist.
- E05: E5 error codes have been discontinued.
- E06: The deposit is already being mined.
- E07: The FCT or MIN group does not exist.
- E08: The player already has 40 MIN groups, and can not have more.
- E09: The FCT group cannot make the new item until the FCT's are retooled.
- E10: There is no market at location of the s/c.
- E11: There is not enough space available in the s/c to complete the order.
- E12: The player already has 25 FCT groups, and can not have more.
- E13: The s/c was at the wrong orbit.
- E14: No REC, AAN, or APU order was given.
- E15: Insufficient TPT capacity or CNW's.
- E16: Permission to colonize was not granted.
- E17: A REC, AAN, or APU order was written, but for a lesser amount.
- E18: The planet is already controlled.
- E19: There is no planet in that orbit.
