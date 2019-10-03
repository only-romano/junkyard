## _Pet Adjutant_

#### _Legend says:_
> Nobody listens to me. Fluffy, you are my only friend.

#### _Goals:_
+ _Survive 50 seconds_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Nested If Statements**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](petAdjutant.js)**
+ **[Python](pet_adjutant.py)**

#### _Rewards:_
+ 190 xp
+ 160 gems

#### _Victory words:_
+ _ADJUTANT: A MILITARY OFFICER WHO ACTS AS AN ADMINISTRATIVE ASSISTANT TO A SENIOR OFFICER._

___

### _HINTS_

The hero needs to survive 50 seconds before wizards can teleport you to safety.

The pet can react to different things it hears using the `event.message` property.

Move the pet to the bottom X when the hero says `"Fire"`.

Move the pet to the top X when the hero says `"heal"`.

```javascript
function onHear(event) {
    if (event.message == "Fire") {
        // Fire the cannons.
    }
}
```

You don't have to change the code inside `while`-loop, but you can if you want to experiment with advanced strategies.

___
