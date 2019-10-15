## _Double Cheek_

#### _Legend says:_
> Are you sneaky enough to collect gold right under the ogres very nose without getting caught?

#### _Goals:_
+ _Defeat at least 6 ogres_
+ _Collect at least 30 gold_
+ _Escape_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops with Conditionals**
+ **If Statements**
+ **If/Else Statements**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](doubleCheck.js)**
+ **[Python](double_check.py)**

#### _Rewards:_
+ 197 xp
+ 164 gems

#### _Victory words:_
+ _YOU TURNED DOUBLE-CHEEKS TO THE DEADLY HEADHUNTERS!_

___

### _HINTS_

First defeat 6 ogres in the abandoned village. Then collect at least 30 gold by picking up coins that are scattered around the oasis.

A `while`-loop is a good way to repeat actions until you reach your goals.

A `while`-loop will continue looping WHILE the condition is TRUE:

```javascript
// while the hero has less than 30 gold... collect coins.
while(hero.gold < 30) {
    var item = hero.findNearestItem();
    if(item) {
        hero.moveXY(item.pos.x, item.pos.y);
    }
}
```

Make sure you are always doing something in a `while`-loop, otherwise you may get an infinite loop error.

Like an `if` statement, a **while-condition** loop specifies a **condition**. Every time the loop re-starts at the beginning, it checks to see if the **condition** is **true**. If so, it will execute again. If not, it stops and your program moves on to the code after the loop.

In other words, _while **condition** true, keep looping_.

_**Note**: that it is possible to create an **infinite loop** if your loop condition is never false!_

```javascript
var defeatedOgres = 0;
while (defeatedOgres < 6) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        hero.attack(enemy);
        defeatedOgres += 1;
    }
}
```

___
