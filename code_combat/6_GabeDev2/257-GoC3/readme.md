## _Game of Coins Step 3: Enemies_

#### _Legend says:_
> Let's add some enemies to our game.

#### _Goals:_
+ _Spawn a scout generator_
+ _Scout should be able "one-hit" the hero_
+ _Add survival goal_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](goc3.js)**

#### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _THE GAME PRODUCER SHOULD REMEMBER ABOUT COMPETITORS._

___

### _HINTS_

In step three of the Pac-Man style arcade game series, we will add enemies to the game.

Enemies make our game more challenging and less predictable.

We're making a "run and catch" style game, where the enemies instantly defeat the player if they catch the player.

We will use a "one-hit" mechanic so enemies attack damage should be greater than or equal the maximum health of the player.

The player will have to avoid the ogres... unless they have a power-up (we'll create power-ups in the next level)!

___

Enemies add excitement to your game.

There are many different types of enemies you can use in your games: they can fight with the player, they can chase and catch the player, or they can be a competitor (racing games, for example).

Adding enemies to our game will be simple if we use a `generator`.

However enemies are spawned over the time, so we should use the `"spawn"` event to configure them as we want.

Currently, we can't defeat enemies, so `"defeat"` event is not required. Also, it's better to make them slow, otherwise it will be a really hard game.

___
