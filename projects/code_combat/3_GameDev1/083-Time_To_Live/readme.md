## _Time To Live_

#### _Legend says:_
> Survive for X seconds.

#### _Goals:_
+ _Set up munchkin generator_
+ _Set up attackDamage and maxHealth for the player_
+ _Set ip 20 second survival goal_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Place game objects**
+ **Create a playable, shairable game project**

#### _Solutions:_
+ **[JavaScript](timeToLive.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _THIS TOO SHALL PASS_

___

### _HINTS_

`game.addSurviveGoal()` sets up a goal for the player to survive until all other goals are complete.

You can pass an number as an argument like: `game.addSurviveGoal(20)` to configure it so that the player has to survive for `20` seconds.

Remember, when you want to set properties on a spawned object, you need to assign the object to a variable first.

```javascript
var myGen = game.spawnXY("generator", 40, 40);
myGen.spawnType = "munchkin";
```

___
