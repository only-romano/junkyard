## _Fence Builder_

#### _Legend says:_
> Cloudrip Mountain is a dangerous place. It's better to have a fence.

#### _Goals:_
+ _Build the fence_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Geometry**
+ **For Loops**
+ **For Loops Range**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](fenceBuilder.js)**
+ **[Python](fence_builder.py)**

#### _Rewards:_
+ 387 xp
+ 178 gems

#### _Victory words:_
+ _SUCH A LOVELY FENCE, HOW MUCH DID YOU BILL THEM?_

___

### _HINTS_

Help build a fence wall around the farm. The peasant will tell you the coordinates of the opposite corners.

So grab a hammer and build some `"fence"`.

Coordinates of opposite corners are enough to describe a rectangle if its sides are parallel to the X and Y-axises. You can build the sides in any order, but it's faster if you build them in a clockwise (or counter clockwise) order. If you build the fence wall in this way you will need to use a negative step in `for-range`.

```javascript
for (var x = mostRight; x >= mostLeft; x -= step) {
    hero.buildXY("fence", x, y);
}
```

___
