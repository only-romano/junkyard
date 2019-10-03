## _Diamond Dozen_

#### _Legend says:_
> Gather coins efficientally while defeating troupes of ogres in the blazing desert.

#### _Goals:_
+ _Collect the optimal amount of coins_

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **While Loops with Conditionals**
+ **Return Statements**
+ **Accessing Properties**
+ **Array Length**

#### _Solutions:_
+ **[JavaScript](diamondDozen.js)**
+ **[Python](diamond_dozen.py)**

#### _Rewards:_
+ 256 xp
+ 191 gems

#### _Victory words:_
+ _VICTORIES LIKE THAT AREN'T A DIME A DOZEN!_

___

### _HINTS_

Sometimes collecting the closest coin isn't the same as collecting the best coin.

We have given you a function called `valueOverDistance()`.

Use that to find the optimal coin to collect, before they disappear!

In this level you'll be required to write a maximum finding function. Specifically you'll want to recall the function to find an optimal coin out of a set of coins. To help visualize this, consider the following coins:

```
coinA
    value = 3
    distance = 2

coinB
    value = 1
    distance = 1

coinC
    value = 2
    distance = 3
```

If we applied the formula of `value / distance` we can see which coin is the best:

```
coinA
    3 / 2 = 1.5

coinB
    1 / 1 = 1

coinC
    2 / 3 = ~0.66
```

So, we can see the best coin to go for is coinA.

___
