## _Standard Operating Procedure_

#### _Legend says:_
> Use the same SOP for all unit types!

#### _Goals:_
+ _Have all units attack_
+ _Win the game_

#### _Topics:_
+ None

#### _Solutions:_
+ **[JavaScript](sop.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _WITHOUT SOP YOU'D BE SOL._

___

### _HINTS_

Event handers get information about the event that triggered them:
+ The `event.target` property contains the unit that is executing the event handler.

```python
# Use event.target, so all units can use the same event handler function
def sayHello(event):
    unit = event.target
    unit.say("Hi!")

game.setActionFor("soldier", "spawn", sayHello)
```

In previous levels you did something like this:

```javascript
var soldier1 = spawnXY("soldier", 10, 10);

function fightEnemies(event) {
    while (true) {
        var enemy = soldier1.findNearestEnemy();
        if (enemy) {
            soldier1.attack(enemy);
        }
    }
}
```

But what happens when we add more soldiers?

```javascript
var soldier1 = spawnXY("soldier", 10, 10);
var soldier2 = spawnXY("soldier", 12, 10);
var soldier3 = spawnXY("soldier", 15, 10);
```

Because `soldier1` is hard-coded into the `findEnemies()` function, it won't work for `soldier2` or `soldier3`!

Instead, we should use `event.target` to know which soldier is executing the event handler function:

```javascript
function fightEnemies(event) {
    while (true) {
        var unit = event.target;
        var enemy = unit.findNearestEnemy();
        if (enemy) {
            unit.attack(enemy);
        }
    }
}
```

Now it works for all the soldiers, and for any other types of units like archers or munchkins, too!

___
