## _Mad Maxer_

#### _Legend says:_
> Write smarter code to chase down faraway enemies.

#### _Goals:_
+ _Defeat ogres and destroy decoys_

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **While Loops with Conditionals**
+ **Accessing Properties**
+ **Array Indexes**
+ **Array Length**

#### _Solutions:_
+ **[JavaScript](madMaxer.js)**
+ **[Python](mad_maxer.py)**

#### _Rewards:_
+ 256 xp
+ 191 gems

#### _Victory words:_
+ _WAY TO MAXIMIZE YOUR POTENTIAL._

___

### _HINTS_

![](img/mad_maxer.jpeg)

Distracting decoys mess up your targeting.

Find the farthest enemies first, as decoys will swarm you.

The farthest enemy is the one with the most `distanceTo`.

The goal here is to target the farthest enemies first, because those are the enemies who will attack you, while the decoys swarm in close.

The sample code shows you how to accomplish this: use a while loop to loop over all the enemies.

Initialize `maxDistance` to 0, so the first enemy in the array will be farther away than that.

Then, for each successive enemy in the array, you compare its distance to the `maxDistance`, and if it's greater, set that as the new `maxDistance`, and store that enemy in the `farthest` variable.

When you've looped through all the enemies, `farthest` will contain the enemy with the greatest distance from you.

Then, use a while loop to attack the farthest target while its health is greater than zero.

___
