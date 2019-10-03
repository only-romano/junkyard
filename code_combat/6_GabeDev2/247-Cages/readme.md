## _Cages_

#### _Legend says:_
> Fences won't protect ogres from the game master's rage.

#### _Goals:_
+ _Destroy 2 fences_
+ _Defeat 2 monster generators_
+ _Beat the game_

#### _Topics:_
+ **Basic Syntax**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](cages.js)**

##### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _CAGES PROTECT THOSE WHO ARE OUTSIDE OF THOSE WHO ARE INSIDE AND VICE VERSA._

___

### _HINTS_

`unit.destroy()` removes a unit from the game. It's like un-spawning.

`unit.defeat()` leaves the unit in the game, but it is "defeated".

In this level, count spawned munchins and scouts. When enough have spawned, use `destroy` on fences and `defeat` on generators.

```python
if game.scoutsSpawned >= 5:
    someGenerator.defeat()
    someWall.destroy()
```

___
