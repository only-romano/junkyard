## _Bits And Trits_

#### _Legend says:_
> Defend yourself with an enchanted robot!

#### _Goals:_
+ _Defeat the ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **While Loops with Conditionals**
+ **Return Statements**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](bitsTrits.js)**
+ **[Python](bits_trits.py)**

#### _Rewards:_
+ 387 xp
+ 178 gems

#### _Victory words:_
+ _G00D J08!_

___

### _HINTS_

Brawlers incoming!

Command the robot by converting base-10 numbers to base-2 and base-3!

You will need to convert our normal decimal number system into something this robot can understand!

We use the decimal system, where _dec_ means 10, like a decade (10 years). There are other number systems out there such as the binary (bicentennial, or 200 years) and trinary system: _bi_ means 2, _tri_ means 3.

We call each number system as a _base_, so _base 10_ means decimal, while _base 2_ means binary.

Observe the various ways to write the number 9 in various bases:

```
Base 10: 9
Base  9: 10
Base  8: 11
Base  7: 12
Base  6: 13
Base  5: 14
Base  4: 21
Base  3: 100
Base  2: 1001
```

The method we use to convert a number to another base is to divide by the desired base and observe the remainder:

```
Convert 9 base 10 to base 3
  9 / 3 = 3, with 0 remainder
 3 / 3 = 1, with 0 remainder
1 / 3 = 0, with 1 remainder
Notice that the remainders equal to 100!

Convert 9 base 10 to base 2
   9 / 2 = 4, with 1 remainder
  4 / 2 = 2, with 0 remainder
 2 / 2 = 1, with 0 remainder
1 / 2 = 0, with 1 remainder
Again, 1001 is the same as the provided answer above!
```

But how can you trust the numbers provided above are the actual binary and trinary representations of 9?

How to count in a base number system:
+ In the binary system there are only 2 digits: (0, 1)
+ In the trinary system there are only 3 digits: (0, 1, 2)
+ In the decimal system there are 10 digits: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
+ In the hexadecimal system there are 16 digitS: (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, a, b, c, d, e, f) Yes! Letters, too!

Now to count in binary, remeber you cannot ever reach the digit 2!

```
Base 10     Base 2
      0          0
      1          1
      2         10
      3         11
      4        100
      5        101
      6        110
      7        111
      8       1000
      9       1001
     10       1010
     11       1011
     12       1100
```

See? It matches! Now command the robot with this knowledge.

___
