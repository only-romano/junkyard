## _Safe Spot_

#### _Legend says:_
> The safest spot is the point which is equally far from all hazards.

#### _Goals:_
+ _Reach the dungeon entrance_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Geometry**
+ **Return Statements**
+ **Accessing Properties**
+ **For Loops Range**

#### _Solutions:_
+ **[JavaScript](safeSpot.js)**
+ **[Python](safe_spot.py)**

#### _Rewards:_
+ 387 xp
+ 178 gems

#### _Victory words:_
+ _EKED OUT WITH EQUIDISTANCE!_

___

### _HINTS_

Looks like we're surrounded by robobombs. Any sound and they will blow up! You need to find the safe place exactly in the centre of that robocircle.

We know an approximate area where the centre can be. Let's just it a metre by a metre.

If all enemies (points) are placed at the same distance from you, then you are in the centre of the circle. In this level, we're using a brute-force method to find the centre point. Of course, it can be done in a more optimal way.

Don't forget to use `almostEqual` function to compare distance. Because it's hard to compare non-integer numbers. For example, `3.14159265359 != 3.1415926536`. That's why we're using comparing with an inaccuracy.

___
