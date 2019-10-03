## _Perimeter Defense_

#### _Legend says:_
> A peaceful village in the mountain forest. It's quiet. Too quiet. Prepare the defenses!

#### _Goals:_
+ _Peasants must survive_
+ _Protect village_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Strings**
+ **Variables**
+ **For Loops**
+ **Boolean Greater/Less**

#### _Solutions:_
+ **[JavaScript](perimeterDefense.js)**
+ **[Python](perimeter_defense.py)**

#### _Rewards:_
+ 379 xp
+ 175 gems

#### _Victory words:_
+ _HOPEFULLY NO ONE NEEDS TO LEAVE THE TOWN!_

___

### _HINTS_

Set up the town with a formidable defense!

Patrol the perimeter of the village and tell peasants to build at each spot.

`for-loops` can be used for more than iterating over arrays! It is possible to increment by 2, 4, or even 10 or 20 units at a time!

```javascript
for (var i = 0; i < 100; i += 10) {
    hero.say(i);  // The hero will say 0, 10, 20, ... etc!
}
```

It is also possible to change the starting position:

```javascript
for (var i = 20; i < 100; i += 20) {
    hero.say(i);  // The hero will say 20, 40, 60, ... etc!
}
```

Use this to navigate around the perimeter of the town and use `say` to tell the peasants when to build.

___
