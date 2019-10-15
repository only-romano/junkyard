## _Game of Coins Step 2: Score_

#### _Legend says:_
> Let's add some challenge to our game.

#### _Goals:_
+ _Reduce score with time_
+ _Increase score on collected items_
+ _The game score can't be less than zero_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](goc2.js)**

#### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _THE GAME DESIGNER SHOULD MAKE A GAME INTERESTING._

___

### _HINTS_

In the second level of the Pac-Man style arcade game series, we will add some challenge to the game.

First, we need to add a scoring system. The goal is to collect all coins as fast as possible.

So we could set the initial score to some value and reduce it with each second that passes. Then, add to the score for collecting coins and mushrooms.

Also, the score can't be less than 0.

Use the `"collect"` event and the `game loop` to implement this scoring mechanic!

___

One of the simplest ways to add replayability to a game is to add some type of score system so players can play your game again and again in attempts to increase their high score.

You can award points for player actions like defeated enemies, collected items, moving to checkpoints and so on.

For games where players should complete some goals quickly, you can define the score based on the game time.

You can reduce score with each second or calculate it based on the final time (there are many options for how to do it). Also, you can reduce score for "incorrect" actions, like collecting restricted items, non-touchable characters, entering forbidden zones and so on.

There are many more ways to implement a scoring system in your game - you should be creative and think about how you might want to implement scoring in your final project.

Part of game design is about thinking up something new!

___
