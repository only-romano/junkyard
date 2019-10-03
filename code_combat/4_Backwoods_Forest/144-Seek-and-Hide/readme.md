## _Seek-and-Hide_

#### _Legend says:_
> You're in the ogre camp. A Brawler is in the tent near you. Ogre hunters are searching for you. Sounds impossible?

#### _Goals:_
+ _Find and collect lightstones_
+ _Defeat the Brawler ogre_

#### _Topics:_
+ **Basic Syntax**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Accessing Properties**
+ **Functions**

#### _Items we've got (- or need):_
+ Boots

#### _Solutions:_
+ **[JavaScript](seekHide.js)**
+ **[Python](seek_hide.py)**

#### _Rewards:_
+ 79 xp
+ 45 gems

#### _Victory words:_
+ _OUT OF SIGHT, OUT OF MIND._

___

### _HINTS_

Your goal is to move to each of the red X marks, searching for lightstones. If you find one, you'll have to hide at the center X mark before continuing your search.

First, finish the `checkTakeHide()` function to hide in the center of the camp after finding a lightstone.

Then, examine the sample code that calls `checkTakeHide(stone)` at the right X mark, and then write your own code to call it at the left X mark.

___

You can use a function parameter as a variable inside the function. But also you can add additional instructions, which are not related to the parameter.
For example:

```javascript
function checkAndHit(unit) {
    if (unit) {
        hero.attack(unit);
        // An additional instruction without 'unit'
        hero.say("I'n dangerous!");
    }
}
```

Also, don't forget you can call the same function as many times as you want.

```javascript
hero.moveXY(10, 10);
var enemy = hero.findNearestEnemy();
checkAndHit(enemy);

// Next point
hero.moveXY(70, 10);
enemy = hero.findNearestEnemy();
checkAndHit(enemy);
```

___
