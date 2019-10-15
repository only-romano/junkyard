## _Transformative Properties_

#### _Legend says:_
> Rotate, scale, or move elements using transform!

#### _Goals:_
+ _Give `#imgE` a transform_
+ _Give `#imgF` a transform_
+ _Give `#imgG` a transform_
+ _Give `#imgH` a transform_

#### _Topics:_
+ None

##### _Solutions:_
+ **[HTML](Transformative_Properties.html)**

#### _Rewards:_
+ 60  xp
+ 20 gems

#### _Victory words:_
+ _HOW MAJESTIC!_

___

### _HINTS_

The `transform` property is a modifier on the position, size, and rotation.

**Example:**

```html
<style>
    img {
        transform: rotate(45deg) scale(2) translateX(10px);
    }
</style>
```

The `transform` CSS property applies certain methods to the layout of elements. Use it to twist and turn your elements in unique ways!

`transform` is used to apply unique effects on your elements.

```css
img {
    transform: rotate(180deg) scale(3) translateX(-20px);
}
```

###### _Rotate_

`rotate` rotates an element by a certain amount. It requires a unit of type `deg` (which means **degrees**)

```css
img {
    transform: rotate(-40deg);
}
```

###### _Translate_

`translateX` and `translateY` moves an element left/right or up/down.

```css
img {
    transform: translateY(-180px);
}
```

###### _Scale_

`scale` can make an element bigger (if the number is > 1) or smaller (if the number < 1)

```css
img {
    transform: scale(0.25);
}
```

___
