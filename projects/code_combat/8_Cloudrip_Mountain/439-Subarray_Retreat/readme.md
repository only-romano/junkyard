## _Subarray Retreat_

#### _Legend says:_
> You would not believe but gems can be negative

#### _Goals:_
+ _Escape from the Valley_

#### _Topics:_
+ **Basic Syntax**

#### _Solutions:_
+ **[JavaScript](subrayRetreat.js)**
+ **[Python](subarray_retreat.py)**

#### _Rewards:_
+ 500 xp
+ 200 gems

#### _Victory words:_
+ _THE SUBARRAY OF AN ARRAY IS STILL AN ARRAY._

___

### _HINTS_

It's a weird place with weird gems. Some of them have a negative value. To escape from ogres you should find a sequence of gems with the maximum possible sum.

There are two ways: naive/slow and smart/fast. You can see two methods to solve the problem in the sample code. Just use the fast one.

As you can see the naive solution iterate through an array for each start element. So the time is propotional to `N * N` where `N` is the length of the array. It's not a problem for small arrays, but when `N` grows the solution time grows much faster. For example:

```
19 elements -> 190 cycles
100 elements -> 5050 cycles
1000 elements -> 505000 cycles
10 ^ 32 elements -> about 5 * 10 ^ 63
```

However, smart algorithms can help and solve that problem in linear time. For `N` elements it takes `N` cycles. Much better. That solution uses `dynamical programming`. It's not neccessary to understand that algorithm now, howeer you can read about it on Wikipedia.

___
