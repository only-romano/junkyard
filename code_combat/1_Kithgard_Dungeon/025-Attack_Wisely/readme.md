## _Attack Wisely_

#### _Legend says:_
> Ogres behind every door–which shall you choose? _Created by player **Lai Manh Tuan**._

#### _Goals:_
+ _Defeat any 3 ogres_
+ _Grab all the Gems_
+ _Escape the dungeon_
+ _Bonus: defeat all the ogres (5)_

#### _Topics:_
+ **Basic Sintax**
+ **Arguments**
+ **Strings**
+ **Variables**

#### _Items we've got (- or need):_
+ Simple boots
+ _Optional: Elemental codex 1+_
+ _Optional: Emperor's gloves_

#### _Solutions:_
+ **[JavaScript](attackWisely.js)**
+ **[Python](attack_wisely.py "#2 - 11,13s")**

#### _Rewards:_
+ 24-36 xp
+ 21-31 gems

#### _Victory words:_
+ _YOU CHOSE WISELY! REVENGE IS A DISH BEST SERVED COLD._

___

### _HINTS_

When you move, you only move as far as the next movement square (look for the small tiles on the ground).

If you don't know the name of ogres, you can use the `findNearestEnemy` method from your glasses to store references to the ogres in variables. When you call the `findNearestEnemy` method, you **must store the result in a variable**, like `enemy2` (you can name it whatever you want). The variable will remember what the nearest enemy **was** when you called the `findNearestEnemy` method, so make sure to call it when you see a nearby enemy.

___
