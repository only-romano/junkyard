## _Misty Island Mine_

#### _Legend says:_
> Learn how your peasants can work together and defend themselves from ogres!

#### _Goals:_
+ _Collect 300 gold_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Return Statements**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](mistyIslandMine.js)**
+ **[Python](misty_island_mine.py)**

#### _Rewards:_
+ 339 xp
+ 161 gems

#### _Victory words:_
+ _IT'S LIKE A SEA OF CLOUDS._

___

### _HINTS_

Command a troupe of peasants to collect their best coin.

Command them to `"buildXY"` a `"decoy"` when an enemy is targeting the peasant:

```javascript
var enemy = peasant.findNearestEnemy();
if (enemy.target == peasant) {
    // ...
}
```

To command a peasant to build, use: `command(peasant, "buildXY", "decoy", x, y)`.
For this level, build your decoys at `peasant.pos.x - 2`, so the decoy will lead the ogres into the arrow towers.

___
