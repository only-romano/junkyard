## _Ring Bearer_

#### _Legend says:_
> Escort the Ring Bearer out of the mountains.

#### _Goals:_
+ _Escape to the East_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Return Statements**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](ringBearer.js)**
+ **[Python](ring_bearer.py)**

#### _Rewards:_
+ 365 xp
+ 170 gems

#### _Victory words:_
+ _INVISIBILITY? NO, THAT'S A DIFFERENT RING. THIS ONE'S FLOWERS._

___

### _HINTS_

Use the `findSoldierOffset` function to find a soldier's radial offset.

Add that number to the peasant's position to create a circular protection area around the ring-bearing peasant!

For this level, you should use the functions that we supplied to calculate where a soldier should move to, in order to form a ring of soldiers around the peasant.

You don't have to fully understand what those functions do to use them, other than the inputs and outputs of `findSoldierOffset(soldiers, i)`.

The first argument `soldiers` is the array containing all of your soldiers.

The second argument `i` is the index of the soldier (in the soldiers array) that you want to find the offset position for.

The `findSoldierOffset` function returns an `{x, y}` object containing the offset position the soldier at position `i` should stand, relative to the peasant.

To calculate where the soldier should move to, you add the offset to the peasant's position like this:

```javascript
var moveTo = {"x": peasant.pos.x + offset.x, "y": peasant.pos.y + offset.y};
hero.command(soldier, "move", moveTo);
```

___
