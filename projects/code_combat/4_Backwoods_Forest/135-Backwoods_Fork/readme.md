## _Backwoods Fork_

#### _Legend says:_
> Use a custom function with parameters to simplify your code!

#### _Goals:_
+ _Defeat the ogres_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Functions**

#### _Items we've got (- or need):_
+ Weapon to one-shot munchkins

#### _Solutions:_
+ **[JavaScript](backFork.js)**
+ **[Python](back_fork.py)**

#### _Rewards:_
+ 79 xp
+ 45 gems

#### _Victory words:_
+ _THE CORRECT ANSWER IS TO TAKE THE FORK!_

___

### _HINTS_

![](img/backwoods-fork.jpeg)

A **function** is an important concept when writing code! They are used to separate individual, **repeatable** parts of your code into easier to digest pieces.

Often times, a function requires an **argument**. This is a way to customize a **repeatable** action while still optimizing and cutting down the length of one's code. This is what you put in between `(` and `)` when **calling** the function.

A **parameter** is what a potential **argument** is called inside the function definition.

```javascript
// This function has 1 parameter: 'target':
function checkAndAttack(target) {
    // 'target' is a predefined variable.
    if(target) {
        hero.attack(target);
    }
}
var enemy = hero.findNearestEnemy();
// Below, 'enemy' is the argument. This becomes 'target' inside checkAndAttack.
checkAndAttack(enemy);
```

___
