## _JavaScript: Back to Back_

#### _Legend says:_
> Patrol the village entrances, but stay defensive.

#### _Goals:_
+ _Villagers must survive_
+ _Elimininate the ogres_

#### _Topics:_
+ **Basic Sintax**
+ **Arguments**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **If/else Statements**

#### _Solutions:_
+ **[JavaScript](backBlack.js)**

#### _Rewards:_
+ 60 xp
+ 20 gems

#### _Victory words:_
+ _BACK AGAIN!_

___

### _HINTS_

![](img/back_to_back.jpeg)

Expand your code's possibilities by using `else`!

`else` is just like `if`, except it contains the code that should run when the `if` condition is `false`:

```javascript
if(enemy) {
    // This happens when there is an enemy.
    hero.attack(enemy);
} else {
    // This happens when there is no enemy.
    hero.say("I don't see an enemy!");
}
```

___

This level introduces the `else` part of `if/else`.

When you add an `else` clause, you choose what to do both when the condition is true and when it is not true.

So you can say, _if_ there is an enemy, _then_ attack it, _else_ move to the X.

To show you how it works, the `if` and the `else` are set up for you, and you need to put in the `attack` and `moveXY` methods so that your hero attacks enemies on sight, but when there are no enemies, moves back to the X marker to defend the peasants.

Make sure you get the coordinates for the X marker correct, or you might not be able to defend both your peasants in time.

___
