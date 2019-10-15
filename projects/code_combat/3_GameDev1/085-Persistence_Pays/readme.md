## _Persistence Pays_

#### _Legend says:_
> Store game information in a database!

#### _Goals:_
+ _Track the game's `defeated` property_
+ _Store the `defeated` property in `db`_
+ _Beat the game_

#### _Topics:_
+ **Basic Syntax**
+ **Place game objects**
+ **Create a playable, shairable game project**

#### _Solutions:_
+ **[JavaScript](persistencePays.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _"ENERGY AND PERSISTENCE CONQUER ALL THINGS." - BENJAMIN FRANKLIN_

___

### _HINTS_

A database can store information between plays of your game.

`db.set("defeated", game.defeated)` sets the `"defeated"` number in the database to the value of `game.defeated`.

`db.add("plays", 1)` adds `1` to the `"plays"` number stored in the database.

Then use `ui.track(db, "plays")` to display the `"plays"` count!

Don't worry too much about the `onVictory` part for now.

You'll learn more about how that works in the Game Dev 2 campaign!

Game Dev 1 levels use a simplified database system to store values between games.

In advanced Game Dev campaigns, you'll learn to use real databses, such as Amazon's DynamoDB.

___
