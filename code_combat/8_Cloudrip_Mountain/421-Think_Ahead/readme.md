## _Think Ahead_

#### _Legend says:_
> If you know the next move of your enemy, then you are invulnerable.

#### _Goals:_
+ _Destroy the cannon_
+ _Soldiers must survive_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Return Statements**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](thinkAhead.js)**
+ **[Python](think_ahead.py)**

#### _Rewards:_
+ 259 xp
+ 119 gems

#### _Victory words:_
+ _A WELL PLANNED PLAN!_

___

### _HINTS_

Ogres have brought in a huge artillery cannon!

The soldiers are frantically avoiding being targeted, but it is no use! The huge cannon targets two units that are closest to each other.

Use this to your advantage and guide the wizards to apply Stoneskin to those two soldiers.

___

The artillery will try to hit the two nearest units with each shot! Use this to your advantage and have your healers apply Stoneskin to the two closest soldiers.

You will need to iterate over all of our units and find the two whose distance is the smallest.

```javascript
// The following code finds the two FURTHEST units
// In the level you need to find the two CLOSEST units

var maxDistance = 0;
var furthestPair = [null, null];
for (var i = 0; i < array.length; i++) {
    var itemI = array[i];
    for (var j = 0; j < array.length; j++) {
        // IMPORTANT: don't compaare the same unit with itself
        if (i == j) {
            continue;
        }
        var itemJ = array[j];
        var dist = itemI.distanceTo(itemJ);
        // Check if the distance is greater than maxDistance
            // Create an array of the two elements and assign it to farthestPair
    }
}
```

___
