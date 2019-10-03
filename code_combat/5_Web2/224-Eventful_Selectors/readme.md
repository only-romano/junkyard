## _Eventful Selectors_

#### _Legend says:_
> Use a single event listener to act on multiple elements.

#### _Goals:_
+ _Bold one of the `h2`s_
+ _Strike-through at least 3 list items_

#### _Topics:_
+ None

#### _Solutions:_
+ **[HTML](Eventful_Selectors.html)**

#### _Rewards:_
+ 60  xp
+ 20 gems

#### _Victory words:_
+ _THIS IS SOME POWERFUL CODE!_

___

### _HINTS_

When an event function is called, it adds a variabled called `this`.

When used with the jQuery object, it selects the specific element that it was called on.

`this` is a special keyword in JavaScript. Inside of the jQuery function, `$` it selects an event function's specific target.

`$(this)` is a very powerful tool when using events!


```javascript
function hideClicked() {
    var element = $(this);  // This is the specific <li>
    element.hide();  // This hides the specific <li>
}

var listItem = $("li");
listItem.on("click", hideClicked);
```

___
