## _Backwoods Ambush A_

#### _Legend says:_
> Functionally ambush some ogre sentries in the backwoods.

#### _Goals:_
+ _Destroy All ogres_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Variables**
+ **If Statements**
+ **Functions**

#### _Items we've got (- or need):_
+ Weapon

#### _Solutions:_
+ **[JavaScript](backAmbA.js)**
+ **[Python](back_amb_a.py "#3 - 4s")**

#### _Rewards:_
+ 35 xp
+ 42 gems

#### _Victory words:_
+ _SO EFFICIENT!_

___

### _HINTS_

Ah, Backwoods Ambush, we return! However, there is an easier way to do this with better form and functions!

We'll use a function to improve our workflow and greatly shorten the amount of code we need to write.

Remember how functions are structured:

```javascript
function attackNearest() {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        hero.attack(enemy);
    }
}
```

But don't forget that functions can have parameters:

```javascript
function pickUpItem(item) {
    if (item) {
        var xPos = item.pos.x;
        var yPos = item.pos.y;

        hero.moveXY(xPos, yPos);
    }
}
```

So there is no reason to limit ourselves to only one parameter! It's quite possible to pass multiple arguments into a function.

```javascript
function moveAndSay(x, y, words) {
    hero.moveXY(x, y);
    hero.say(words);
}
```

Use these concepts to help complete this level!

___
