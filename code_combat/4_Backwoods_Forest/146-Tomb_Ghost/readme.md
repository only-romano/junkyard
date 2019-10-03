## _Tomb Ghost_

#### _Legend says:_
> The only exit to the tomb is blocked by ogres. Hide in the shadows and attack wisely.

#### _Goals:_
+ _Defeat the ogre munchkins_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Functions**

#### _Items we've got (- or need):_
+ Weapon
+ **No longrange glasses**

#### _Solutions:_
+ **[JavaScript](thombGhost.js)**
+ **[Python](thomb_ghost.py)**

#### _Rewards:_
+ 79 xp
+ 45 gems

#### _Victory words:_
+ _OOOO! OOOOOOO OOO! O._

___

### _HINTS_

Practice using a parameter passed into a function:

```javascript
function hitAndRun(target) {
    if(target) {
        hero.attack(target);
        hero.moveXY(10, 20);
    }
}

var enemy = hero.findNearestEnemy();
hitAndRun(enemy); // Call hitAndRun with target set to enemy
```

Remember that a **parameter** is a way of passing information into a function. It is a predefined variable containing whatever was put between the `()` when the function was **called**.

Just use the `target` parameter like you would any variable:

```javascript
function checkAndDefend(target) {
    if (target) {
        hero.say("I see an enemy! I should defeat them!");
    }
}
```

___
