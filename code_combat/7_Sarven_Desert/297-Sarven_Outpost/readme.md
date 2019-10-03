## _Sarven Outpost_

#### _Legend says:_
> Patrol the outskirts of an outpost in the desert. Fend off ogres and watch your watch!

#### _Goals:_
+ _Defeat the ogres._

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **While Loops with Conditionals**
+ **Accessing Properties**
+ **Geometry**
+ **Trigonometry**

#### _Solutions:_
+ **[JavaScript](sarvenOutpost.js)**
+ **[Python](sarven_outpost.py)**

#### _Rewards:_
+ 162 xp
+ 76 gems

#### _Victory words:_
+ _EXCELLENTLY TIMED!_

___

### _HINTS_

The sample code shows you how to patrol in a circle, based on time.

After each movement, find and defeat any enemies before moving on with the patrol.

Patrolling the deserts is tough work. Time-based patrols must rely on a hero's watch to accomplish this.

To help understand what the movement code is, consider the pieces:

```javascript
// The current time, divide by 4 to slow down the hero.
var polarPos = hero.time / 4;
// Using trigonometric functions, we can turn our polarPos into a number between 1 and -1.
var xPos = 40 + Math.cos(polarPos) * 20;
// So we get 40 or 34 + [-20, 20] with a nice circular path.
var yPos = 34 + Math.sin(polarPos) * 20;
```

Remember that `while` loops can be used to check a condition until it is true. For example, getting healed until above 75% health:

```javascript
while (hero.health < hero.maxHealth * 3 / 4) {
    hero.say("I need more heals!");
}
```

___
