## _Pet Engineer_

#### _Legend says:_
> Powerful battle machines. But, simple enough, even a pet can use them!

#### _Goals:_
+ _Protect the camp for 50 seconds._

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Nested If Statements**
+ **Accessing Properties**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](petEngineer.js)**
+ **[Python](pet_engineer.py)**

#### _Rewards:_
+ 190 xp
+ 160 gems

#### _Victory words:_
+ _CONTROLLING ROBOTS ISN'T ROCKET SCIENCE... IT'S ROBOTIC!_

___

### _HINTS_

Move your pet to the left button (near the robot) when it hears the `archer` call for help.

Move your pet to the right button (near the cannon) when it hears the `soldier` call for help.

Use the `"hear"` event handler's `event.speaker` parameter to recognize who is calling for help!

You can check who `event.speaker` is like this:

```javascript
var archer = pet.findNearestByType("archer");
if (event.speaker == archer) {
    // It's the archer
}
```

The left button is located at `x = 32`, `y = 30`.

The right button is located at `x = 48`, `y = 30`.

___
