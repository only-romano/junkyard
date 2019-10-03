## _Them Bones_

#### _Legend says:_
> Generators spawn enemies over time.

#### _Goals:_
+ _Spawn a generator_
+ _Spawn a lightstone_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Place game objects**
+ **Create a playable, shairable game project**

#### _Solutions:_
+ **[JavaScript](themBones.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _I LIKED IT BETTER WHEN THE SKELETONS WERE IN THE CUPBOARD._

___

### _HINTS_

A `"generator"` is a building that spawns enemies every so often.

By default, the `"generator"` spawns `"skeletons"`s, a powerful enemy that will attack both humans and ogres!

But `"skeleton"`s have a weakness to `"lightstone"`s.

If the player picks up a `"lightstone"`, skeletons will flee from the player, buying enough time to destroy the `"generator"`.

You can configure the behavior of a `"generator"` by setting its properties:

```javascript
var generator = game.spawnXY("generator", 20, 20);

generator.spawnType = "skeleton";
generator.spawnDelay = 5;
```

`generator.spawnType` is a string, representing the type of enemy to spawn. 

`generator.spawnDelay` is a number, representing the delay in seconds between spawns.

___
