## _Behind the Darkness_

#### _Legend says:_
> Embrace the Darkness.

#### _Goals:_
+ _Survive 70 seconds_

#### _Topics:_
+ **Basic Syntax**

#### _Solutions:_
+ **[JavaScript](darkness.js)**
+ **[Python](darkness.py)**

#### _Rewards:_
+ 999 xp
+ 333 gems

#### _Victory words:_
+ _IF YOU CAN'T USE MAGIC YOU CAN BUY D-HOPPER._

___

### _HINTS_

The Wall of Darkness can protect you from projectiles, also it can slow units who try to pass it. Use the wall to survive against the ogre hordes.

P.S.: Yetis don't like darkness.

The Wall of Darkness is not an ordinary ability. The time to summon the wall depends on the length of the wall. Each element of the wall requires 0.125 seconds, so if you want the looong wall you need to wait.

The wall can contain as many segments as you want, but remember each segment takes time to cast. You define points and the wall is built between them in the order. Points can be objects or vectors.

```javascript
hero.wallOfDarkness([Vector(1, 1), {x: 20, y: 20}, hero.pos]);
```

___
