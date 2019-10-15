## Computer Science (Code Combat) & Code Combat API

___


**Table of Contents:**

* [Base](#base)
    + [Strings](#strings)
    + [Variables I](#variables-i)
    + [Variables II](#variables-ii)
    + [Variables III](#variables-iii)
    + [Comments](#comments)
    + [Python Inside](#python-inside)
        - [Methods in Python](#methods-in-python)
        - [Variables in Python](#variables-in-python)
        - [Truthy and Falsy in Python](#truthy-and-falsy-in-python)
        - [If and Else statements in Python](#if-and-else-statements-in-python)
    + [Arrays](#arrays)
    + [Array Indexes](#array-indexes)
    + [Adding to an Array](#adding-to-an-array)

* [True and False](#true-and-false)
    + [Truthy and Falsy](#truthy-and-falsy)
    + [What is Boolean](#what-is-boolean)
    + [Why do we use booleans](#why-do-we-use-booleans)
    + [Important Notes](#important-notes)
    + [Comparison](#comparison)
    + [Comparison Equals](#comparison-equals)
    + [Usage of `not`, `or` and `and`](#usage-of-bool)
    + [Boolean Not Equals](#boolean-not-equals)
    + [Boolean AND](#boolean-and)
    + [Boolean OR](#boolean-or)

* [If and Else](#if-and-else)
    + [If-statements I](#if-statements-i)
    + [If-statements II](#if-statements-ii)
    + [If-statements III](#if-statements-iii)
    + [Nesting](#nesting)
    + [Nested If-Statements](#nested-if-statements)
    + [Compact version](#compact-version)

* [Loops](#loops)
    + [Looping While-True](#looping-while-true)
    + [How To Use while-true Loops](#how-to-use-while-true-loops)
    + [Code Before While](#code-before-while)
    + [While-Conditional Loops](#while-conditional-loops)
    + [Loops Break](#loops-break)
    + [Loops Continue](#loops-continue)
    + [Looping over Items in an Array with While](#looping-over-items-in-an-array-with-while)
    + [Advanced While-loops](#advanced-while-loops)

* [Methods](#methods)
    + [Calling Methods](#calling-methods)
    + [Method Arguments](#method-arguments)
    + [Multiple Arguments](#multiple-arguments)
    + [Functions](#functions)
    + [Defining a Function](#defining-a-function)
    + [Return Statement I](#return-statement-i)
    + [Return Statement II](#return-statement-ii)

* [Code Combat](#code-combat)
    + [Directional Movement](#directional-movement)
    + [Attacking with Strings](#attacking-with-strings)
    + [Finding Nearby Enemies](#finding-nearby-enemies)
    + [Attack Nearby Enemies](#attack-nearby-enemies)
    + [Say and Speaking](#say-and-speaking)
    + [Building Defenses](#building-defenses)
    + [Code Limits](#code-limits)
    + [Events](#events)
    + [Event Handler](#event-handler)
    + [X, Y Coordinates](#x-y-coordinates)
    + [Positions](#positions)
    + [moveXY vs move](#movexy-vs-move)
    + [Game Health](#game-health)
    + [Game Time](#game-time)
    + [Hero Gold](#hero-gold)
    + [Hero Debug](#hero-debug)


___


## Base

___

### _Strings_

A `string` is a piece of **text** information. To tell the computer about a string, surround **text** with `"`.

For example,

```javascript
"Brak";  // This is a string!
"Hello, world";
"soldier";
```

Often times the use of a `string` is as an argument in a **method**.

For example,

```javascript
// The hero's attack method requires a name or unit:
hero.attack("Brak");
// The hero can say things to help debug:
hero.say("Bonjour: blue-marble.");
```

___

### _Variables I_

`variables` are a way of storing information to use over and over.

`variables` are made up a **name** and an `=`. The `=` (**equals**) assigns the variable information to the **name**.

```javascript
// JavaScript must DECLARE variables using var (or let in ES5+)
var boop = "Snoot";
// Read as: create a variable named boop and set it equal to "Snoot"
// Now boop can be used in place of "Snoot" anythere in your code.
```

Further,

```javascript
var enemy1 = "Kratt";  // enemy1 now stores "Kratt"
hero.attack("Kratt");  // Is the same as:
hero.attack(enemy1);   // this!
```

`variables` **names** are **NOT** linked to their content at all! A `variable` can have **ANY name**!

Example:

```javascript
var hello = "Kratt";
var kratt = "Kratt";
var dance = "Kratt";  // hello, kratt and dance all are the same thing!

hero.attack(hello);
hero.attack(kratt);
hero.attack(dance);
```

___

### _Variables II_

`variables` can store more information than just `strings` or **numbers**. They also can store references to things in the world!

The `hero` doesn't know the names to all the munchkins in the dungeon. But, if they can **see** a unit, they can provide a reference to that unit.

**Example:**
```javascript
// Remember JavaScript variables must be DECLARED with var
var target = hero.findNearestEnemy();

// Now they can attack their target:
hero.attack(target);
hero.attack(target);  // All without knowing their name!
```

But don't forget that `variables` can store other information too! Variables can store strings, numbers, boolean(true or false), and many other things.

**As an example:**
```javascript
var theHero = hero;
var aNumber = 2;
var coolString = "cool";
```

___

### _Variables III_

A _variable_ lets you hold on to a value for later. Some of those values are **strings** like names or phrases.

```javascript
var phrase = "This is a phrase";
hero.say(phrase);
```

A _variable_ is a way of holding on to a **value** so you can use it any time. The value of a variable can be a string, a number, or almost anything else.

Use the equals sign (`=`) to _set_ the value of a variable:

```javascript
var phrase = "This is a phrase";
```

Once it's set, you can use the variable anywhere in your code that you would use the value it holds.

```javascript
hero.say(phrase);  // Hero says "This is a phrase"
```

Note that a variable is _not_ a string, so you don't put quotes around it.

___

### _Comments_

Comments are a way for two programmers to communicate with each other. They are even useful for a single programmer to remember what they were doing to resume later!

In CodeCombat, we add comments to help you structure your code and give vital hints. Read them to understand what the objective is and what code you need to write to accomplish it.

In this level you will need to read the comments we provide to find the answer, to escape the prison cell!

Comments are pieces of information put in the code editor to help guide your coding.

It is extremely valuable to read each of the lines of code before jumping in!

We provide you with the instructions inside of levels themselves, just read it line by line!

For example, a level might start like this:

```javascript
// Move Up
// Attack Bob
// Say "I win!"
```

Then it is your job to fill in the blanks:

```javascript
// Move Up
hero.moveUp();
// Attack Bob
hero.attack("Bob");
// Say "I win!"
hero.say("I win!");
```

___

### _Python Inside_

Python is a great programming language! It allows you to work quickly and integrate systems more effectively. It is easy to read and use, and the interactive mode makes it simple to test short sections of code. Python is available under an open-source license.


#### Methods in Python

_They do stuff!_ Methods are the commands you give the computer. Above is an example of calling a **method**. In this case `moveRight`.

Since this is one of Tharin's methods, you use `self` to say that it's your own unit's method you're running, not someone else's. Without it, it's unclear where to find the `moveRight` method.

The parentheses following a method just mean 'run it'. Without them, nothing happens.

A method's **argument** is placed between its parentheses. Arguments specify exactly what the command should do. Here, `say()` tells the hero to say something, and `"Hello!"` tells him what he should say. (It has to be in quotes because it's a text string, and text strings need quotes.)

You separate multiple arguments with commas. In `moveXY(5, 6)`, the `5` is the first argument (the x position), and the `6` is the second argument (the y position). (Numbers don't use quotes.)


#### Variables in Python

_Let's give things nicknames!_

A variable is a simple way to store almost anything! As in the first two lines above, a coder often stores a character or an object as a variable in order to use it easily as an argument for a method. If a coder frequently uses a certain text string, storing it as a variable lessens the amount of effort required to type it all out. The last three lines show examples of variables that represent numerical values. If a number is stored as a variable, that variable can later be used in equations, or simply to keep track of progress.

To create a variable, you type the variable name, an equals sign, then what you want to store. If your variable name has multiple words, you can't put spaces between them, but capitalizing every word but the first will make it easier to read--for example, `lowestHealthFriend` instead of `lowesthealthfriend`. This is usually termed camelCase. Speaking of capitalization, spelling is not the only thing that names a variable--capitalization does, too. For this reason, once you create a variable using one capitalization, you must avoid typing the capitalization differently later in your code. For example, will not work because "enemy" and "Enemy" are not the same. Watch your shift key!


#### Truthy and Falsy in Python

Anything before the colon in the `if` statement must be 'truthy' for the `if` block to happen. If the value is 'falsy', then the `else` block (if there is one) runs instead. There are several falsy values in Python:

```python
None
False     # boolean
0         # integer
0.0       # float
0L        # long integer
0.0+0.0j  # complex
""        # empty string
[]        # empty list
()        # empty tuple
{}        # empty dictionary
```

Everything else is truthy:
+ All objects
+ All arrays that are not empty
+ All numbers that are not 0 (even imaginary numbers!)
+ All strings that are not empty
+ `True` (boolean)


#### If and Else statements in Python

Programming is all about handling various situations automatically. Your main tool for doing different things based on the state of things are `if` and `else`. They look something like this: In this case, everything in the `if` block (everything after the word `if` and before the word `else`) never happens, because 3 will never be greater than 9. So only the lines in the `else` block ever run. 

Notice that the items that you want to happen if the statement is true are indented exactly four spaces in from the `if` statement itself. This is how we let the computer know which statement we want to run only when the statement is in fact true.

Also note the colon after the `if` statements, and the fact that they are absent for the rest of the block. These end the statement and let the computer know that you have completed the “test” you want to perform, and to get ready for the instructions of what to do after the test. 


___

### _Arrays_

**Arrays** are a way of storing lots of information for use in the future! Think of them like a list of variables.

Previously, variables needed to be defined for each item:

```javascript
var enemyName1 = "Borker";
var enemyName2 = "Pally";
var enemyName3 = "Cindy";
```

But with an **array**, a single variable can hold multiple **elements**:

```javascript
var enemyNames = ["Borker", "Pally", "Cindy"];
```

Observe the correct way to create an an **array** is to use opening and closing **square-brackets**: `[` and `]` and to separate each **element** with a `comma`: `,`.

To **access** a specific element, use the variable name plus the **square-brackets** with a **number** inside.

_**Important**: **arrays** are `0`-indexed which means the very first element is actually `0`! NOT `1`._

```javascript
var enemyNames = ["Borker", "Pally", "Cindy"];
hero.say(enemyNames[0]);  // The hero says: "Borker"
hero.say(enemyNames[1]);  // The hero says: "Pally"
hero.say(enemyNames[2]);  // The hero says: "Cindy"
```

___

### _Array Indexes_

A variable is a name you can use to store a value.

An array is a name you can use to store a lot of values - like a list of related values.

In an array, each value is stored at a certain **index**.

An **index** is just a number.

So, an array is a numbered list:

0. Chocolate
1. Stroopwafels
2. Cupcakes
3. Ice Cream

You can represent this as an array:

```javascript
var snacks = [];

// The first item is index zero!
snacks[0] = "Chocolate";
snacks[1] = "Stroopwafels";
snacks[2] = "Cupcakes";
snacks[3] = "Ice Cream";
```

___

### _Adding to an Array_

You can add items to the end of an array like this:

```javascript
// Initialize empty array:
var myArray = [];

// Add the string "foo" to the end:
myArray.push("foo");

// myArray is now: ["foo"]

myArray.push("bar");

// myArray is now: ["foo", "bar"]
```

___


## True and False

___

### _Truthy and Falsy_

Anything between (and) after the if must be _truthy_ for the if block to happen. If the value is _falsy_, then the else block (if there is one) runs instead. There are only a few _falsy_ values:

```javascript
undefined
null
0  // Zero
NaN  // A special Number in JavaScript
""  // Empty string
false
```

Everything else is _truthy_:

```javascript
// objects
// arrays
// numbers that are not 0 or NaN
// strings that are not empty
true
```

___

### _What is Boolean_

Boolean describes a type of data, just like String or Number describe different types of data.

A string is text, usually written inside of double quotes, like `"This is a string"`

A boolean is a value that is either  `true` or `false`. It is written slightly differently depending on what programming language you use.

In Python a boolean is either `True` or `False` (with capitalized first letters).

In JavaScript and CoffeeScript, a boolean is either `true` or `false` (no capital letters!).

Whether or not something is considered `true` or `false` is a complicated subject in programming, but for now we will start you off with a simple example.

___

### _Why do we use booleans_

When coding, it's useful to determine if a question is true or false!

One type of question often asked is **EQUALITY**: "Is A equal to B?"

To ask this question in code, we use the **equality operator** which is usually written as `==`.

Think of `==` as meaning _"is equal to?"_. So To ask: "A is equal to? B" you write `A == B`.

___

### _Important Notes_

Remember when we assigned values to a variable using code like:
`enemy = hero.findNearestEnemy()`?

Notice that the **assignment operator** is a single `=`.

The **equality operator** uses two `==`.

Many tears have been shed by programmers trying to find a bug caused by using one `=` instead of two!

Also, note that the **string** `"true"` is not the same thing as the **boolean** `true`, though in this level, the Burl will accept your answer if you say either one. Burls are nice that way.

___

### _Comparison_

Comparisons are expressions that resolve to true or false.

```javascript
if (1 < 10)
```

Because 1 _is_ less than 10, this if statement is true.

Whereas:

```javascript
if (15 < 10)
```

As 15 is _not_ less than 10, this if statement is false.

This becomes very useful in Code Combat for comparing variables with specific numbers and only performing an action when something occurs. For example, it only makes sense to use your "cleave" action  if the enemy is close enough. Otherwise, the cleave does not do damage to your enemy and it is wasted.

```javascript
var distance = hero.distanceTo(enemy);

if (distance < 10) {
    if (hero.isReady("cleave")) {
        hero.cleave(enemy);
    }
}
```

This IF statement will only attempt to cleave an enemy if the distance is less than 10.

There is also >=, which will return true if the number or variable is equal to or greater than the second input.

Whereas:

```javascript
var x = 16;
if (x >= 10)
```

As x  is greater than 10, this statement will resolve to true.

___

### _Comparison Equals_

Use **comparison operators** to compare two values. The result of a comparison will be either True or False.

The first comparison operator we'll use is the **equality operator**. In Python and JavaScript, this is written as: `==`.

Note that this is **two equal-signs together** `==`, as opposed to `=` which is the **assignment operator** used to assign a value to a variable! _Confusing these two is a common mistake by new programmers!_

We use `==` like this:
+ `4 == 4` (this is `true`)
+ `4 == 5` (this is `false`)

We can also combine this with other mathematical operators like `+`:
+ `2 + 2 == 4` (this is `true`)
+ `2 + 2 == 5` (this is `false`)

___

### _Usage of Bool_

> Usage of `not`, `or` and `and`

```python
if 1:
    hero.say("one is here")
elif not 1:  # means that "1" condition is not met
    hero.say("one is not here")
    if 2:
        hero.say("2 is here")

if 1 or 2:  # means that either "1" or "2" conditions have to be met
    hero.say("either of them is here")

if 1 and 2:  # means that both "1" and "2" conditions to be met
    hero.say("both of them are here")
```

___

### _Boolean Not Equals_

The sympol `!=` MEANS **is NOT EQUAL to**.

It is the opposite of `==` which means **is EQUAL to**.

For example, if you wanted to attack all the enemies, except for the `"burl"`s you could use `!=`:

```javascript
var enemy = hero.findNearestEnemy;
if (enemy) {
    if (enemy.type != "burl") {
        hero.attack(enemy);
    }
}
```

In this example,
`enemy.type != "burl"` is **TRUE** if `enemy.type` is `"munchkin"`
`enemy.type != "burl"` is **FALSE** if `enemy.type` is `"burl"`

___

### _Boolean AND_

The boolean AND operator allows you to combine two other boolean operations.

For example:

```javascript
if (a && b) {
    // both a AND b are true
} else {
    // either a or b are false, or both are false
}
```

So, the AND operator evaluates to TRUE only if both of the values to either side are true, and FALSE if either of (or both of) the values are false.

```javascript
true && true  // == true
true && false  // == false
false && true  // == false
false && false  // == false
```

___

The **AND** operator has a short-circuit evaluation feature.

This means that if the first expression before `and` is `false` (or null), then the second expression after the operator isn't executed or evaluated.

We can use it when we need to read a property of an object, but we aren't sure the object exists.For example, when we need to read an enemy's type, first we should be sure that enemy exists or we'll get the error:

```javascript
var enemy = hero.findNearestEnemy();
if (enemy) {
    if (enemy.type == "burl") {
        // Do something
    }
}
```

But we can make it shorter:

```javascript
var enemy = hero.findNearestEnemy();
if (enemy && enemy.type == "burl") {
    // Do something
}
```

We don't have to worry about the reference error if there isn't an enemy, becase the second part isn't evaluated in this case.

___

### _Boolean OR_

The boolean OR operator allows you to combine two other boolean operations.

For example:

```javascript
if (a || b) {
    // either a OR b are true, or both are true
} else {
    // both a and b are false
}
```

So, the OR operator evaluates to TRUE if one or both of the values to either side are true, and FALSE only if both the values are false.

```javascript
true || true  // == true
true || false  // == true
false || true  // == true
false || false  // == false
```

The logical **OR** operator can make your code readable and help to avoid repetition. For example instead several `if` statements:

```javascript
if (condition1) {
    // do something
}
if (condition2) {
    // do the same again
}
```

you can put them in one:

```javascript
if (condition1 || condition2) {
    // do something
}
```

Avoiding to repeat the same code is a good practice because it makes your code readable. Also if you want to change some code and logic you can do it one place.

___


## If and Else

___

### _If-statements I_

`if`-statements are used to only perform actions if something (the _conditional_ of the `if`-statement) is `true`.

```javascript
if (conditional) {
    // Code inside here executes if "conditional" is true.
}
```

The `conditional` can be used to check existence, whether something is close or far, or the type of a unit.

```javascript
var tree = hero.findNearestTree();
var fruit = hero.pluckFruit(tree);  // A tree doesn't always have fruit.
// The fruit variable potentially holds information about a tree's fruit.

if (fruit) {
    // If the variable fruit holds information, then code inside the if-statement occurs.
    hero.eat(fruit);
}
```

___

### _If-statements II_

The `if` statement says: "**if** _this_ is `true`, **then** do _that_"

```javascript
if (2 + 2 == 4) {
    hero.say("2 + 2 equals 4!");  // Happens all the time, because 2 + 2 is 4!
}

if (2 + 3 == 4) {
    hero.say("2 + 3 equals 4!");  // Will never happen, because 2 + 3 isn't 4!
}
```

___

### _If-statements III_

`if`-statements are used to control the **flow** of a program. They can be used to check if a certain **condition** is `true`.

`if`-statements are like `while`, but instead of `true`, a _conditional_ should be checked against.

Commonly, `if` can be used to check if a unit **exists** by adding it after the `if`.

**Example:**
```javascript
var enemy = hero.findNearestEnemy();

if (enemy) {
    // The enemy exists
    // Probably should attack here!
}

// This always happens whether or not there is an enemy!
```

Programming is all about handling various situations automatically. Your main tool for doing different things based on the state of things are `if` and `else`. They look something like this:

```javascript
var a = 3;
var b = 9;

if (a > b) {
    hero.say("Math is broken!");
    hero.soundTheAlarm();
} else {
    hero.say("Math is still sound. All is well.");
    hero.sleep();
}
```

In this case, everything in the `if` block never happens, because 3 will never be greater than 9. So only the lines in the `else`block ever run.

___

### _Nesting_

You will often need to perform additional `if/else` checks within an existing `if` and `else` blocks.

```javascript
if (1) {
    hero.say("One exists! Does Two?");
    if (2) {
        hero.say("Two exists too!");
    }
    else {
        hero.say("Two is gone!");
    }
}
else {
    hero.say("One is not there, try Three!");
    if (3) {
        hero.say("Three is here!");
    }
    else {
        hero.say("Three is gone too! Four is our only hope!");
        if (4) {
            hero.say("Four is here to save the day!");
        }
        else {
            hero.say("We're doomed!");
        }
    }
}
```

___

### _Nested If-Statements_

In order to make your strategy work, you have to use _nested_ `if`-statements. That's where you put an `if`-statement _inside_ another `if`-statement to make more complex choices inside choices. (Yo dawg...)

```javascript
if (gem) {
    if (gem.pos.x == 34) {
        hero.say("left!");
    } else {
        hero.say("right!");
    }
} else {
    hero.say("middle!");
}
```

Note that the nested `if`-statement has extra indentation to show that it's _inside_ the first one. The extra indentation is our way of showing that the left and right branches are in the inner `if`-statement, while the middle branch is part of the outer `if`-statement.

___

### _Compact version_

**JavaScript only**

Both `if` and `else` do not need brackets if only one things to happen:

```javascript
// long versions, with braaces

// Style #0
if (1)
{
    alert("yes");
}
else
{
    alert("no");
}

// Style #1
if (1) {
    alert("yes");
}
else {
    alert("no");
}

// Style #2
if (1) {
    alert("yes");
} else {
    alert("no")
}

// short version, no braces
if (1)
    alert("yes");
else
    alert("no");

// inline version
if (1) alert("yes");
else alert("no");
```

Which arrangement to use? Whatever is most readable for you. Conciseness is nice, but you don't want code to get too dense.

___


## Loops

___


### _Looping While-True_

Sometimes a certain piece of code needs to be repeated **forever**! Dodging **fireballs** or escaping a long **maze** are two of many use cases! A `while-true` loop can do this!

A `while-true` loop could be considered a **container** of your code that repeats it over and over.

With this concept, it is important to match the **syntax** closely, as this is what the computer reads to perform it.

For example:

```javascript
while (true) {  // Notice while, true and {
    hero.moveRight();  // Notice the indentation
    hero.moveUp();  // Notice the indentation
}  // Notice the }
```

Code outside of the `while-true` loop will **NEVER** run!

Once you enter a `while-true` loop, no more code after will be ran!
An example:

```javascript
while (true) {
    // Everything between the { and } repeats!
    // Yes
}

// And code down here will NEVER run!
// The code will be stuck in while-true loop.
```

___

### _How To Use while-true Loops_

First, we start a loop with the `while` keyword. This tells your program **WHILE** something is true, repeat the **body** of the loop.

For now we want our loops to continue forever, so we'll use a **while-true loop**. Because true is always true! 

Don't worry about this true stuff too much for now. We'll explain it more later. Just remember that a **while-true loop** is a loop that never ends.

This is how you code a **while-true loop**:

```javascript
// Start the while-true loop with "while (true) {"
// Anything between the { and } is considered INSIDE the loop

while (true) {
    hero.moveRight();
    hero.moveLeft();
}

hero.say("This line is not inside the loop!");

// Tip: the indention (spacec at the start of the lines) is optional
// in javaScript (but not in Python), but it makes your code easier to read!
```

> _Tip: You can put whatever you want inside a while-true loop! But for this level, we only need to repeat two commands: `moveRight()` and `moveLeft()`._

___

### _Code Before While_

Code cannot be added after a `while-true` loop, but there can be code that is executed before a `while-true`.

This is because a **programm** that tells the `hero` what to do reads the lines one-by-one.
It will only get "stuck" in a `while-true` loop once it reaches it.

For example:

```javascript
hero.moveUp();     // This code happens first
hero.moveRight();  // This line happens second

while (true) {     // This line happens third, starting the loop
    hero.attack("Burt");  // This line happens fourth, fifth, sixth etc.
}

hero.say("I'm free!");  // This line NEVER happens
```

___

### _While-Conditional Loops_

A **while-loop** consists of a `while` statement followed by a **condition**.

The loop will continue to execute **while** the **condition** is **TRUE**.

The familiar **while-true-loop** looks loke:

```javascript
var count = 0;
while (true) {
    // Count from zero to infinity
    count += 1;
}
```

This is actually the same thing as a **while-condition-loop**, but the condition is always TRUE, so the loop never ends.

We could count from zero to 10 using a while-condition loop like:

```javascript
var count = 0;
while (count < 10) {
    count += 1;
}

hero.say(count);
```

In this example, the while-loop will continue until `count` is `10` (because `10 < 10` is **FALSE**), and then exit.

When the loop exits, the `hero.say(count)` code will run, and the hero will say `10`.

___

### _Loops Break_

Sometimes you want to stop a loop early. You can do this with the `break` statement:

```javascript
var i = 0;
while (true) {
    if (i >= 10) {
        break;
    }

    i += 1;
}
hero.say(i);
```

In this example, the loop will increment `i` from `0` to `10`, then the `break` statement will exit the loop before `i` is incremented to `11`.

The code after the loop then executes, and the hero will say `10`.

You can think of this as **breaking out** of the loop.

___

### _Loops Continue_

If you're inside a loop, and want to skip the current iteration and start over with the next iteration, you use the `continue` statement.

```javascript
while (true) {
    var enemy = hero.findNearestEnemy();
    if (!enemy) {
        continue;
    }

    // The hero will only say something if there's an enemy.
    hero.say("I see an enemy.");
}
```

When the code reaches a `continue` statement, it skips the rest of the loop and jumps back to the top.

___

### _Looping over Items in an Array with While_

Looping through the items in an array is called "iterating" over the array.

You can do this with a `while` loop by using an `index` variable to count each array item.

You can stop when you've reached the **length** of the array:

```javascript
var snacks = ["Chocolate", "Stroopwafels", "Cupcakes", "Ice Cream"];

var index = 0;
// Use snacks.length to get the length of the snacks array
while (index < snacks.length) {
    var snack = snacks[index];
    hero.say("I like " + snack);
    // Increment the index:
    index += 1;
}
```

___

### _Advanced While-loops_

This level focuses on advanced while-loops usage. Listed below are concepts to help visualize what kind of loops are involved.
+ Moving multiple using towards a point.
+ Defeating all at any given stage before continuing through the rest of a loop.
+ Attacking an enemy until it is defeated.
+ Waiting until a peasant catches up with a potentially faster hero.

An example of moving multiple units towards a point:

```javascript
var point = {x: 20, y: 20};
var friends = hero.findFriends();  // In this level, there is only 1 friend!
while (hero.distanceTo(point) > 0.5) {
    hero.move(point);
    // The hero.move() method allows the hero to
    // perform actions inbetween steps!
    for (var i = 0; i < friends.length; i++) {
        // In this level, you won't need to use
        // a for-loop with only 1 friend.
        var friend = friends[i];
        hero.command(friend, "move", point);
    }
}
```

An example of defeating all enemies inside a while loop:

```javascript
while (true) {
    hero.moveXY(hero.pos.x + 20, hero.pos.y);
    var enemy = hero.findNearestEnemy();
    while (enemy) {
        hero.attack(enemy);
        enemy = hero.findNearestEnemy();
    }
}
```

An example of defeating an enemy before moving to the next one:

```javascript
var enemy = hero.findNearestEnemy();
while (enemy.health > 0) {
    hero.attack(enemy);
    // This will continue to attack the enemy until
    // it runs out of health
}
```

An example of checking the distance with a unit other than the hero:

```javascript
var friend = hero.findNearest(hero.findFriends());
var point = {x: 20, y: 20};
while (friend.distanceTo(point) > 0.5) {
    // Note nothing much changes than checking the distance
    // from the peasant to the point
    hero.move(point);
    hero.command(friend, "move", point);
}
```

___


## Methods

___

### _Calling Methods_

The `hero` has actions or **methods** they can perform based on what gear they have.

The simplest case are the `moveUp`, `moveDown`, `moveLeft` and `moveRight` **methods**. To **call** a **method**, use `()` at the end of the **method**'s name.

**For example:**
```javascript
hero.moveRight();  // This tells the hero to move to the right.
hero.moveUp();
hero.moveLeft();
```

Note, the `hero` will do nothing if the `()` are executed!

```javascript
hero.moveDown;  // Nothing will happen!
```

___

### _Method Arguments_

No, not a fight with methods! But information that can be **passed** into a method to make it behave differently.

The **argument** is information included between the `(` and `)` when **calling** a function.

For example:

```javascript
hero.moveRight(2);  // The hero will move right twice!
```

There are methods that require **arguments** or else they won't know what to do!

Another example:

```javascript
hero.attack('Brak');  // The hero will attack Brak.

hero.attack();  // The hero doesn't know what to attack! This is an error!
```

___

### _Multiple Arguments_

Some **methods** can take multiple **arguments**!

To insert multiple **arguments** into a **method**, include `,` between each of the **arguments**.

**Methods** like `buildXY` require a very strict order for their **arguments** so be sure to check for examples and read the guide.

```python
# buildXY takes 3 arguments!
# That means you need 2 commas to separate all 3 arguments.
hero.buildXY("fence", 20, 20)
hero.buildXY("fire-trap", 40, 40)
```

___

### _Functions_

Functions are an important part of coding. 

You've been using functions all along: any time you write code like:

```python
hero.attack(enemy)
```

...you are "calling" (or "invoking") a function called `attack`.

The actual code that gets executed when you call `attack` is long and complex. Imagine if you had to write 25 lines of code in your program each time you wanted to swing your sword!

That's the first benefit of functions: they reduce a whole bunch of code down into one line.

Not only does this save you from having to re-type the same code over and over, it also makes your code easier to understand, because it takes what might really be complicated logic ("Ok so I want to attack. Do I have a weapon? Am I close enough to hit with my weapon? How long does it take to use my weapon? Do I hit? Do I cause damage?"), and makes it an easy to understand idea: `attack`.

Now you will not only be calling functions, you will **define** your own functions!

Defining a function has two parts: the **name** and the **body**.

The name is the thing you will use to call the function later, like `attack`.

The body is the code that will be executed when the function is called.

There are also sometimes **arguments** (like the `enemy` in `attack(enemy)`) but we will get into that in future levels.

___

**Functions** are an important part of writing code! They can be used to separate individual parts of code to help understand each bit easier.

**Functions** can do much more than just do some actions independent of any input! Using **arguments** and **parameters**, **functions** are capable of acting on what is sent in.

An **argument** is the information included between the `()` when any given **function** is called.

A **parameter** is a variable containing the information passed in from a **function**. It is just a predefined variable containing any information sent in!

```javascript
// 'target' after the function name is called a parameter.
// Think of a parameter as a new variable containing information from outside the function!
function chackAndAttack(target) {
    // 'target' is a predefined variable by the parameter, so nothing more needed to use it!
    if (target) {  // Check if the 'target' exists
        hero.attack(target);  // If so, attack
    }
}

var enemy = hero.findNearestEnemy();
// Below, the variable 'enemy' is an argument.
// Including 'arguments' when calling functions lets them behave differently depending on the input!
// In this case, we'll attack whatever enemy is passed in!
checkAndAttack(enemy);
```

___

### _Defining a Function_

A function has a **name** and a **body**.

The code inside the **body** of a function is not run until the function is **called**.

This is how to define and call a function (javascript):

```javascript
// The function's name is "myFunction"
function myFunction() {
    // This is the function's body.
    // Commands here will only run when the function is called
    hero.say("myFunction has been called!");
}

// This is no longer in the body of the function.
// This is line calls the function named myFunction
myFunction();
```

Python:

```python
# The function's name is "my_function"
def my_function():
    # This is the function's body.
    # Commands here will only run when the function is called
    hero.say("my_function has been called!")

# This is no longer in the body of the function.
# This is line calls the function named my_function
my_function();
```

___

### _Return Statement I_

A function can `return` a value back to where the function was called.

You have used function return values a lot:

```javascript
var enemy = hero.findNearestEnemy();
```

In this example, you **assign the value returned by** `hero.findNearestEnemy()` to the variable `enemy`.

Functions you write can also return values, using the `return` keyword:

```javascript
function add(a, b) {
    return a + b;
}

var sum = add(2, 3);
hero.say(sum);
// The hero says: 5
```

**Note** that `return` immediately exits the function and returns the given value back to the caller.

___

### _Return Statement II_

Functions can contain several (or many) instructions to make you can clearer and more readable. Also, functions allow avoiding repetition of code.

The function can return values and you can use them to get some data from them. You've met it before, when you used `hero.findNearestEnemy()`.

To return a value from a function, use the keyword `return` in the function. Place the value (or variable) which you want to return after that.

```javascript
function someFunction() {
    // ...
    return 3;  // the function returns 3
}
```

You can save function's result in a variable and use it further in your code:

```javascript
var x  = someFunction();
// No x equals 3
hero.say(x);
```

___


## Code Combat

___

### _Directional Movement_

In the Dungeon, the `hero` has access to the following **methods**:
+ `moveUp` - moves the hero up (north) a bit
+ `moveDown` - moves the hero down (south) a bit
+ `moveLeft` - moves the hero left (west) a bit
+ `moveRight` - moves the hero right (east) a bit

Use these to navigate the perilous passages!

> Remember! These methods are `hero` object methods. To use them you need to run it within an `hero` object, for example:

```javascript
hero.moveUp();
hero.moveRight();
hero.moveRight();
hero.moveDown();
```

___

### _Attacking with Strings_

Escaping the Dungeon of Kithgard is dangerous work. Sometimes a little muscle is required to break out!

By now, the `hero` has the `attack` method which is valuable when facing enemies toe-to-toe.

Check above an enemy's head for their name and **call** the `attack` method using the name **string** as an **argument**.

Munchkins in the Dungeon must be attacked **twice** to defeat them! You will need to call the method **twice**!

An example:

```javascript
hero.attack("Brak");
// You must attack twice to defeat munchkins:
hero.attack("Brak");
```

___

### _Finding Nearby Enemies_

With glasses, the `hero` has access to the `findNearestEnemy` **method**.

But, the interesting thing about this **method** is that it **returns** something! It returns the nearest enemy to the `hero`.

The **method** on it's own isn't too useful. However when combined with a `variable`, it can be used to find any nearby enemy and attack them!

```javascript
hero.findNearestEnemy();  // This find nearest enemy, but doesn't store it anywhere!
var enemy = hero.findNearestEnemy();  // Now there is a variable to attack!

hero.attack(enemy);
```

___

### _Attack Nearby Enemies_

The `attack` **method** can be used to target enemy units, as well!

If the hero knows the name of the enemy:

```javascript
hero.attack("name of the enemy");
```

If the `hero` doesn't know the enemy's name, passing in a **reference** to the unit allows the `hero` to `attack` them.

```javascript
var foe = hero.findNearestEnemy();  // Set foe to a nearby enemy.
hero.attack(foe);  // Attack the enemy in the foe variable.
```

___

### _Say and Speaking_

The `hero` always has access to the `say` method. This creates a speech bubble above the `hero`'s head saying whatever is inside.

In certain levels this is a requirement! But it can be a useful debugging tool.

```python
hero.say("Let me out!")
hero.say("Kazaam!")
hero.say("I'm here now.")
```

___

### _Building Defenses_

When the `hero` has a **hummer**, they can build defenses like `"fence"`s and `"fire-trap"`s.

However, the `hero` need to know the exact **coordinate** location of where to build! That is why the **method** is called `buildXY`, because it needs an `x` and `y` position.

Mouse-over the level map and after a second the **coordinates** will appear. Use this to guide where to `buildXY`.

The **arguments** in order are:
+ item *type* as a `string` such as `"fence"` and `"fire-trap"`.
+ item position `x`, which is always a number.
+ item position `y`, which is always a number.

For example:

```javascript
hero.buildXY("fence", 20, 20);
```

___

### _Code Limits_

Some levels have a strict amount of lines of code you're required to write!

If you find yourself going over the limit, consider using a `while-true` loop to shorten your code.

For example:

```javascript
hero.moveRight();
hero.moveUp();
hero.moveRight();
hero.moveUp();
hero.moveRight();
hero.moveUp();
```

Becomes:

```javascript
while (true) {
    hero.moveRight();
    hero.moveUp();
}
```

___


### _Events_

An **event** is something that happens in the game world.

For example, a `"spawn"` event happens when a unit is created (spawned). A `"hear"` event happens when a unit hears another unit `say()` something.

You can register a function as an **event handler** using the `on(eventType, eventHandler)` method.

An **event handler** function is run when the specified type of event happens:

```python
# Define an event handler function:
def on_hear():
    pet.say("I heard something!")

# Register on_hear as an event handler for "hear" events on the pet object.

pet.on("hear", on_hear)
```

___

### _Event Handler_

An **event handler** is a function that will be executed when an **event** happens.

You use `pet.on(eventType, eventHandler)` to assign an event handler for an event type, like `"hear"`.

The event handler can be any function you define. It should accept one parameter, the event's data. You'll learn more about the event data later.

For example:

```python
def some_function(event):
    pet.say("Ahhh")
    pet.say("Bbbbzzzz")

pet.on("hear", some_function)
```

_**Note**: You don't use `()` after `someFunction` in `pet.on("hear", someFunction)`. The `()` means that the function is immediately called. Instead we are passing the function as an argument to `.on()` so that it can be called later, when a `"hear"` event happens._

___

### _X Y Coordinates_

A position on the game map is represented as two numbers: `x` and `y` coordinates.

`x` represents the **right-left** (horizontal) direction.

`y` represents the **up-down** (vertical) direction.

Moving in the **right** direction, the `x` number **increases**. Moving in the **left** direction, the `x` number **decreases**.

Moving in the **up** direction, the `y` number **increases**. Moving in the **down** direction, the `y` number **decreases**.

The bottom left corner of the map is `0, 0` (**x** is zero, **y** is zero).

___

### _Positions_

Most of the things you interact with in the game (your hero, enemies, allies, coins, etc) have a position on the game map.

Remember that a position has an `x` coordinate and a `y` coordinate.

A thing's position can be accessed with the `pos` property.

The x coordinate can be accessed with the `x` property of the `pos` object.

The y coordinate can be accessed with the `y` property of the `pos` object.

```javascript
var item = hero.findNearestItem();

// Move to the item's position:
hero.moveXY(item.pos.x, item.pos.y);
```

___

Each item object (and each unit) has a `pos` property, which stands for its position. And each `pos` is itself an object, which has `x` and `y` properties that you can use with `moveXY` and `buildXY`.

```javascript
var enemy = hero.findNearestEnemy();

if (enemy) {
    var p = enemy.pos;
    hero.say(p.x);
    hero.say(p.y);
}
```

___

### _moveXY vs move_

With `move`, you specify a **position** to move to.

Positions are objects with an `x` property and a `y` property. You've used these before, with `moveXY` like:

```javascript
hero.moveXY(coin.pos.x, coin.pos.y);
```

but with `move` you'd just pass the `pos` object as the argument, like:

```javascript
hero.move(coin.pos);
```

#### _Block Execution or Continue Execution?_

With `moveXY` **your program will stop executing** until your hero has reached the specified `(x, y)` location.

With `move` your hero will **move toward** the `pos` you pass in, but **your program will continue to execute**.

This means that your hero will take a few steps in the direction of `pos`, but then your program will continue to run, so you can interrupt that movement by taking different actions in the next loops of your code.

___

### _Game Health_

Code Combat units have two properties relating to health:
+ `unit.maxHealth` is the unit's maximum total health.
+ `unit.health` is the unit's current health.

So, if you want to do something when your hero is down to half health, you could do:

```javascript
if (hero.health < hero.maxHealth / 2) {
    // Run away
}
```

___

### _Game Time_

The `hero.time` property is the age of the game world measured in seconds.

When you click "Run" or "Submit", the age starts at `0`, and increases from there.

You can use this to choose actions based on the passage of time, like:

```javascript
if (hero.time < 30) {
    // Do something for the first 10 seconds.
} else if (hero.time < 30) {
    // Do something between 10 and 30 seconds.
}
```

___

### _Hero Gold_

The Quartz Sense Stone allows you to determine how much gold you have using the `hero.gold` property.

For example, some buildable items cost gold to build:

```javascript
if (hero.gold >= 25) {
    hero.buildXY("decoy", hero.pos.x, hero.pos.y);
}
```

___

### _Hero Debug_

Works like JavaScript's `console.log`, taking any number of arguments and printing them out. Output appears in your JS console.

___
