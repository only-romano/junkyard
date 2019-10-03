## _Steelclaw Gap_

#### _Legend says:_
> Surrounded by enemies in Steelclaw Gap, the remainder of your troops defend a makeshift palisade.

#### _Goals:_
+ _Summon 16 units_
+ _Humans and palisade must survive for 30 seconds_
+ _Bonus: Humans and palisade must survive for 60 seconds_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Array Length**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](steelclawGap.js)**
+ **[Python](steeclaw_gap.py)**

#### _Rewards:_
+ 255-380 xp
+ 117-175 gems

#### _Victory words:_
+ _YOU'VE ESCAPED THE STEELCLAW GAP TRAP. STEELCLAW GAP IS NAMED AFTER TARWIN STEELCLAW, WHO FIRST CROSSED IT._

___

### _HINTS_

Use the modulo operator (`%`) to send two units to each guard point.

You need to summon 8 units and move to 4 points, so `unitIndex % 4` is the requried `defendIndex`.

___

The `%` operator is known as the modulo operator.

`a % b` gives you the remainder (as an integer) of `a / b`. So `12 % 5 == 2`.

This can be used to wrap around an array, for example:

Using the array `summonTypes = ["soldier", "archer", "peasant", "paladin"]` with `type = summonTypes[ i % summonTypes.length ]`:
`0 % 4 == 0` so `type == "soldier"`
`1 % 4 == 1` so `type == "archer"`
`2 % 4 == 2` so `type == "peasant"`
`3 % 4 == 3` so `type == "paladin"`
`4 % 4 == 0` so `type == "soldier"`
`5 % 4 == 1` so `type == "archer"`
etc...

___
