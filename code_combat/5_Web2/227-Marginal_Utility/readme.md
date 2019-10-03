## _Marginal Utility_

#### _Legend says:_
> Margins and padding are used to separate content.

#### _Goals:_
+ _Give `<div>` elements a margin_
+ _Give `<div>` elements some padding_

#### _Topics:_
+ None

#### _Solutions:_
+ **[HTML](Marginal_Utility.html)**

#### _Rewards:_
+ 60  xp
+ 20 gems

#### _Victory words:_
+ _YOU'RE PADDING YOUR STATS WITH ALL THESE LEVELS!_

___

### _HINTS_

`margin`s and `padding` is used to create whitespace between other elements, and the edge of elements.

```css
div {
    padding: 30px;
    margin: 30px;
}
```

___

#### _`margin`_

The `margin` property controls the distance between elements.

**Example:**

```html
<style>
    div {
        margin: 20px;
    }
</style>
```

`margin` is used to increase the space between elements. This happens outside the `border` if one exists.

```css
.spacedDivs {
    margin: 300px;
}
```

#### _`padding`_

The `padding` property controls the distance between the edge of the element and the content in the element.

**Example:**

```html
<style>
    div {
        padding: 40px;
    }
</style>
```

`padding` is used to increase the space between the inside of the element and the edge of the element. This happens inside the `border`, if one exists.

```css
.paddedDivs {
    padding: 300px;
}
```

___
