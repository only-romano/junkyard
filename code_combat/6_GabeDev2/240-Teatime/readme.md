## _Teatime_

#### _Legend says:_
> Don't forget to prepare and drink your evening health potion.

#### _Goals:_
+ _Spawn 3 potions with the same time interval_
+ _Spawn 6 throwers with the same time interval_
+ _Win the game_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **If Statements**
+ **While Loops**
+ **Accessing Properties**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](teaTime.js)**

#### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _TICKTACK, TICKTACK. THE TIME IS PLAYING AGAINST YOU, OGRES._

___

### _HINTS_

You can have several timers and track them independently.
Spawn munchkins and throwers with different intervals, because throwers are more dangerous.
Also, we need some potions which we will spawn with a third time interval.

So you can run from ogres and take potions when it's required or fight against ogres and take potions.

There are four timers in this level. 

Three of them should be familiar, and we're using them to generate units and items.

However, the last one `nextPotionIn` is not required for the game logic. We're using it only for UI 
so players can see when the next potion spawns. Of course, we can just show `game.spawnPotionTime` 
but it's not clear for players because they have to compare the current time and the spawn time.
Instead, we show the remaining time until the next potion.

Unlike `game.time` we have to update that timer each game frame, so we've put in the function `updateTimers` which is called in the main game loop each game frame.

___
