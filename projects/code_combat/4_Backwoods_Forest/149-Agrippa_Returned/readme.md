## _Agrippa Returned_

#### _Legend says:_
> Streamline your code even more with advanced functions.

#### _Goals:_
+ _Rid the meadow of ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Nested If Statements**
+ **Assigning Properties**
+ **Return Statements**

#### _Items we've got (- or need):_
+ Long Sword

#### _Solutions:_
+ **[JavaScript](agrippaReturn.js)**
+ **[Python](agrippa_return.py)**

#### _Rewards:_
+ 74 xp
+ 74 gems

#### _Victory words:_
+ _THERE IS TACTICAL ADVANTAGE TO EFFICIENT CODE._

___

### _HINTS_

![](img/the_agrippa_defense.jpeg)

Just as in the previous **The Agrippa Defense** level, you'll be replaying the same scenario, but with even more advanced functions.

You can use a function to calculate a value, then `return` it so you can use it in your code.

```javascript
hero.triple = function(a) {
    var b = a + a + a;
    return b;
};

hero.say("3 × 3 = " + triple(3));
hero.say("4 × 3 = " + triple(4));
```

In the previous **Agrippa Defense** level, we streamlined our code by using functions to extract logic. In this level, we use a function to calculate a value and pass it back to the calling code.

In this level, we do a distance check so that we can only fight ogres that are close to us:

```javascript
while (true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        var distance = hero.distanceTo(enemy);
        if (distance < 5) {
            hero.cleaveOrAttack(enemy);
        }
    }
}
```

We can make this code cleaner by putting the distance check in its own function. The function `return`s a **true** or **false** value so we can decide whether or not to attack:

```javascript
while (true) {
    var enemy = hero.findNearestEnemy();
    if (enemy) {
        if (hero.enemyInRange(enemy)) {
            hero.cleaveOrAttack(enemy);
        }
    }
}
```

When you have a function calculate a value, use the `return` keyword to end the function and send a value back to the caller:

```javascript
hero.triple = function(a) {
    var b = a + a + a;
    return b;
};

hero.say("3 × 3 = " + triple(3));
hero.say("4 × 3 = " + triple(4));
```

___
