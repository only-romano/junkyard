## _Danger Valley_

#### _Legend says:_
> Ogres have taken some peasants hostage. Rescue them!

#### _Goals:_
+ _Stay out of the ogre's sight_
+ _Defeat all the ogres with a trap_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **If Statements**
+ **Array Indexes**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](dangerValley.js)**
+ **[Python](danger_valley.py)**

#### _Rewards:_
+ 259 xp
+ 119 gems

#### _Victory words:_
+ _SO THAT'S HOW IT GOT IT'S NAME!_

___

### _HINTS_

Set up a field of mines to trap incoming ogres!

The answer lies in a set of nested arrays, so lay out the fire-traps carefully.

___

Ogres have captured a group of peasants, and it's your job to save them.

Luckily a scout has gone ahead and found out what the layout of the ogres will be and reported this information back as nested arrays.

A nested array, or 2D array, is an array containing... more arrays! Look at the following code:

```javascript
var doubleArray = [[1, 2], [3, 4]];
```

A bit confusing at first, but if we clean up the code, we can better understand how it works:

```javascript
var doubleArray = [
    [1, 2],
    [3, 4]
];
```

Now that the structure is more apparent, to access a specific element you will use the familiar `[index]` notation:

```javascript
var doubleArray = [
    [1, 2],
    [3, 4]
];
var row1 = doubleArray[0];  // This is [1, 2]!
var cell1 = row[0];  // This is 1!
```

However, if you're real crafty, you can double up these index calls like so:

```javascript
var doubleArray = [
    [1, 2],
    [3, 4]
];
var cell1 = doubleArray[0][0];  // This is 1!
```


___
