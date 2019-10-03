## _Stick Shift_

#### _Legend says:_
> Learn how to create custom goals for your games!

#### _Goals:_
+ _Add a Manual Goal to Defeat the Boss_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Place game objects**
+ **Basic Game AI**
+ **Basic Event Handling**
+ **Create a playable, sharable game project**

#### _Solutions:_
+ **[JavaScript](stickShift.js)**

#### _Rewards:_
+ 10 xp
+ 10 gems

#### _Victory words:_
+ _ASSUMING DIRECT CONTROL..._

___

### _HINTS_

Now you can create custom goals for your games!

We call them **manual** goals, because you are responsible for manually marking them as succeeded or failed.

Create a manual goal like this:

```python
myGoal = game.addManualGoal("Defeat the skeleton, save the archer!")

def onDefeat(event):
    unit = event.target
    if unit.type == "skeleton":
        game.setGoalState(myGoal, True)
    if unit.type == "archer":
        game.setGoalState(myGoal, False)

game.setActionFor("archer", "defeat", onDefeat)
game.setActionFor("skeleton", "defeat", onDefeat)
```

___
