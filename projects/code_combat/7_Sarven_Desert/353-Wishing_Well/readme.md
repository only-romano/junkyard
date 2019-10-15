## _Wishing Well_

#### _Legend says:_
> Gather an exact amount of coins from the wishing well!

#### _Goals:_
+ _Collect 104 gold_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **While Loops with Conditionals**
+ **Return Statements**
+ **Algorithm Sum**

#### _Solutions:_
+ **[JavaScript](wishingWell.js)**
+ **[Python](wishing_well.py)**

#### _Rewards:_
+ 256 xp
+ 191 gems

#### _Victory words:_
+ _I WISH, I WISH, I WISH FOR RICHES OF GOLD!_

___

### _HINTS_

You need exactly 104 gold.

Use the `sumCoinValues()` function to get the total value of coins.

If there is not enough gold say `"Non satis"`.

If there is too much gold say `"Nimis"`.

If there is exactly `104` gold, then collect the coins.

_**Hint**: check out the code for `sumCoinValues()` to understand how it works!_

The simplest example of a **summary function** is the calculation of the sum of an array of numbers:

```javascript
function sumNumbers(array) {
    var index = 0;
    var total = 0;
    while (index < array.length) {
        total += array[index];
        index += 1;
    }
}
```

We iterate all elements of the array and add them to the variable `total`.

In this level, we have an array of objects (coins), so we need to calculate the total of each coin's `value` property.

___
