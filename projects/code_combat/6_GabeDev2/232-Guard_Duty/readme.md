## _Guard Duty_
> It's a massacre down here...

#### _Legend says:_
> Someone forgot to defend the pass! Add a soldier and program them to defend!

#### _Goals:_
+ _Defeat all the ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **If Statements**
+ **If/Else Statements**
+ **While Loops**
+ **Functions**

#### _Solutions:_
+ **[JavaScript](guardDuty.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _MUST GET LONELY OUT HERE._

___

### _HINTS_

Give your soldier instructions using event handler functions!

```python
def soldierLogic():
    while True:
        enemy = soldier.findNearestEnemy()
        if enemy:
            soldier.attack(enemy)

soldier = hero.spawnXY("soldier", 42, 48)
soldier.on("spawn", soldierLogic)
```

In Game Development levels, programming soldiers is like programming a pet.

You can use the `on(eventName, eventHandlerFunction)` function to assign custom behavior to a unit.

The `eventName` argument is a string for the particular event that will trigger the `eventHandlerFunction` to execute.

The `"spawn"` event only happens once, when a unit is spawned.

The `eventHandlerFunction` argument is a function you define. You can put any code in here you want! You are the game developer after all.

As an example, consider this setup:

```javascript
function munchkinLogic() {
    while (true) {
        var enemy = munchkin.findNearestEnemy();
        if (enemy) {
            munchkin.attack(enemy);
        }
    }
}

var munchkin = game.spawnXY("munchkin", 20, 20);
munchkin.on("spawn", munchkinLogic);
```

Consider what the above code does!

+ It defines a function for the munckin's logic.
    + The logic says to attack the nearest enemy if it sees one.
+ It creates a munchkin and stores it in a variable.
+ Finally, set the action on the munchkin's spawn trigger.

It always helps to read through the code to understand what it does, before diving into the next problem.

___
