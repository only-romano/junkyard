## _Canyon of Storms_

#### _Legend says:_
> Observe the wild animals. They know and feel the Nature better than you.

#### _Goals:_
+ _Collect gold until storm_
+ _Return to the cave_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Variables**
+ **While Loops with Conditionals**
+ **If Statements**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](canyonOfStorms.js)**
+ **[Python](canyon_of_storms.py)**

#### _Rewards:_
+ 197 xp
+ 164 gems

#### _Victory words:_
+ _THE STATIC OF A STORM STANDS YAK HAIR STRAIGHT UP!_

___

### _HINTS_

A storm is coming, but you still have a little time to collect coins before it arrives. Observe the sand yaks, they know when a storm starts.

You can use a variable as a condition for a `while`-loop, just be sure to update it inside the loop!

```javascript
// Initialize the condition:
var yak = hero.findNearestEnemy();
while(yak) {
    // Do stuff...

    // Update the loop condition:
    yak = hero.findNearestEnemy();
}
```

Just like we use `enemy` as the condition for an `if` statement to determine the existence of an enemy:

```javascript
var enemy = hero.findNearestEnemy();
if (enemy) {
    hero.attack(enemy);
}
```

We can also use `enemy` (or `yak`, in this level) as the condition for a `while` loop:

```javascript
var enemy = hero.findNearestEnemy();
while(enemy) {
    // Do something while there is an enemy
    // Be shure to update enemy inside the loop!
    enemy = hero.findNearestEnemy();
}
```

___
