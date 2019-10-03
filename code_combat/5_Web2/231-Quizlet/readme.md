## _Quizlet_

#### _Legend says:_
> Create a quiz of questions and group them using pseudo-psychological methods!

#### _Goals:_
+ _Change he quiz title's `<h1>`_
+ _Change he first question's `<h2>`_
+ _Give question #2 4 answers_
+ _Give question #3 4 answers_
+ _Give question #4 4 answers_
+ _Have 5 results with an `<h2>`, `<img>`, and `<p>`_
+ _Have 4 answers with `data-value="A"`_
+ _Have 4 answers with `data-value="B"`_
+ _Have 4 answers with `data-value="C"`_
+ _Have 4 answers with `data-value="D"`_

#### _Topics:_
+ None

#### _Solutions:_
+ **[HTML](Quizlet.html)**
+ **[Result](https://codecombat.com/play/web-dev-level/5d0f593cdee0ea004978cf2a)**

#### _Rewards:_
+ 60 xp
+ 20 gems

#### _Victory words:_
+ _None_

___

### _HINTS_

Make your own personality quiz!

We gave you the layout, and started scripting it for you. Now it's time for you to complete it!

Personality quizzes are useful for figuring out what kind of people your classmates are.

Provide them a question of introspection, and have them answer a series of psychological questions to find out about their very soul.

_What type of Dog are you?_ Is a suitable title, while, **What's your favorite food?** Is a good starter questionю And the following are some example answers:

+ Kibble
+ Steak
+ Vegetables
+ Cowpie

___

##### _Conditional statements in Web_

###### _`if` keyword_

`if` statements are used to control the flow of your program.

`if` statements are used to ask a question (called a `conditional`), and performs an action if the answer is `true`.

To help understand `if` statements, read them out loud:

```javascript
if (element.hasClass("selected")) {
    element.css("background-color", "blue");
}
```

or, in normal language:

```
if element has the "selected" class, set the element's background-color to blue.
```

**Example:**

```html
<script>
    var header = $("#header");
    if(header.css("background-color") == "rgb(255, 0, 0)") {
        header.css("background-color", "blue");
    }
</script>
<style>
    #header {
        background-color: rgb(255, 0, 0);
    }
</style>
<div id="header">
    <h1>Welcome!</h1>
</div>
```

###### _`else if` keyword_

`else if` statements perform an action only if the previous `if` and `else if` statements were `false` and then own `conditional` is `true`.

`else if` statements have their own question `conditional` that they ask.

To help understand `if` statements, read them out loud:

```javascript
if(element.hasClass("muted")) {
    // Code in here only runs if the element has the class "muted".
}
else if (element.hasClass("selected")) {
    // Code in here only runs if:
    // element DOESN'T have the class "muted".
    // The element DOES have the class "selected".
}
```

**Example:**

```html
<script>
    var elements = $(".helper");
    function hideNope() {
        var target = $(this);
        if(target.text() == "Yep.") {
            target.show();
        } else if (target.text() == "Nope.") {
            target.hide();
        }
    }
    elements.on("click",hideNope);
</script>
<style>
    .helper {
        width:64px;
        height:64px;
        background-color:blue;
    }
</style>
<div class="helper">
    Nope.
</div>
<div class="helper">
    Yep.
</div>
```

###### _`else` keyword_

`else` statements perform an action only if **all** previous `if` and `else if` statements were `false`.

They do **not** have their own `conditional`.

```javascript
if(element.hasClass("muted")) {
    // This code only runs if element has the class "muted".
}
else if (element.hasClass("selected")) {
    // This code only runs if:
    // The element doesn't have the class "muted".
    // The element has the class "selected".
}
else {
    //This code only runs if all of the above are false
}
```

**Example:**

```html
<script>
    var elements = $(".helper");
    function hideNope() {
        var target = $(this);
        if(target.text() == "Yep.") {
            target.show();
        } else if (target.text() == "Nope.") {
            target.hide();
        } else {
            target.addClass("nahFound")
        }
    }
    elements.on("click",hideNope);
</script>
<style>
    .helper {
        background-color:blue;
    }
    .nahFound {
        font-size:large;
    }
</style>
<div class="helper">Nope.</div>
<div class="helper">Yep.</div>
<div class="helper">Nah.</div>
```

___
