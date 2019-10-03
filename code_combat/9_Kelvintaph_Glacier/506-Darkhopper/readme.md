## _Darkhopper_

#### _Legend says:_
> I know a short cut... Through another plane.

#### _Goals:_
+ _Collect 10 gems_

#### _Topics:_
+ **Reading the Docs**

#### _Solutions:_
+ **[JavaScript](darkhopper.js)**
+ **[Python](darkhopper.py)**

#### _Rewards:_
+ 999 xp
+ 333 gems

#### _Victory words:_
+ _IF YOU CAN'T USE MAGIC YOU CAN BUY D-HOPPER._

___

### _HINTS_

One of Ritic's abilities allows him teleport in close range instantly. Use it to collect gems in the minefield and evade catapult fire.

```javascript
if (hero.isReady("blink")) {
    hero.blink(enemy.pos);
}
```

The `blink` method takes one argument `position`. It can be an item/unit position, a vector or an object with properties `x` and `y`:

```javascript
hero.blink(item.pos);
hero.blink(Vector(19, 19));
hero.blink({x: 42, y: 42});
```

`blinc` can't teleport you in place which you can't see (it doesn't work even with the Twilight Glasses).

___
