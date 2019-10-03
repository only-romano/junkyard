## _Prime Pathing_

#### _Legend says:_
> Navigate your troops through a maze of mines using prime numbers.

#### _Goals:_
+ _You all must reach the end_
+ _Bonus: pass bear traps_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops with Conditionals**
+ **Return Statements**
+ **Accessing Properties**
+ **Vectors**

#### _Solutions:_
+ **[JavaScript](primePathing.js)**
+ **[Python](prime_pathing.py)**

#### _Rewards:_
+ 2206-3309 xp
+ 656-984 gems

#### _Victory words:_
+ _"ALTHOUGH THE PRIME NUMBERS ARE RIGIDLY DETERMINED, THEY SOMEHOW FEEL LIKE EXPERIMENTAL DATA."_

___

### _HINTS_

_"God may not play dice with the universe, but something strange is going on with the prime numbers."_

For this level you need to get all your men through the minefield.  Each mine has been given a `value`, and only the traps with prime number values are safe for passing over.

Prime numbers are those numbers that are not divisible by any number other than 1 and themself. One algorithm to determine whether a number `n` is prime is to iterate over all numbers between 2 and `Math.ceil(Math.sqrt(n))` and see if `n` is divisible by any of them with the modulo operator: does `n % x == 0`?

You'll need to coordinate both your troops and your hero for passing over the dud (prime) traps without accidentally stepping on a live (composite) trap.

If you can get past the fire traps, there's a bonus goal to deal with the bear traps, which have much larger primes on them. You'll want to either write very efficient code for determining whether a bear trap's value is prime, or you'll want to make sure to just do the calculation once for each bear trap and remember the result instead of recalculating it every loop iteration.

___
