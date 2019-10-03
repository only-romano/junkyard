## _Yakstraction_

#### _Legend says:_
> Thirsty yaks are stampeding towards a vulnerable peasant sunning herself at an oasis, but you've got decoys to distract the yaks out of the way.

#### _Goals:_
+ _Save Brandy with decoys!_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **If/Else Statements**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](yakstraction.js)**
+ **[Python](yakstraction.py)**

#### _Rewards:_
+ 213 xp
+ 174 gems

#### _Victory words:_
+ _NOW BRANDY HAS THE POOL TO HERSELF._

___

### _HINTS_

Combine flags, `hero.gold`, and `"decoy"`s to protect the peasant!

Inside your loop, first thing to do is use `findFlag` to check if there are any flags placed.

If there is a flag, **and** if you have `25` gold or more, then use `buildXY` to build a decoy at the flag's `pos.x` and `pos.y`. Don't forget to `pickUpFlag` while you're there!

_**Tip**: Check for flags first so you won't delay building your decoy while you move to another coin._

Next, use `findNearestItem` to find a coin, and move to it.

___
