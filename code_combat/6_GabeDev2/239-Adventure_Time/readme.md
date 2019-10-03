## _Adventure Time_

#### _Legend says:_
> Spawn enemies as time passes.

#### _Goals:_
+ _Spawn at least 5 ogres_
+ _Win the game_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **If Statements**
+ **While Loops**
+ **Accessing Properties**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](adventureTime.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _TIME KEEPS ON TICKING._

___

### _HINTS_

In this level, `spawnTime` is a variable we're using to track when the next `"munchkin"` should spawn. In the beginning, it's set to zero, which means an ogre will spawn at the start of the game.

The property `game.time` is automatically updated by the game engine as time passes. It is the amount of time since the start of the game, in **seconds**.

In the **while-true** loop, we check each time to see if `game.time` is greater than `spawnTime`. If it is, we know it's time to spawn a new ogre.

After spawning a new ogre, we update `spawnTime` to be equal to the current `game.time` plus however many seconds we want to wait in between spawns (in this case, we're using `2`).

___
