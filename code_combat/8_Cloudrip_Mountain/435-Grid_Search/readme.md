## _Grid Search_

#### _Legend says:_
> Don't know exact coordinates? Search all the possible points!

#### _Goals:_
+ _Find the Treasure_

#### _Topics:_
+ **Basic Syntax**
+ **Strings**
+ **Variables**
+ **For Loops**
+ **Nested For Loops**
+ **Boolean Greater/Less**

#### _Solutions:_
+ **[JavaScript](gridSearch.js)**
+ **[Python](grid_search.py)**

#### _Rewards:_
+ 259 xp
+ 119 gems

#### _Victory words:_
+ _THERE'S GOLD IN THEM THERE HILLS!_

___

### _HINTS_

It was written in an old treasure map:

"Between four trees, between four rocks. The treasure is at the point `?0, ?0.`"

But the numbers are unreadable!

`?0` could mean 10, 20, 30... or more!

We found the trees and the rocks, so you need just look over each of the possible points.

Navigate across the field to find the treasure. You have 2 peasants at your disposal. Command them using `hero.say` to dig up at your location.

Note how the nested `for`-loops map out the locations you should explore!

```javascript
var startX = 20;
var endX = 110;
var startY = 30;
var endY = 90;

for (var x = startX; x < endX; x += 10) {
    for (var y = startY; y < endY; y += 10) {
        hero.moveXY(x, y);
        // The hero will move to each tile in a 100x100 square:
        // 10, 10 -> 90, 10
        //   |   ...   |
        //   V   ...   V
        // 90, 10 -> 90, 90
    }
}
```

___
