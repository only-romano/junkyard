## _Salted Earth_

#### _Legend says:_
> Defend the start of a forest settlement.

#### _Goals:_
+ _Gather all the coins_
+ _Defeat all the ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statement**
+ **Accessing Properties**
+ **Boolean Or**

#### _Items we've got (- or need):_
+ Weapon

#### _Solutions:_
+ **[JavaScript](salted.js)**
+ **[Python](salted.py)**

#### _Rewards:_
+ 69 xp
+ 79 gems

#### _Victory words:_
+ _REMEMBER, POISON YOU DRINK, TOXINS YOU TOUCH!_

___

### _HINTS_

![](img/salted_earth.jpeg)

This level introduces the concept of the boolean `or`.

Placing an `or` between two boolean values will return a single boolean value, much like `+` takes 2 numbers and spits out a another number.

Remember that booleans are a single bit of data, `true` or `false`. `or` returns `true` if either the value before or after is `true`, or `false` if both are `false`.

```javascript
// Write boolean or using '||'
hero.say(false || false); // Hero says 'false'
hero.say(false || true); // Hero says 'true'
hero.say(true || false); // Hero says 'true'
hero.say(true || true); // Hero says 'true'
```

Which is useful if you know the exact boolean, but, programming lets you do so much more!

Recall that `<`, `>`, `<=`, `>=`, `==` return boolean values, so to make this more useful:

```javascript
var enemy = hero.findNearestEnemy();
// It helps to read it outloud:
if (hero.distanceTo(enemy) < 10 || enemy.type == "thrower") {
    // If distanceTo enemy is less 10, OR, enemy type is thrower
    hero.attack(enemy);
}
```

___

The `or` operatorn (`||` in JavaScript) is used for checking if either of two conditions are `true`.

Use an `if`-statement to check if the nearest item's type is a `"coin"` `or` `"gem"`.

```javascript
if (item.type == "coin" || item.type == "gem") {
    // ...
}
```

If the item is a gem or coin, then move to it and pick it up.

___
