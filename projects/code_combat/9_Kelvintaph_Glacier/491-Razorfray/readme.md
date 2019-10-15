## _Razorfray_

#### _Legend says:_
> Master the art of the trick shot to clear out an icy dungeon without taking a step.

#### _Goals:_
+ _Defeat the ogres_

#### _Topics:_
+ **Basic Syntax**
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Geometry**

#### _Solutions:_
+ **[JavaScript](razorfray.js)**
+ **[Python](razorfray.py)**

#### _Rewards:_
+ 1334 xp
+ 419 gems

#### _Victory words:_
+ _TRICKSHOT? THE TRICK IS TO NOT GET SHOT._

___

### _HINTS_

Arryn's `throwPos` ability lets her target trick shots at arbitrary targets, so you can bounce discs off walls to shoot around corners. Since the enemies in this level are randomized, you can't hard-code the positions to shoot at. It would be pretty difficult to calculate the bounce trajectories to hit each enemy, but luckily, your human brain is great at calculating trajectories, so you can use flags to help out your targeting code!

Use `throwPos` and `removeFlag` together to throw a disc at each flag you place, then remove it, without moving to the flag to pick it up.

I'd watch out and not hit that ice yak if I were you.

___
