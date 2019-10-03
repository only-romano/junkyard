## _Brewball_

#### _Legend says:_
> Also known as "Hand-Potion-Throw-Game-in-a-Minefield". You can see why Brewball is the more popular name.

#### _Goals:_
+ _Catch 3 potions_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Array Indexes**
+ **Vectors**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](brewball.js)**
+ **[Python](brewball.py)**

#### _Rewards:_
+ 1685 xp
+ 439 gems

#### _Victory words:_
+ _NOW YOU SEE WHY IT'S THE NEXT BIG SPORT!_

___

### _HINTS_

#### Welcome to Brewball!

Can you path through the mines and grab the potion safely before it lands?

One wrong step, **KABLOOIE**.

One failed catch, **KABLOOIE**.

There are multiple ways to solve this problem. Consider the following:

#### Dynamic Mine Avoidance (Magnets!)

Make a run for it! But as you move towards the _Explosive Potion_, be sure to check how close the **nearest** _Fire Trap_ is. If it's too close, you'll want to adjust your path **away** from the trap. Ensure, however, that every movement is _towards_ the potion, or you won't get to it in time!

#### Evaluate a Path (Pathfinding!)

Do all the hard computations in advance. As soon as you detect an _Explosive Potion_, begin setting a route through the field. Since the traps are randomly placed, you'll need to create an avoidance algorithm to navigate the trecherous terrain.

___
