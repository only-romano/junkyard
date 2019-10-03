## _Bookkeeper_

#### _Legend says:_
> Use your watch to keep track of time while counting up victories and gold.

#### _Goals:_
+ _Report ogres defeated in the first wave_
+ _Report gold collected_
+ _Report ogres defeated in the second wave_

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Nested If Statements**
+ **Accessing Properties**
+ **Break Statements**

#### _Solutions:_
+ **[JavaScript](bookkeeper.js)**
+ **[Python](bookkeeper.py)**

#### _Rewards:_
+ 162 xp
+ 76 gems

#### _Victory words:_
+ _HOW YOU LIKE ME NOW()?_

___

### _HINTS_

This level has three phases:
+ Fight ogres for 15 seconds.
+ Collect coins for 15 seconds.
+ Fight more ogres for 15 seconds.

Tell Naria your total victories or gold after each phase. You can get know how much gold you have with the hero's property `gold`.

Use `time` to check the time, and `break` to cancel a `while` loop.

You can perform an action repeatedly until a certain time using `time` and `break` like this:

```javascript
while (true) {
    // Do something
    if (herio.time > 15) {
        break;
    }
}
```

Also, you can tell when you've defeated an enemy like this:

```javascript
hero.attack(enemy);
if (enemy.health <= 0) {
    defeated += 1;
}
```

___
