## _Teleport Lasso_

#### _Legend says:_
> Why should we search for ogres if we can teleport them here?

#### _Goals:_
+ _Defeat at least 4 ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Accessing Properties**
+ **Boolean Greater/Less**

#### _Items we've got (- or need):_
+ Weapon
+ **Do not use Ring of Speed**

#### _Solutions:_
+ **[JavaScript](teleport.js)**
+ **[Python](teleport.py)**

#### _Rewards:_
+ 69 xp
+ 79 gems

#### _Victory words:_
+ _TELEPORTATION IS SERIOUS BUSINESS. A SUPER PROFITABLE BUSINESS._

___

### _HINTS_

The ogre army is strong, so we are going to teleport them here, one by one. The teleportation isn't stable, so ogres appear for a short time. If you attack an ogre, you will make it stable.

Attack only weak ogres - `"munchkin"`s, and only if they're closer than 20 meters.

Use an AND operator to make sure both of these conditions are true!

The operator `and` (`&&` in JS) takes two boolean operands and return `true` only if both operands are `true`:

```javascript
// If item's type is "coin" AND its value is 2
if (item.type == "coin" && item.value == 2) {
    // Do something
}
```

In this level, attack an ogre if its `type` is `"munchkin"` AND the distance to it is **less than 20 metres**.

___
