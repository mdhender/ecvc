<!-- Page 6.1 | source: EC Rules 1980 Odd Pages.pdf, p8 -->

# 6. BASIC NEEDS (FOOD, CONSUMER GOODS, LIFE SUPPORT)

## 6.1 FOOD

### 6.1.1 CONSUMPTION

Each population unit (POP) automatically consumes one quarter of a food unit (FOOD) per turn, unless the Ruler rations the s/c.
If the rationed amount of food is less than 1/16 of a food unit per POP per turn, the computer will divide the food equally, and check for starvation, according to the Starvation Rule below.
Ration orders can not be more than 100% (1/4 food unit per POP), or less than 25% (1/16 food unit per POP)

#### 6.1.1.1 Starvation Rule

    (M-R) ÷ M = S

Where S is the fraction of the population of the s/c that starves, M is the minimum amount of food units that can be allotted without starvation, (or 1/16 of a food unit), and R is the rationed amount of food per POP (when less than M).

##### 6.1.1.1.1 Example

Due to a food shortage, the computer rations each POP to 1/20 of a food unit, (20%).

```text
(1/16 - 1/20) ÷ 1/16 = S
(5/80 - 4/80) ÷ 5/80 = S
16/80 = 1/5 of the population starved.
```

Note: 30% OF THE STARVING POP DIE EACH **TURN**.
(Fractions rounded up).

### 6.1.2 RATION PERCENTAGE

The percentage of a ration (RTN) order is the percentage of the normal 1/4 food unit per population unit.

## 6.2 CONSUMER GOODS

### 6.2.1 CONSUMPTION

All population types (except unemployables) are paid in consumer goods (CNGD).
Unemployables are paid nothing.

All PAY orders are standing orders; they remain the same until changed by the player.
At the start of the game, all unskilled (USK) units are paid 0.125 CNGD per turn; soldiers (SLD) are paid 0.25 CNGD per turn; and professionals (PRO) are paid 0.375 per turn.
Construction workers (CNW) are paid the USK rate plus the PRO rate.
Spies (SPYS) are paid the PRO pay rate plus the SLD pay rate.
Trainees are paid at the USK rate.
To change the pay rate, the player writes a PAY order.

### 6.2.2 BACK PAY

If a s/c does not have enough CNGD to pay its people, then the computer adds the unpaid amount to a record the computer keeps which is shown on each printout, called the Back Pay Amount.
Back pay has the effect of increasing rebels.
The larger the amount of back pay in proportion to the population, the greater the increase in rebels.
The effect of back pay on ships is only one tenth the effect in colonies.
Back pay is decreased when the s/c has more CNGD than it needs to meet its payroll.
