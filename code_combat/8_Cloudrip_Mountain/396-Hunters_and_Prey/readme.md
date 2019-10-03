## _Hunters and Prey_

#### _Legend says:_
> Ogres are hunting your reindeer. Who hunts the hunters?

#### _Goals:_
+ _Your reindeer must survive_
+ _Bonus: All your allies live_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Array Indexes**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](huntersAndPrey.js)**
+ **[Python](hunters_and_prey.py)**

#### _Rewards:_
+ 249-372 xp
+ 116-173 gems

#### _Victory words:_
+ _NO REINDEER WERE HARMED IN THE MAKING OF THIS LEVEL. ALSO, NO SOLDIERS WERE HARMED._

___

### _HINTS_

Command a set of troops efficiently!

Archers should only attack enemies that are closer than `25m`.

Soldiers should attack anyone.

Collect coins using a function.

If your archers move too far away from your reindeer, ogres will ambush the reindeer from the surrounding hills. So, keep the archers back near the reindeer.

In order to do this, you will have to command the archers to `command(archer, "move", archer.pos)` which simply means "stay where you are". You need to do this because the default behavior of your archers, if they haven't received any other commands, is to chase after enemies.

If an enemy is within the archer's attack range (**25 metres**), your archer can safely attack it.

___
