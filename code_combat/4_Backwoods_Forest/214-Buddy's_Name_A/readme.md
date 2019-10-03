## _Buddy's Name A_

#### _Legend says:_
> You have a pet, but what is its name? Let's ask.

#### _Goals:_
+ _The pet must answer to the peasant_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Strings**
+ **Functions**

#### _Solutions:_
+ **[JavaScript](buddyNameA.js)**
+ **[Python](buddy_name_a.py)**

#### _Rewards:_
+ 79 xp
+ 45 gems

#### _Victory words:_
+ _BARK. BARBKARKBAKRBK._

___

### _HINTS_

The peasant wants to know Kitty's name!

However, your pet doesn't have an **event handler** yet!

use `pet.on("eventName", functionName)` to set a new event for `"hear"` and `sayName`.

An **event handler** is a function that monitors for a specific **event**.

An **event handler** can be created by using the `.on()` method on certain units, like your `pet`!

Use `pet.on("eventType", functionName)` to run the function at `functionName` when the event `"eventType"` occurs. However, this is just an example, as the `"eventType"` event doesn't actually exist! Look at a real example:

_**Note**: Do not include a `()` after the `functionName`! You only want to point to the function, not call it at that exact moment when setting up the **event handler**_

```javascript
// This defines a new function named performTrick!
function performTrick(event) {
    // When this function is called, the pet performs a trick.
    pet.trick();
}

// Using the .on() method, the pet waits for a "hear" event to run performTrick.
pet.on("hear", performTrick)
```

The `"hear"` event occurs when the unit quite literally **hears** something! If someone uses the `.say("string")` method close enough to the unit, the event will **fire** and get **called**. At this point, the code inside the function is run!

In this level the peasant and cows are saying things, so every time they speak, Kitty will say something.

_**Remember**: `pet.on("hear", sayName)` is like saying: **Pet should `on` `"hear"`ing something run `sayName`**_

___
