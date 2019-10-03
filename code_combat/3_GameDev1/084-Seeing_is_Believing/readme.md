## _Seeing is Believing_

#### _Legend says:_
> Users like to aim for high scores. Use user-interface elements to display their score to them!

#### _Goals:_
+ _Track the game's `defeated` property_
+ _Defeat 6 munchkins in under 20 seconds_
+ _Set ip 20 second survival goal_
+ _Beat the game_

#### _Topics:_
+ None

#### _Solutions:_
+ **[JavaScript](seeingIsBelieving.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _USER INTERFACING COMPLETE: BEEP BOOP_

___

### _HINTS_

Use the `ui.track` function to display an object's property for the player.

Be sure to beat up 6 munchkins before the 20-second survival ends.

The `ui` object contains helpful methods to control the player's user-interface. One particular method `track()` is used to display an object's properties in real time for the player to observe.

For example, if you want to show the user how long they've been playing the game, the `game` object has a `time` property so use:

```javascript
ui.track(game, "time");  // Will display the elapsed time in seconds
```

For this level you should add a `ui.track` for `"defeated"` and defeat 6 munchkins in under 20 seconds!

___
