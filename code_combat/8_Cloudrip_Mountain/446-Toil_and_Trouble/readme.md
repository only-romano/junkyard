## _Toil and Trouble_

#### _Legend says:_
> Ogre witches: double the trouble.

#### _Goals:_
+ _Defeat the ogres_
+ _At least one ally must survive_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Return Statements**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](toilAndTrouble.js)**
+ **[Python](toil_and_trouble.py)**

#### _Rewards:_
+ 387 xp
+ 178 gems

#### _Victory words:_
+ _SHE TURNED ME INTO A NEWT!_

___

### _HINTS_

Soldiers and archers should target different units to complete this level.
+ `"soldier"`s should attack the `"witch"`.
+ `"archer"`s should attack their nearest enemy.

The `findByType` method allows you to find all (visible) enemies or items by their type. Combine it with `findNearest` and you can find the nearest unit/item by its type.

```javascript
var gems = hero.findByType("gem");
var nearestGem = hero.findNearest(gems);
var nearestThrower = hero.findNearest(hero.findByType("thrower");
```

___

Define a `chooseTarget` function that accepts an argument called `friend`.

Find the `nearest` enemy to the friend, as well as the nearest enemy with type `"witch"` _(use **findByType**)_

Your soldiers should target witches first, or if there are no witches, then the nearest enemy. Other units should always target the nearest enemy.

_**Hint**: Each soldier should attack the `"witch"` nearest to that soldier. This will split your soldiers into two groups, and they won't get injured by the splash damage done by the witches' attacks._

___
