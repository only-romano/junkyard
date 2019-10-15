## _Grid Minefield_

#### _Legend says:_
> The grid minefield is the same as a carpet bombing, just more surprising.

#### _Goals:_
+ _Defeat the ogres_
+ _Peasants must survive_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Nested For Loops**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](gridMinefield.js)**
+ **[Python](grid_minefield.py)**

#### _Rewards:_
+ 259 xp
+ 119 gems

#### _Victory words:_
+ _PERFECT TIMING, PERFECT EXECUTION._

___

### _HINTS_

An ogre formation is marching towards the village. We much prepare the meeting for our guests. We'll use their strict formation against them!

If we place mines between the ogre's lines and blow them all at once, the ogres will go flying.

Use nested loops to build the grid minefield, but, increment by numbers higher than one and use those as coordinates to place mines!

These mines won't explode unless a human steps on them, so don't be afraid and take a step!

It is possible to use `for`-loops to map out not just 1-dimensional positions!

Nested `for-loop`s will cover each individual square, great for building an impenetrable minefield!

```javascript
for (var x = 10; x < 100; x += 10) {
    for (var y = 10; y < 100; y += 10) {
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
