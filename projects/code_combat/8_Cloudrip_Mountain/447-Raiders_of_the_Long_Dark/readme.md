## _Raiders of the Long Dark_

#### _Legend says:_
> Help Arryn Stonewall rescue a prisoner from The Long Dark.

#### _Goals:_
+ _Reach the end of the dungeon_
+ _Protect the peasant_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Return Statements**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](raidersLongDark.js)**
+ **[Python](raiders_long_dark.py)**

#### _Rewards:_
+ 393 xp
+ 180 gems

#### _Victory words:_
+ _OGRES. VERY DANGEROUS. YOU GO FIRST._

___

### _HINTS_

Prepare yourself for a challenge!

Guide the Raider Arryn through the long, dark dungeons!

It is your responsibility to protect her back using a lone peasant, so keep your eye out for ogres and write your code carefully.

___

In this level, you control your hero, and the peasant.

#### Hero

The `chooseHeroStrategy` function should return either `"advance"` or `"fight"`.

Return `"advance"` if the hero's distance to the peasant is greater than 15.

Return `"fight"` if there is an enemy close by (within 5 meters).

Return `"advance"` if there are no enemies.

The `heroFight` function deals with your hero attacking nearby enemies. You should try to use something like `bash` to slow the enemy's advance toward the peasant.

The `heroAdvance` function deals with moving your hero. You should try to move to 5 meters behind the peasant (`peasant.pos.x - 5`)

#### Peasant

The `choosePeasantStrategy` function should return `"follow"`, `"build-above"`, or `"build-below"`.

Use `isPathClear` to detect if the spot 10 meters above or below the peasant is clear, and if it is, return `"build-above"` or `"build-below"`, so the peasant will block off the path with a fence.

The `peasantAdvance` function should move the peasant to 5 meters behind Arryn's position. (`arryn.pos.x - 5`)

The `peasantBuild` function takes two arguments: `x` and `y`, and should use `command` to have the peasant build a `"palisade"` at `x` and `y`.

The code inside the `while-true` loop is given to you, and will call the functions you defined above!

___
