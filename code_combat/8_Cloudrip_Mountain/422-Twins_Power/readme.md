## _Twins Power_

#### _Legend says:_
> Praise the Moon! Oh, sorry, Praise the Sun!

#### _Goals:_
+ _Defeat the Big Brawler_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Return Statements**
+ **Array Indexes**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](twinsPower.js)**
+ **[Python](twins_power.py)**

#### _Rewards:_
+ 259 xp
+ 119 gems

#### _Victory words:_
+ _GOOD JOB HERO AND HERB!_

___

### _HINTS_

We must lure this huge ogre through the temple of the Moon and the Sun. He is near-sighted and that will give us plenty of time to prepare a trap.

Use pairs of twins to awake the powers of the Sun and Moon!

Say each twin's name seperated by a space: `hero.say(twin1.id + " " + twin2.id)`

___

The code to check if two paladins are twins has been given to you: `areTwins(unit1, unit2)`.

You will need to iterate over each element each time you iternate over all the elements! Confusing, yes, but observe the following code for help:

```javascript
for (var i = 0; i < array.length; i++) {
    var elemI = array[i];
    for (var j = 0; j < array.length; j++) {
        if (i == j) {
            continue;
        }
        var elemJ = array[j];
        // Check if the two elements match

            // Say each of the element's id
    }
}
```

Be sure to move forward/backwards to lure the ogre through the trap.

___
