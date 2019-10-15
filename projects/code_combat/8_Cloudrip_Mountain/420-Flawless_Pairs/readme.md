## _Flawless Pairs_

#### _Legend says:_
> To escape from the cemetery you need to find four pairs of equal gems.

#### _Goals:_
+ _Collect 4 flawless pairs_

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **Return Statements**
+ **Array Indexes**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](flawlessPairs.js)**
+ **[Python](flawless_pairs.py)**

#### _Rewards:_
+ 259 xp
+ 119 gems

#### _Victory words:_
+ _GEM-ERRIFIC!_

___

### _HINTS_

You need to collect 4 pairs of gems to escape from the cemetry.

Each pair must be two gems of the same value. If you make a mistake, you will faint!

The wizard helps you with the "Haste" spell. Just return to the start point after each collected gem.

___

In this level you must search through an array and find two elements that are similar.

To help, think of it like this:
1. Go through each index of an array (i @ 0)
2. Go through each index of an array again (j @ 0)
3. If i isn't j and arr[i] is arr[j], then return both as an array.

```javascript
function findPair(array) {
    for (var i = 0; i < array.length; i++) {
        var elemI = array[i];
        for (var j = 0; j < array.length; j++) {
            // Skip if *i* is *j*
            if (i == j)
                continue;
            var elemJ = array[j];
            if (elemI === elemJ) {
                // These two elements match, return them
                return [elemI, elemJ];
            }
        }
    }
    // No elements were found!
    return null;
}
```

___
