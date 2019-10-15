## _Chameleons_

#### _Legend says:_
> Those ogres are masters of camouflage.

#### _Goals:_
+ _Find and Defeat ogres_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Accessing Properties**

#### _Items we've got (- or need):_
+ _Optional: Elemental codex 1+_
+ _Optional: Emperor's gloves_

#### _Solutions:_
+ **[JavaScript](chameleons.js)**
+ **[Python](chameleons.py "Top-5 - 8.5s")**

#### _Rewards:_
+ 60 xp
+ 71 gems

#### _Victory words:_
+ _KARMA, KARMA, KARMA, KARMA CHAMELEON._

___

### _HINTS_

Ogres are hiding in this room. They can disguise as gems or coins. To find disguised ogres, you need to move really close to an item.

Collect all items and defend yourself from ogres when you see them. Use the nearest item's `pos`, `x` and `y` to find where to move.

Remember items have **objects** and they have **properties** like `pos`. In fact, `pos` is also an **object** and contains another 2 **properties** like `x` and `y`.

For example, if you wanted to find a friend's hair length and color:

```javascript
var friend = hero.findNearestFriend();

if (friend) {
    var hair = friend.hair;  // Access the friend's hair property
    var hairLength = hair.size;  // Access the hair property's size property
    var hairColor = hair.color;  // Access the hair property's color property
    hero.say("You have " + hairLength + " " + hairColor + " colored hair!");
}
```

Use this to move to the various coins's X and Y positions!

___
