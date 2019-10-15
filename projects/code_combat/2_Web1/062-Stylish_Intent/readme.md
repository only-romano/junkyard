## _Stylish Intent_

#### _Legend says:_
> Begin learning how to style various elements of a webpage.

#### _Goals:_
+ _Change the color of the `<p>` tags_
+ _Center the `<h1>` text_

#### _Topics:_
+ **Basic HTML**
+ **Basic CSS**

#### _Solutions:_
+ **[HTML](Stylish_Intent.html)**

#### _Rewards:_
+ 30  xp
+ 10 gems

#### _Victory words:_
+ _HOW DAPPER._

___

### _HINTS_

Cascading Style Sheets, or CSS, is the web's way of formatting the various parts of a website.

To include special style rules, use the opening and closing `<style>` tag.

**Note: `<style>` is unlike other HTML tags! What you put between the two tags is different from other HTML tags!**

```html
<style>
/* This is the element selector. Use { and } to contain CSS rules */
p {
    /* The attribute name comes first, followed by value it should be set to. */
    color: red;

    /* Be sure to use a : between the name and value. Use a ; at the end! */
}

/* Selector */
div { /* Brackets { } */
    /* Attribute Name : Attribute Value ; */
    text-align: center;

    /* Note the : and ; */
}

img {
    width: 100px;
    height: 200px;
}
</style>
```

___

The `<style>` tag can be used to style how the various elements behave.

It follows a special set of rules.

The `<style>` tag is for containing CSS rules, or Cascading **Style** Sheet rules. Place all of your webpages styles here. Styles make text different colors and sizes.  Styles can change the location of HTML elements and even hide them. Styles change how content looks on a webpage.  HTML changes what content there is on the webpage.

**Example:**

```html
<style>
    p {
        color: red
    }
</style>
```

___
