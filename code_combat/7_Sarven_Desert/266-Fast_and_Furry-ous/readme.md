## _Fast and Furry-ous_

#### _Legend says:_
> Nobody can catch the Road Runner.

#### _Goals:_
+ _Your hero must outrun the ogre._
+ _Your pet must outrun the ogre._

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Strings**
+ **Functions**
+ **Event Concurrency**

#### _Solutions:_
+ **[JavaScript](fastAndFury.js)** _warrior_
+ **[Python](fast_and_fury.py)** _wizard_

#### _Rewards:_
+ 142 xp
+ 69 gems

#### _Victory words:_
+ _UP NEXT IS THE 100 METER BATON PASS!_

___

### _HINTS_

Normally code is executed in order: you have to wait for one command to finish before the next one runs.

```javascript
// The hero only moves when the pet has finished moving:
pet.moveXY(50, 21);
hero.moveXY(50, 12);
```

If you put the pet's code into an event handler function, it will run in parallell with the hero's code!

With the event handler, both your pet and hero will move at the same time, winning the race.

```javascript
// Both hero and pet move at the same time.
function petMove(event) {
    pet.moveXY(50, 21);
}

pet.on("spwan", petMove);
hero.moveXY(50, 21);
```

___
