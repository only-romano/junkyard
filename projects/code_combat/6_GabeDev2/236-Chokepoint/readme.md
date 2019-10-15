## _Chokepoint_

#### _Legend says:_
> Control all soldiers on patrol individually.

#### _Goals:_
+ _All soldiers must survive_
+ _Defeat 10 munchkins_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **If Statements**
+ **If/Else Statements**
+ **While Loops**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](Chokepoint.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _ASPHYXIATION OF THE ENEMY'S ASSAULT!_

___

### _HINTS_

Use soldiers to defend the forest lanes.

Creating a variable of the starting position, for each soldier, before a while-true loop can be used to return each soldier to their starting position.

Long-term actions can be defined inside of an event-callback. Use a `while-true` loop, and it will run the code for each soldier over and over, just like with your hero!

Treat each function as an indivudal hero and remember to store the information required within those functions.

```javascript
function defendNearestFriend(event) {
    var unit = event.target;
    var friend = unit.findNearestFriend();

    while (true) {
        var enemy = unit.findNearestEnemy();

        if (enemy.distanceTo(friend) < 5) {
            unit.attack(enemy);
        }
    }
}

game.spawnXY("soldier", 20, 20);
game.spawnXY("soldier", 30, 40);

game.setActionFor("soldier", "spawn", defendNearestFriend);
```

___
