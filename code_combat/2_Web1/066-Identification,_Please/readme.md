## _Identification, Please_

#### _Legend says:_
> Identify and control specific elements on the page.

#### _Goals:_
+ _Change the `text-align` of `#element2`_
+ _Change the `background-color` of `#element3`_

#### _Topics:_
+ **Basic HTML**
+ **Basic CSS**

#### _Solutions:_
+ **[HTML](Identification,_Please.html)**

#### _Rewards:_
+ 30  xp
+ 10 gems

#### _Victory words:_
+ _THIS ALL CHECKS OUT, GOOD JOB!_

___

### _HINTS_

The alternative to the CSS `class` is `id`. `id` attributes mark elements with a specific name to recall later. While a `class` can be repeated across multiple elements, and `id` is for **one** specific element. Think of it as an piece of identification like a school ID or driver's license.

```html
<style>
    #main {
        color: orange;
    }
</style>

<div id="main">
    There can only by one!
</div>
```

The `id` attribute is to assign a unique **identifier** to an element. This makes it easier to target inside your style.

```html
<style>
    /* This sets the element with id 'main' to a red background color. */

    #main {
        background-color: red;
    }
</style>

<!-- Notice the id attribute! -->
<div id="main">
    Hello, world!
</div>
```

___
