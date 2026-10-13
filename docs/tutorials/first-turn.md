# Your first turn

In this tutorial we will play one turn of Empyrean Challenge: we will read the initial printout, write two orders on the turnsheet, and find out what happened to them on the next printout.
By the end you will have named your home colony and sent a message to the rest of your race.

This tutorial explains the rules; it does not add to them.
Where it and the [manual](../manual.md) differ, the manual is right.

## Before we start

You need the initial printout and the initial turnsheet that came with it ([B2.0](../manual.md#rule-B2.0)).
Our examples use the numbers from the sample turnsheet in [S3.0](../manual.md#rule-S3.0): race 2, player ID 22, and a home colony with s/c ID 22.
Use the numbers from your own printout wherever ours appear.

## Read the initial printout

Open the printout and find three numbers on it: your player ID, your race number, and your home colony's ID ([B2.0](../manual.md#rule-B2.0)).
Write them down; every turnsheet needs them.

Next, find the list of what your colony holds: factory groups, population, weapons, transports, and resources.
Your factories are already working, because every factory group starts with work in process already running ([B2.0](../manual.md#rule-B2.0)).
So your factories keep producing while you learn.

Last, find the free magnitude-10 probe report.
It lists the stars within 10 light years of your home planet and the planet in each orbit of your home system ([A2.3](../manual.md#rule-A2.3)).
Your home planet is at coordinates 0/0/0, and every coordinate on the printout is measured from there.

## Head the turnsheet

At the top of the first page, write the turn number from your printout, the game name and number, your race number, your player ID, your account number, your name, and your signature ([S1.0](../manual.md#rule-S1.0)).
Ours looks like this:

```text
EC #3        PLAYER NAME:  PRINCE JAMES      TURN #0          PAGE 1 of 1
RACE #2      SIGNATURE:                      PLAYER ID #22    ACCT #0353
```

## Name your home colony

Every order starts with the ID of the s/c that carries it out, because orders are addressed to ships and colonies ([S2.0](../manual.md#rule-S2.0)).
We will give our colony a name with a name order, NAM ([S13.1](../manual.md#rule-S13.1)).
Write this line under the heading:

```text
22, NAM, New Hope.
```

That is the colony's ID, the order, and the name, separated by commas, with a period at the end.

## Send a news release

Next we will tell the rest of our race that we are open for trade.
A news release, NSR, goes to every member of your race on their next printout ([P1.1.1](../manual.md#rule-P1.1.1), [S13.4](../manual.md#rule-S13.4)).
Write this line:

```text
22, NSR, New Hope is open for trade. SIGNED.
```

Because it ends with SIGNED, the other players will see your ID, your name, and the s/c number.

## Check the lines

Before sending the turnsheet, check every line against the general rules for orders ([S2.0](../manual.md#rule-S2.0)):

- It starts with the ID of an s/c that belongs to you.
- It uses the abbreviation for every word on the abbreviation list, such as NAM and NSR ([A7.0](../manual.md#rule-A7.0)).
- It is less than 80 characters long, including spaces.
- It ends with a period.

Both of our lines pass.
Print neatly, and leave a blank line after every three or four orders ([S1.0](../manual.md#rule-S1.0)).

## Send the turnsheet

Mail the turnsheet so that it arrives before the date shown on your printout ([B2.0](../manual.md#rule-B2.0)).

The computer works through everyone's orders in stages, finishing each stage before starting the next ([B3.0](../manual.md#rule-B3.0)).
Our NAM order runs in the naming stage ([B3.14.1](../manual.md#rule-B3.14.1)), and our NSR order runs in the news release stage ([B3.21.1](../manual.md#rule-B3.21.1)).

## Read the results

When your next printout arrives, look at the report for colony 22.
It now carries the name New Hope, and our news release appears in the News Service, which every member of the race receives ([P1.1](../manual.md#rule-P1.1)).

If an order failed, it is listed under "Special Messages" with an error code at the end ([R2.0](../manual.md#rule-R2.0)).
For example, E01 means the order was not written in the right format, often because of a misspelling.
Find the code in [R2.0](../manual.md#rule-R2.0), fix the line, and write it again on your next turnsheet.

## What we did

We read the initial printout, headed a turnsheet, wrote and checked two orders, and read their results.
Every turn works the same way: read the printout, write orders, and send the turnsheet back.

From here:

- Subject S of the manual lists every order, grouped by what it does ([S. Orders](../manual.md#s-orders)).
- [B3.0](../manual.md#rule-B3.0) shows the order in which a turn is processed.
- [B5.0](../manual.md#rule-B5.0) explains how the game is won.
- If you are new to games like this one, the rules suggest starting as a Regent, coached by your Ruler ([A1.0](../manual.md#rule-A1.0), [B4.1](../manual.md#rule-B4.1)).
