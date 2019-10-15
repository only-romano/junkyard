## _Don't Touch Them_

#### _Legend says:_
> Set goals for ogre population.

#### _Goals:_
+ _Add 3 Manual Goals_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Place game objects**
+ **Basic Game AI**
+ **Basic Event Handling**
+ **Create a playable, sharable game project**

#### _Solutions:_
+ **[JavaScript](dontTouchThem.js)**

#### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _IT'S TOO MUCH BLUE ON THAT FIELD._

___

### _HINTS_

Manual goals can be marked as either a success or failure. Also you can read the state of goals with the property `success`.

```python
goal = game.addManualGoal("Do the thing.")
# This marks the goal as a success.
game.setGoalState(goal, True)
# This marks the goal as a failure.
game.setGoalState(goal, False)
# Checking the goal state.
if goal.success:
    hero.say("Done!")
```

When you mark a manual goal as failed, the game will end.

Let's use it to make a game where the player only needs to defeat `"scout"` ogres and must not touch `"munchkin"` ogres.

If you use manual goals don't forget to set their state.

Some goals might depend on other goals before being marked complete. In this level, the `dontTouchGoal` is marked as failed if the player takes the forbidden action, and only marked for success when the other two goals are successful.

For the current level, we wait until both "success" goals are completed and only after that, we set `dontTouchGoal`'s state to True.

This is similar to how `addSurviveGoal` works. It only succeeds when all the other goals are complete.

___
