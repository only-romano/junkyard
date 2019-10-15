## _Query Confirmed_

#### _Legend says:_
> Get introduced to the basics of the web's most popular library: jQuery.

#### _Goals:_
+ _Change the image's width_

#### _Topics:_
+ **Basic HTML**
+ **Basic CSS**
+ **Basic Web Scripting**

#### _Solutions:_
+ **[HTML](query_confirmed.html)**

#### _Rewards:_
+ 60  xp
+ 20 gems

#### _Victory words:_
+ _THE WONDERS OF WEB SCRIPTING!_

___

### _HINTS_

Change the size of the image, using the `css()` jQuery function.

```javascript
var image = $("#theImage");  // Selects the element with id "theImage"
image.css("background-color", "red");  // Sets the image's background color to red
```

___

#### _jQuery_

CodeCombat Web Development uses **jQuery** to make web-based JavaScript easier. **jQuery** introduces 2 new functions: `jQuery()` and `$()`. They both do the exact same thing, but the `$()` was added to simplify things. `$` is no different from `enemy` or `moveLeft` to JavaScript! CodeCombat uses the `$()` because it is easier to type, and is iconic for the _jQuery_ library.


> `$` is a function, so remember to call it using parenthesis `(` and `)`. The most common `argument` to pass in is a `"string"`. Specifically, `$()` is expecting a CSS-style _selector_.

```javascript
var image = $("#theImage");

// The "image" variable is now set to a special jQuery object.
// "image" now has a lot of useful methods to help with manipulating the element!

// For example, the "css()" function takes a property name and a value and changes that element's CSS!
image.css("background-color", "red");
```

___
