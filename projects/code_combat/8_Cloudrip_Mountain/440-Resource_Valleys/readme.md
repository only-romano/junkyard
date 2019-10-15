## _Resource Valleys_

#### _Legend says:_
> Gold Gorge, Silver Swale, and Bronze Basin! Command peasants to gather precious metals from these resource-rich valleys.

#### _Goals:_
+ _Collect all the coins_
+ _Humans must survive_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Array Length**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](resourceValley.js)**
+ **[Python](resource_valley.py)**

#### _Rewards:_
+ 255 xp
+ 117 gems

#### _Victory words:_
+ _FILTER-Y!_

___

### _HINTS_

Command peasants to pick their nearest coin, but, don't let them target the wrong coin!

The peasants are unable to get the coins from other areas. However, each area only spawns a certain value of coin! Filter the coins by value and have each peasant only find the nearest of special arrays.

In this level, the hero will need to filter coins so there won't be any confusion amongst the peasants!

Filtering is the process of keeping or removing certain elements. Specifically in this level, the hero should filter each of the coins into their own array to pass to the corresponding peasant.

Another way of doing what is demonstrated in the level is as follows:

```javascript
// Take an array with lots of elements
var enemies = hero.findEnemies();
// Set aside a new array to put our desired types.
var throwers = [];
// Iterate over all the elements our searchable array.
for (var i = 0; i < enemies.length; i++) {
    var enemy = enemies[i];
    // Check if the element matches our desired condition.
    if (enemy.type == "thrower") {
        // If so, push that element into our subset array.
        throwers.push(enemy);
    }
}
// Now we have an array of all the throwers!
throwers;
```

___
