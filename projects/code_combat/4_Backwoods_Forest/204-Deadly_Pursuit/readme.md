## _Deadly Pursuit_

#### _Legend says:_
> This level exercises: if/else statements, flag placement, timing and item collection.

#### _Goals:_
+ _Use traps to destroy all the ogres_
+ _Collect all the coins_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Nested If Statements**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](deadly.js)**
+ **[Python](deadly.py)**

#### _Rewards:_
+ 80 xp
+ 86 gems

#### _Victory words:_
+ _WAY TO COVER YOUR TRACKS!_

___

### _HINTS_

Use your `pickUpFlag` method to go to and pick up flags that you place–but first, use `buildXY` to build a `"fire-trap"` where the flag is. Just keep collecting coins until you see some ogres coming, then go back and build a trap on the X to stop them.

Don't build a trap on every X, or you won't have time to collect all the coins. You have to defeat the ogres, so fences won't work. You'll have to react quickly to place the flag in time to stop them!

If you're having trouble with the code, check out what you did in Drop the Flag. Remember that each flag and item object has a `pos` property, which has `x` and `y` properties that you can use with `moveXY` and `buildXY`.

_**Tip**: remember that you need to press Submit before you can place flags. The ogres are randomized, so they'll come from different paths each time._

___
