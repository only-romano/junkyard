## _Basin Stampede_

#### _Legend says:_
> Something spooked the Yaks! Run, run for your life!

#### _Goals:_
+ _Get to the oasis._

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **If/Else Statements**
+ **Nested If Statements**
+ **Accessing Properties**


#### _Solutions:_
+ **[JavaScript](basinStampede.js)** _warrior_
+ **[Python](basin_stampede.py)** _wizard_

#### _Rewards:_
+ 146 xp
+ 131 gems

#### _Victory words:_
+ _THAT WAS A CLOSE ONE! THAT ONE, TOO! WHEW, TOO MANY CLOSE CALLS._

___

### _HINTS_

Uh oh, a stampede! Dynamically dodge those dastardly yaks!

There are some simple rules for surviving a yak stampede:

1. Keep moving to the right! The sample code gives you this part: `hero.pos.x + 5`
2. Subtract `3` from y if the yaks are above the hero (`enemy.pos.y > hero.pos.y`)
3. Add `3` to y if the yaks are below the hero (`enemy.pos.y < hero.pos.y`)

Remember that `y` controls how far up or down a unit is on the game map.

Lower numbers are further down. Higher numbers are further up.

So if `enemy.pos.y` is greater than `hero.pos.y`, that enemy is **ABOVE** the hero.

In this case, that means the hero needs to move **DOWN** to escape the enemy, by subtracting from `yPos`

If `enemy.pos.y` is less than `hero.pos.y`, that enemy is **BELOW** the hero. So the hero would add to `yPos` to escape by moving **UP**.

___
