## _Agony of Defeat_

#### _Legend says:_
> Snatching loose change from the jaws of defeat.

#### _Goals:_
+ _Collect 8 coins_
+ _Win the game_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **If Statements**
+ **While Loops**
+ **Accessing Properties**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](agonyOfDefeat.js)**

#### _Rewards:_
+ 10 xp
+ 10 gems

#### _Victory words:_
+ _IT'S ALL ABOUT THE LOOT DROPS._

___

### _HINTS_

When a unit i defeated, a `"defeat"` event is triggered:

```python
def onDefeat(event):
    unit = event.target
    unit.say("You got me!")

game.setActionFor("munchkin", "defeat", onDefeat)
```

In this level, you'll spawn a `"gold-coin"` near a defeated unit using thre `"defeat"` event.

Using the `"defeat"` event, we can have enemies drop loot!

When a munchkin is defeated, spawn a `"gold-coin"` near the defeated munchkin's `pos` by adding a `randomInteger` between `-5` and `5` to the `pos.x` and `pos.y`.

When playing your game, you may notice that sometimes the munchkins don't seem to spawn a coin. 
Don't worry - the coin is probably just being spawned on top of the player, who immediately collects it.

___
