## _Uneasy Truce_

#### _Legend says:_
> Keep a truce by balancing the number of your soldiers against the ogres'.

#### _Goals:_
+ _Don't anger the Yeti_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Return Statements**
+ **Iterating Over Arrays**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](uneasyTruce.js)**
+ **[Python](uneasy_truce.py)**

#### _Rewards:_
+ 324 xp
+ 124 gems

#### _Victory words:_
+ _NO ONE MAKE A SOUND..._

___

### _HINTS_

If one army gets larger than the other, the nervous soldiers will attack, waking up the angry yeti in a nearby cave! But, the ogres to the north are blocked off, and don't count. 

Summon one `"soldier"` for each ogre that appears to the south.

Notice how the function `findSouthernUnits()` adds to the end of an array:

```javascript
southernUnits.push(unit)
```

First, pass the `enemies` array as the argument to `findSouthernUnits()`.

This will return a new array containing only the enemies to the south, so save that in a new variable.

Then, compare the length of the new array to the length of your friends array, and summon a `"soldier"` if there are more enemies!

___
