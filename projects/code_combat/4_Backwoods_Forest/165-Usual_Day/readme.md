## _Usual Day_

#### _Legend says:_
> Ogres, coins, booleans... I've seen it a hundred times. Let's make it shorter at least.

#### _Goals:_
+ _Defeat the ogres_
+ _Collect 3 coins_
+ _Under 8 statements_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statement**
+ **Accessing Properties**
+ **Boolean Equality**

#### _Items we've got (- or need):_
+ Weapon

#### _Solutions:_
+ **[JavaScript](usualDay.js)**
+ **[Python](usual_day.py)**

#### _Rewards:_
+ 69 xp
+ 79 gems

#### _Victory words:_
+ _SLEEPWALKING OGRE MUSHROOMS. NOW THAT'S AN UNUSUAL DAY!_

___

### _HINTS_

When using the AND operator, if the first condition (on the left of the AND) is false, the second condition (on the right) will never have to execute.

You can use this to your advantage!

This code may have an error:

```python
enemy = hero.findNearestEnemy()
# Trying to get enemy.type is an error if enemy is None!
if enemy.type == "munchkin":
    hero.attack(enemy)
```

This code with AND will not cause an error:

```python
enemy = hero.findNearestEnemy()
# If enemy is None, the AND is False
# So enemy.type will not be executed, and won't cause an error.
if enemy and enemy.type == "munchkin":
    hero.attack(enemy)
```

___
