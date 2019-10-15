## _Shine Getter_

#### _Legend says:_
> Filter only gold coins to get the most money in a short time.

#### _Goals:_
+ _Collect 100 gold_

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **While Loops with Conditionals**
+ **Accessing Properties**
+ **Array Indexes**
+ **Array Length**

#### _Solutions:_
+ **[JavaScript](shineGetter.js)**
+ **[Python](shine_getter.py)**

#### _Rewards:_
+ 311 xp
+ 230 gems

#### _Victory words:_
+ _DON'T YOU JUST LOVE PICKING UP SHINY THINGS? YES, YES YOU DO._

___

### _HINTS_

![](img/shine_getter.jpeg)

Use `while` to loop over an array of coins with `findItems()`.

```javascript
var coins = hero.findItems();
var coinIndex = 0;

while(coinIndex < coins.length) {
    var coin = coins[coinIndex];
    hero.moveXY(coin.pos.x, coin.pos.y);
    coinIndex += 1;
}
```

This time you'll use a `while` loop to loop over items instead of enemies, to find the gold coins.

As you can see in the sample code, the `value` property of the coin can be used to determine what kind of coin it is.

Gold coins have a `value` of `3`.

Use `moveXY` to pick up only the gold coins by moving to their `pos.x` and `pos.y`.

___
