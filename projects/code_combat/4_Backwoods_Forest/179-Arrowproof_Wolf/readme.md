## _Arrowproof Wolf_

#### _Legend says:_
> The forest is full of rogues. You'd better use some protection against arrows (or spears).

#### _Goals:_
+ _Collect 15 mushrooms_

#### _Topics:_
+ **Basic Syntax**

#### _Items we've got (- or need):_
+ Wolf Pet
+ _Optional: Elemental codex 1+_
+ _Optional: Boots with jump available_

#### _Solutions:_
+ **[JavaScript](arrowproof.js)**
+ **[Python](arrowproof.py "Top-10 - 27.8s")**

#### _Rewards:_
+ 60 xp
+ 71 gems

#### _Victory words:_
+ _YOU ARE FAST. YOU CAN CATCH AN ARROW, BUT CAN YOU CATCH FUTURE?_

___

### _HINTS_

Ogre throwers are powerful in this forest. They can easily defeat even strong heroes. The Wolf Pet can catch arrows even if you don't command it. Just to have it close to you.

Don't forget to wake up the pet (come to it and say something).

Use the nearest item's `pos`, `x`, and `y` to find where to move.

The Wolf pet can catch arrows (or spears, but bullets or shells...). If you haven't commanded anything to your pet and it is in **automatic** mode, then the pet catches arrows without command. Of course as any ablity it has some cooldown.

Also you can use it actively:

```javascript
var arrow = hero.findNearest(hero.findEnemyProjectiles());
if (arrow) {
    pet.catch(arrow);
}
```

___
