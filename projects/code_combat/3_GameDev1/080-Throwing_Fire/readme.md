## _Throwing Fire_

#### _Legend says:_
> Some game objects can be configured by setting properties.

#### _Goals:_
+ _Change the direction to vertical_
+ _Win the game_

#### _Topics:_
+ None

#### _Solutions:_
+ **[JavaScript](throwingFire.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _"IT DOESN'T HAVE TO BE PERFECT.. IT JUST NEEDS TO BE FUN (MOST OF THE TIME)" -- RONALD JENKEES_

___

### _HINTS_

Some game objects can be configured by setting their properties.

A `"fire-spawer"` shoots a bunch of fireballs! 

By default it shoots them `"horizontal"`ly.

You can change it to shoot `"vertical"`ly like this:

```javascript
var spew = game.spawnXY("fire-spawer", 40, 40);
spew.direction = "vertical";
```

___
