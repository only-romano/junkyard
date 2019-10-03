## _Marauder_

#### _Legend says:_
> I don't know what it is, but they are full of gold.

#### _Goals:_
+ _Collect 100 gold_

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **While Loops with Conditionals**
+ **Accessing Properties**
+ **If Statements**
+ **Boolean Greater/Less**

#### _Solutions:_
+ **[JavaScript](marauder.js)**
+ **[Python](marauder.py)**

#### _Rewards:_
+ 277 xp
+ 211 gems

#### _Victory words:_
+ _GOLD PIÑATA!_

___

### _HINTS_

These pacing mechs are full of gold. To get that gold you need to break them open!

First, use a `while` statement to collect all coins that exist.

```javascript
var coin = hero.findNearest(hero.findItems());
while(coin) {
    // Collect the coin.
    coin = hero.findNearest(hero.findItems());
}
```

Then, attack the nearest enemy `while` its `health` is greater than `0`.

`while`-expression is an useful construction, which allows you do some action while something exists, for example. For example, you can watch for an enemy health while it's alive.

```javascript
while (robot.health > 0) {
    hero.say("The robot's alive");
}
```

`while`-expression allows to check the existance of some thangs too:

```javascript
var weakOgre = hero.findNearestEnemy();

while (weakOgre) {
    hero.attack(weakOgre);
    hero.say("One hit, one frag! Next!");
    weakOgre = hero.findNearestEnemy();  // Reaasign (update) the variable.
}
```

___
