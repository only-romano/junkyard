## _Animania_

#### _Legend says:_
> Animation is about squishing and squashing elements!

#### _Goals:_
+ _Add properties to myAnim's `from`_
+ _Add properties to myAnim's `to`_

#### _Topics:_
+ None

#### _Solutions:_
+ **[HTML](Animania.html)**

#### _Rewards:_
+ 60 xp
+ 20 gems

#### _Victory words:_
+ _NOW THAT'S SOME MANIAC ANIMATION!_

___

### _HINTS_

`animation` and `@keyframe` are used for blending animations together.

```css
img {
    animation: grow 3s infinite;
}

@keyframes grow {
    from {
        background-color: blue;
    }
    to {
        background-color: red;
    }
}
```

___

#### _Animation_

The `animation` CSS property tells the browser how to display an element. It blends CSS properties over a certain amount of time.

```css
img {
    /* In the following example, 10 is the number of times it 
        repeats. */

    animation: keyName 5s 10;
}
```

The `animation` property applies a repeating animation to elements.

**Example:**

```html
<style>
    img {
        animation: grow 2s infinite;
    }
    /* The following keyframes is named 'grow'. */
</style>
```

___

#### _Keyframes_

The `@keyframes` CSS keyword is used to defining a path of CSS properties for the `animate` property to use.

`from` is what the animation should start at.

`to` is what the animation should end up as.

```css
/* keyName can be anything, but, is used again in the CSS
    document when calling 'animate': */

@keyframe keyName {
    /* This animation will start at default size and grow to 
        double size. */

    from {
    }
    to {
        transform: scale(2);
    }
}
```

The `@keyframes` selector creates a set of keyframes for the animation to follow. It is referenced by the animation property.

**Example:**

```html
<style>
    /* The following keyframes is named 'grow'. */
    @keyframes grow {
        from {
            transform: scale(1);
        }
        to {
            transform: scale(2);
        }
    }
</style>
```

___
