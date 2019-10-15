## _Passing Through_

#### _Legend says:_
> You've found a village of peaceful ogres. Don't insult them!

#### _Goals:_
+ _Don't insult the peaceful ogres_
+ _Take the gems_
+ _Don't take mushrooms_
+ _Move to the X_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statement**
+ **Nested If Statement**
+ **Accessing Properties**

#### _Items we've got (- or need):_
+ Pet

#### _Solutions:_
+ **[JavaScript](passingThrough.js)**
+ **[Python](passing_through.py)**

#### _Rewards:_
+ 89 xp
+ 49 gems

#### _Victory words:_
+ _NICE VILLAGE YOU HAVE HERE._

___

### _HINTS_

You found a village of peaceful ogres. If you insult them, they will join the hostile ogres!

They will be insulted if you take their food, or if you don't take the gems they offer you.

The sample code shows you how to compare things with `!=`:

```javascript
if(item.type != "gem") {
    // The item is not a "gem".
}
```

This level shows you how to use `!=`.

You know that `==` measn **is equal to**.

`!=` is similar, but it means **is NOT equal to**.

In this case, we've given you the code with `!=`, and what you have to do is write the `else` part of the code, using `moveXY` to move the hero to `item`s `pos.x` and `pos.y` position.

___
