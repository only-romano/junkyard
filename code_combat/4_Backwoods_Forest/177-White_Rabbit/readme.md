## _White Rabbit_

#### _Legend says:_
> You'd better follow the white rabbit. Oh, I wanted to say the lightstone.

#### _Goals:_
+ _Escape from the maze_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Accessing Properties**

#### _Items we've got (- or need):_
+ _Optional: Elemental Codex 1+_

#### _Solutions:_
+ **[JavaScript](whiteRabbit.js)**
+ **[Python](white_rabbit.py "#1 - 7.38s")**

#### _Rewards:_
+ 60 xp
+ 71 gems

#### _Victory words:_
+ _I'M LATE, I'M LATE. FOR A VERY IMPORTANT DATE!_

___

### _HINTS_

The room is full of traps. Don't worry and follow the lightstone. The lightstone is an item and you can find it with the hero's `findNearestItem` method.

Try to collect the lightstone by moving to its position. It is fast but it will guide you to the exit.

Each item has the property `pos` which contains the items position. The object (`pos`) has properties `x` and `y`. Use them to find where you should move.

Each item is an **object**, which is a type of data, like a **string** or a **number**. Objects contain other pieces of data, known as **properties**.

Each item object (and each unit) has a `pos` property, which stands for its position. And each `pos` is itself an object, which has `x` and `y` properties that you can use with `moveXY` and/or `buildXY`.

Also, you can reference `x` and `y` directly without using variables:

```javascript
var item = hero.findNearestItem();
if (item) {
    hero.moveXY(item.pos.x, item.pos.y);
}
```

___
