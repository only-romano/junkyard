## _Toggulation_

#### _Legend says:_
> Toggle classes, on and off, to create improve interactability in the page!

#### _Goals:_
+ _Toggle class `"expand"` on `h1`_
+ _Click the `h1`_
+ _Click the `img`_

#### _Topics:_
+ None

#### _Solutions:_
+ **[HTML](Toggulation.html)**

#### _Rewards:_
+ 60  xp
+ 20 gems

#### _Victory words:_
+ _TOGGLED, ON, OFF, ON, OFF._

___

### _HINTS_

`toggleClass()` will add or remove a class depending if an element already has that class on it.

If it has the class on it, it will remove it.

if it doesn't have the class on it, it will add it.

**Example:**

```html
<div id="mainElement" class="strike">
    I contain information!
</div>
<style>
    .strike {
        text-decoration: line-through;
    }
</style>
<script>
    // Remove the "strike" class to the mainElement div.
    var target = $("#mainElement");
    target.toggleClass("strike");
</script>
```

**Required Parameters:**
+ `className`: `string` (ex. `"selected"`). _A string of a CSS class name._

The `toggleClass()` is used to turn specific classes on and off. Think of it as a light switch. It either adds (on) the class, or it removes (off) the class, depending if the state before was (off) or (on).

This is good for certain types of selectors, such as checklists or giant pug faces.

___
