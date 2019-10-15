## _Golden Choice_

#### _Legend says:_
> You have only one direction, but you always have a choice.

#### _Goals:_
+ _Collect maximum possible gold_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Return Statements**
+ **Object Literals**
+ **Accessing Properties**
+ **Assigning Properties**

#### _Solutions:_
+ **[JavaScript](goldenChoice.js)** _TO DO_
+ **[Python](golden_choice.py)**

#### _Rewards:_
+ 3070 xp
+ 930 gems

#### _Victory words:_
+ _THAT CHOICE WAS AU-RIGHT!_

___

### _HINTS_

The gate keeper will tell you how much gold you need to collect.

Move in the direction of the exit.

After each coin choose one of the two (or one for edges) nearest coins in the next row.

Don't stop and move exactly to the next coin. One wrong step and deadly beams will burn you.

The algorithm required to beat this level is advanced! Be prepared to work for your victory.
1. Iterate across an entire row of coins and store their values
2. Check the next row, and sum each initial value with each neighbor.
3. Repeat until the last row.
4. Check which path has the highest value.
5. Navigate that path!

___
