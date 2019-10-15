## _By Any Other Name_

#### _Legend says:_
> Rename variables to reveal secret gems.

#### _Goals:_
+ _Defeat the ogres_
+ _Collect the Gems_
+ _Bonus: no code problems_

#### _Topics:_
+ **Basic Sintax**
+ **Arguments**
+ **Variables**

#### _Items we've got (- or need):_
+ Simple boots
+ _Optional: Elementals codex 1+_
+ _Optional: Emperor's gloves_

#### _Solutions:_
+ **[JavaScript](byAnyOtherName.js)**
+ **[Python](by_any_other_name.py "#3: 5.13s")**

#### _Rewards:_
+ 21 xp
+ 30 gems

#### _Victory words:_
+ _AN OGRE BY ANY OTHER NAME IS JUST AS VILE!_

___

### _HINTS_

A _variable_ can have any name you want it to: it's just a label for an object! In this level, rename enemy variables to reveal the gems.

In this level, you need to defeat two ogres and collect two gems. The provided code takes care of the ogres – but where are the gems? In order to make the gems appear, you'll have to _change_ the names of variables in your code.

```javascript
// These are the gems
var enemy = hero.findNearestEnemy();
var anyName = hero.findNearestEnemy();
```

When you change the name of a variable, make sure you change it everywhere that it is used.

```javascript
var anyName = hero.findNearestEnemy();
hero.attack(anyNamy);  // right
hero.attack(enemy);  // wrong
```

___
