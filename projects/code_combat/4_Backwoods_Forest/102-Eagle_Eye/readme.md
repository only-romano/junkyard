## _Eagle Eye_

#### _Legend says:_
> Spot the ogres with help from an eagle-eyed baby griffin!

#### _Goals:_
+ _Defeat the ogres_
+ _Bonus: cleen code (no warnings)_

#### _Topics:_
+ **Basic Sintax**
+ **Arguments**
+ **Variables**
+ **If Statements**
+ **While Loops**

#### _Items we've got (- or need):_
+ Weapon

#### _Solutions:_
+ **[JavaScript](eagle.js)**
+ **[Python](eagle.py)**

#### _Rewards:_
+ 53 xp
+ 33 gems

#### _Victory words:_
+ _GOOD EYE, GRIFFY!_

___

### _HINTS_

A Griffin pal has arrived to help! It will call out the ogres as they arrive.

There won't always be an ogre, so you should use an `if`-statement to check if an enemy exists before trying to attack it.

```javascript
var enemy = hero.findNearestEnemy();
if(enemy) {
    // There IS an enemy nearby!
}
```

You must use an `if`-statement to check if an enemy exists, so the hero doesn't try to attack someone that isn't there!

For example, a fisherman would check if a fish is caught every time they cast their line:

```javascript
var fish = fisherman.castLine();

if (fish) {
    fisherman.store(fish);
}
```

Imagine trying to store nothing in a pail! It's confusing to think about.

___
