## _Sleepwalkers_

#### _Legend says:_
> Even yetis can be sleepwalkers. Don't wake up them. Seriously.

#### _Goals:_
+ _Humans must survive_
+ _Peasants must get in the village_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Return Statements**
+ **Array Length**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](sleepwalkers.js)**
+ **[Python](sleepwalkers.py)**

#### _Rewards:_
+ 259 xp
+ 119 gems

#### _Victory words:_
+ _"NEVER WAKE UP ANYTHING SLEEPING" IS A GOOD LIFE MOTTO._

___

### _HINTS_

This village is an anomaly. There are too many sleepwalkers and they often walk out the village. But it's only half of the problem. There are sleepwalking yetis and they are following our returning peasants.

We must build a fence system to pass sleeping peasants and turn round yetis. Don't use combat methods which can wake up yetis. Yetis are angry when somebody wakes them up.

Senick is an experienced hunter and he knows everything about yetis. He can calculate and predict their routes. Senick prepared the grid map of the fence system. You should use that scheme and build fences where it's required.

The map is represented as 2d-array (an array of arrays) with numbers (1 or 0). 0 is an empty cell, 1 is a place where to build a fence.

___

The grid map is an array of arrays where each element can be 1 or 0. 0 is an empty cell, 1 is a place where to build a fence.

In previous levels you've learnt how to loop through 2d-arrays and get their element values. Use nested loops and `array[i][j]` syntax to read all values and if you meet 1, then build a fence there. There is a prepared function `convertCoor` to convert grid coordinates (row and column) to (x, y) coordinates.

```javascript
// 2-nd row, 3-rd column
convertCoor(2, 4);  // result: {x: 42, y: 38}
```

Don't forget in the village when fences are built, because yetis can smell the hero.

___
