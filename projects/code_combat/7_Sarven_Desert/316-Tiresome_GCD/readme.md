## _Tiresome GCD_

#### _Legend says:_
> Not all algorithms are equal.

#### _Goals:_
+ _Get into the Treasury_

#### _Topics:_
+ **Basic Syntax**

#### _Solutions:_
+ **[JavaScript](tiresomeGCD.js)**
+ **[Python](tiresome_gcd.py)**

#### _Rewards:_
+ 200 xp
+ 146 gems

#### _Victory words:_
+ _GCD! DON'T MOVE AND DROP YOUR CALCULATOR!_

___

### _HINTS_

The greatest common divisor (`gcd`) of two or more integers, which are not all zero, is the largest positive integer that divides each of the integers.

To get into the Treasury you should say the password. Our spies get two number keys for the password. To find the password you need to find `gcd` of those two numbers.

The simplest, but not fast, way to find gcd is enumerating all possible numbers (from up to down) which are less than given keys. If both keys are dividable of the current number without remainders, then it's gcd.

Maybe there is another way?

___

The naive algorithm for searching `gcd` can be named **brute-force** because we're trying to enumerate all possible answers. If we have two numbers `A` and `B` (`A > B`), then we're taking `B` as a start number and reduce it by one on each cycle. As the result, we need from `1` to `B` cycles. For the current level, it can be `10 ** 15` cycles.

It's not a problem when numbers are small. But what if numbers are huge (Ex.: `2**100`) and we need to find `gcd` for many pairs of numbers (it's a usual task in cryptography)? Even for powerful computers, it can be a problem. Also, it's not a good idea to waste computational resources if we can do it more optimal way.

In the default code, you can see the function `euclidianGCD`. It's an implementation of the Euclidian Algorithm which allows finding `gcd` much faster. The Euclidean algorithm is based on the principle that the greatest common divisor of two numbers does not change if the larger number is replaced by its difference with the smaller number. You aren't necessary to understand that algorithm right now. The main point is to show how various algorithm can solve the same problem different ways with different efficiency.

P.S.: If you want to know more about the Euclidian Algorithm you can read about it in [Wikipedia](https://en.wikipedia.org/wiki/Euclidean_algorithm).

___
