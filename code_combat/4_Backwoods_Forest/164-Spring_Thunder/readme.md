## _Spring Thunder_

#### _Legend says:_
> I love thunderstorms. The rain and lightning cleans the land and reveals shiny things.

#### _Goals:_
+ _Collect 3 coins_
+ _Collect 3 gems_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statement**
+ **Accessing Properties**
+ **Boolean Equality**

#### _Items we've got (- or need):_
+ Weapon

#### _Solutions:_
+ **[JavaScript](springThunder.js)**
+ **[Python](spring_thunder.py)**

#### _Rewards:_
+ 69 xp
+ 79 gems

#### _Victory words:_
+ _DOESN'T EVERYONE LIKE GETTING CAUGHT IN THE RAIN?_

___

### _HINTS_

Treasure collecting is a dangerous work when it's a thunderstorm outside. Some gems and coins attract lightning - you'll want to avoid those!

Use an AND operator to determine if an item is safe to pick up.

```javascript
var item = hero.findNearestItem();
if(item.type == "coin" && item.value == 2) {
    hero.moveXY(item.pos.x, item.pos.y);
}
```

`A AND B` is true only if both A and B are true.

___

This level introduces the concept of the boolean `and`.

Placing an `and` between two boolean values will return a single boolean value, much like `*` takes 2 numbers and spits out an another number (in this case, the multiplication).

Remember that booleans are a single bit of data, `true` or `false`.

`and` returns `true` if both the value before and after is `true`, or `false` if one (or both) of them is `false`.

```javascript
// Write oolean 'and' using '&&'
hero.say(false && false)  // Hero says 'false'
hero.say(false && true)  // Hero says 'false'
hero.say(true && false)  // Hero says 'false'
hero.say(true && true)  // Hero says 'true'
```

Recall that `<`, `>`, `<=`, `>=`, `==` return boolean values, so to make this more useful:

```javascript
var item = hero.findNearestItem();
// It helps to read it out loud:
if (hero.distanceTo(item) < 15 && item.type == "potion") {
    // If distanceTo the item is less than 15, AND, item's type is a potion
    hero.moveXY(item.pos.x, item.pos.y);
}
```

___
