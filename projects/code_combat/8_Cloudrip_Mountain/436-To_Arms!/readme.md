## _To Arms!_

#### _Legend says:_
> Ogres are coming! Wake up everyone! To arms, soldiers!

#### _Goals:_
+ _Defeat the ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **For Loops**
+ **Nested For Loops**
+ **Boolean Greater/Less**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](goArms.js)**
+ **[Python](go_arms.py)**

#### _Rewards:_
+ 566 xp
+ 191 gems

#### _Victory words:_
+ _I LOVE THE SMELL OF OGRE IN THE MORNING._

___

### _HINTS_


Ogres are coming to attack, but your army is asleep!

Use nested `for`-loops to move through the camp row by row.

At each X-mark, stop and wake your troops with a `hero.say()`

Ogres are coming to attack, and your army is asleep! Wake them up by visiting each tent one-by-one.

Move to the X Mark in front of each tent and use `hero.say()` to wake the soldiers up.

There are 4 rows with 5 tents in each row.

The sergeant knows the exact distance between tents - every camp is a little different, so don't hard-code the values!

Find the camp's distance usin the sergeant's `tentDistanceX` and `tentDistanceY`.

```javascript
var sergeant = hero.findNearest(hero.findFriends());
var stepX = sergeant.tentDistanceX;
var stepY = sergeant.tentDistanceY;
```

Using this information, construct two `for-loop`s to navigate the camp:

```javascript
var maxY = firstY + tentsInColumn * stepY;
var maxX = firstX + tentsInRow * stepX;

for (var y = firstY; y < maxY; y += stepY) {
    for (var x = firstX; x < maxX; x += stepX) {
        // Now move and say!
    }
}
```

_**Tip:** It is quicker to do **row-by-row** instead of column-by-column._

___
