## _Center Formation_

#### _Legend says:_
> Night is coming. Bring the soldiers in around the fire!

#### _Goals:_
+ _Your hero must survive_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Strings**
+ **Variables**
+ **Accessing Properties**
+ **Functions**

#### _Solutions:_
+ **[JavaScript](centerFormation.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _ATTEN-HUT!_

___

### _HINTS_

The `setActionFor` function can be used to control multiple units at once.

Make all the `"soldier"`s move to the center of the level when they spawn!

The `setActionFor` function is used to define a certain type of unit's logic. Use it to tell all soldiers to move to the center of the map, or munchkins to attack their nearest enemy, or archers to only attack the big guys!

When the behavior function is called, it creates an event of the specific unit it was called on. `event.target` is how you can command the specific unit how to perform things.

```javascript
function sayMi(event) {
    // This is the specific uni:
    var unit = event.target;
    // This makes that unit say something.
    unit.say("Mi!");
}

hame.spawnXY("munchkin", 20, 20);
hame.spawnXY("munchkin", 30, 40);

// All munchkins now have an event listener on `spawn` which calls sayMi when they spawn:
game.setActionFor("munchkin", "spawn", sayMi)
```

___
