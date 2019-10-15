## _From Dust to Dust_

#### _Legend says:_
> You can create game objects. However you can destroy or ruin them.

#### _Goals:_
+ _Block the forest passages and clear them later_
+ _Defeat 2 ogre generators_
+ _Beat the game_

#### _Topics:_
+ **Basic Syntax**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](fromDustToDust.js)**

#### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _NOW I AM BECOME GAME MASTER, THE DESTROYER OF WORLDS._

___

### _HINTS_

The most time we `spawn` new objects for games. However, sometimes we need to remove them. There are two ways to do it:
+ units or attackable objects (ex. `generator`) can be "killed" with the method `.defeat()`.
+ any objects can be removed from the game scene with the method `.destroy()`.

```python
# Create and defeat a munchkin.
munchkin = game.spawnXY("munchkin", 10, 10)
munchkin.defeat() # We can see the defeated ogre.
# Create and remove a scout
scout = game.spawnXY("munchkin", 20, 20)
scout.destroy() # Nothing here
```

`defeat()` and `destroy()` are similar methods, however there is huge difference between them.

___
