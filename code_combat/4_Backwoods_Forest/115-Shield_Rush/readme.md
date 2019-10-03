## _Shield Rush_

#### _Legend says:_
> Combine cleave and shield to endure an ogre onslaught.

#### _Goals:_
+ _Use "shield" to endure the onslaught_

#### _Topics:_
+ **Basic Sintax**
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **If/else Statements**

#### _Items we've got (- or need):_
+ Long Sword
+ Shield

#### _Solutions:_
+ **[JavaScript](shRush.js)**
+ **[Python](sh_rush.py)**

#### _Rewards:_
+ 60 xp
+ 71 gems

#### _Victory words:_
+ _WAY TO HULK OUT ON THOSE OGRES!_

___

### _HINTS_

![](img/shield_rush.jpeg)

You have access to a new method: `shield()`. Combine `if-else` to use `shield()` while you wait for `cleave()` to be ready!

Be sure to use a **while-true loop**, as you only `shield()` for a short time.

___

Your shield gives you the `shield()` ability, which blocks some of the damage you take while you are shielding. You can't do anything else while shielding, but it's a useful ability to help you stay alive until you can use `cleave()` again.

Remember that special abilities like `cleave` have cooldown periods, which means you can't use them all the time. (You can only cleave every ten seconds.) You need to check if they are ready to use with your Sundial Wristwatch's `isReady()` method.

You'll need to use `if/else` like this:

```javascript
while (true) {
    var enemy = hero.findNearestEnemy();
    if (hero.isReady("cleave")) {
        // Cleave!
    } else {
        // Shield yourself!
    }
}
```

Hover over the `isReady`, `cleave`, `shield`, and `if/else` documentation in the lower right if you need a reminder on the syntax.

Tip: **use a loop**! The sample code won't always give you the `while` statement. You need a loop so that you can decide what to do over and over instead of just once in the beginning.

___
