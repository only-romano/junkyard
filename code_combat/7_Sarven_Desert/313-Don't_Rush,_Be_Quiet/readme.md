## _Don't Rush, Be Quiet_

#### _Legend says:_
> Move slowly and strangely to avoid the cannon firestorm.

#### _Goals:_
+ _Collect 8 gems_

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **If/Else Statements**
+ **Functions**
+ **Return Statements**

#### _Solutions:_
+ **[JavaScript](dontRush.js)**
+ **[Python](dont_rush.py)**

#### _Rewards:_
+ 238 xp
+ 189 gems

#### _Victory words:_
+ _SSSH-TEADILY SSSH-UCCESSFUL!_

___

### _HINTS_

![](img/rush.jpg)

You need to collect 8 gems in Death Valley. Named as such because of the cannons ready to wipe out anyone who tries to get the gems.

However, the cannons are only prepared for quick thieves, so it's possible to trick them if you move slowly.

The first function returns a value from `0` to `30` (0 <= N < 30). The second function should return a value from `0` to `40` (0 <= N < 40).

Complete it, and the gems are yours.

The `modulo` operation returns the remainder after division of one number by another. The `modulo` function must return a value from `0` to `x`, where `x` is modulo operand. For the current level, it's enough to use the shortened version of it.

While input argument (`n`) is less than the `x` it returns the input number. But when `n` is greater or equal to the `x` it must reduce the input number by `x`.

The second function `mod40` must return a value from 0 to 40. In the sample code, it works only until `n < 40`. But when `n >= 40` it returns a wrong value. To complete the function you need to check an input value if it's greater or equal than 40 -- `if (n >= 40)`. If it's true, then substract 40 -- `n = n - 40`.

Be careful, and don't change the code under `while`.

___
