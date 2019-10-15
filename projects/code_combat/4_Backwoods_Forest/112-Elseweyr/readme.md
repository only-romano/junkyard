## _Elseweyr_

#### _Legend says:_
> The munchkins are so friendly, always.

#### _Goals:_
+ _Your hero must survive_

#### _Topics:_
+ **Basic Sintax**
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **If/else Statements**

#### _Items we've got (- or need):_
+ Long Sword

#### _Solutions:_
+ **[JavaScript](elseweyr.js)**
+ **[Python](elseweyr.py)**

#### _Rewards:_
+ 60 xp
+ 71 gems

#### _Victory words:_
+ _THOSE SPECIFIC MUNCHKINS WON'T BOTHER YOU EVER AGAIN!_

___

### _HINTS_

Wield your new long sword like a pro! Use `isReady()` to check if you can `"cleave"` and then `cleave()`!

Use an `else` statement to ensure the hero defends themself while the munchkins rampage around.

___


`else` can be used to perform actions when an `if`-statement isn't `true`. `else`s can ONLY be used after an `if`-statement within the same **scope**. In otherwords, they must be on the same line as the previous `if`-statement.

When reading an `else`, consider it to be all other options other than what the connected `if`-statement was.


```javascript
var enemy = hero.findNearestEnemy();
// Check if an enemy exists

if (enemy) {
    // Ther is an enemy, so attack it!
    hero.attack(enemy);
}
// Otherwise (or else), there isn't an enemy.
else {
    // There is NOT an enemy, so relax.
    hero.say("I'm safe.");
}
```

___
