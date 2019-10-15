## _Cloudrip Commander_

#### _Legend says:_
> Use your new Boss Star to summon and command troops!

#### _Goals:_
+ _Get everyone to the base_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops with Conditionals**
+ **Iterating Over Arrays**
+ **Accessing Properties**
+ **Object Literals**

#### _Solutions:_
+ **[JavaScript](cloudripCommander.js)**
+ **[Python](cloudrip_commander.py)**

#### _Rewards:_
+ 363 xp
+ 174 gems

#### _Victory words:_
+ _IT'S ABOUT TIME THOSE BRAINLESS SOLDIERS STARTED LISTENING TO YOU._

___

### _HINTS_

![](img/cloudrip_commander.png)

In this level you have access to the Boss Star I. You can now `summon` `"soldier"` and `"archer"` allies.

You can now also `command` your `soldier` and `archer` allies.

___

This level introduces the **Boss Star**, an item that allows you to summon and command allies.

The **Boss Star I** lets you summon `"soldier"` allies and command `"soldier"` and `"archer"` allies.

The sample code first demonstrates how to use the `costOf` and `summon` methods to summon `"soldier"` allies if you have enough gold to do so.

Then, it uses `findFriends` to get an array of your allies, and shows how to command an ally to `"move"` with the `command` method.

You need to take this `command` code and put it inside a `while` loop, so you give commands to all the soldiers, instead of just one.

Then, use another `while` loop with `move` to move your hero to the X mark.

___
