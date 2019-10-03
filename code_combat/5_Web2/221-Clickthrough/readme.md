## _Clickthrough_

#### _Legend says:_
> Interactive elements are a staple of the web!

#### _Goals:_
+ _Change the button's background using JavaScript_
+ _Click the button_

#### _Topics:_
+ None

#### _Solutions:_
+ **[HTML](Clickthrough.html)**

#### _Rewards:_
+ 60  xp
+ 20 gems

#### _Victory words:_
+ _NOW YOU'RE THINKING WITH EVENTS!_

___

### _HINTS_

You can bind events to certain elements using the `.on()` function.

```javascript
element.on("click", functionName);
```

The `function` keyword is for defining custom user-functions. `functions` are important in web development, as most events require a `callback` function, or, a `function` that is called back-to when the event occurs.

`function`s don't run on their own and must be called first!

**Example:**

```html
<script>
    function hideElement() {
        $(this).hide();
    }
    $(".hideMe").on("click", hideElement);
</script>
<div class="hideMe">
    <img src="http://direct.codecombat.com/file/db/thang.type/566a2202e132c81f00f38c81/portrait.png"/>
</div>
<div class="hideMe">
    <img src="http://direct.codecombat.com/file/db/thang.type/5432f9d18364d30000d1f943/portrait.png"/>
</div>
<div class="hideMe">
    <img src="http://direct.codecombat.com/file/db/thang.type/5744e3683af6bf590cd27371/portrait.png"/>
</div>
```

___

#### _Events_

Events are things that can happen during use of your website. A button gets `"click"`ed on the `"mousemove"`s over an image.

It is possible to "hook" into these events with an `eventListener`. jQuery comes with a suite of tools to make it easier, but the easiest is the `on()` function.

For any element, `on()` will listen for a specific event to happen, and then call it's desingated `callback` function.

The structure of `on()` is simple, `on(eventName, functionName)`. `eventName` is a string of the event you want to listen to. Examples are: `"click"`, or `"mousemove"`, or `"keydown"`. The `functionName` is the name of a function you've created.

```javascript
var button = $("#theButton");

function thiIsFunction() {
    // Code in here will only be performed when the button is clicked.
}

button.on("click", thiIsFunction);
```

Note that the second argument, the `functionName` doesn't have it's own `()`. This is because at that moment you are not `calling` the function. It is simply informing the `on()` function of what function it should call when the time is right.

___
