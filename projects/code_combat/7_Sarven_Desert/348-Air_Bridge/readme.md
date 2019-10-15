## _Air Bridge_

#### _Legend says:_
> SOS! SOS! We need a helicopter!

#### _Goals:_
+ _Evacuate 3 peasants_

#### _Topics:_
+ **Basic Syntax**

#### _Solutions:_
+ **[JavaScript](airBridge.js)**
+ **[Python](air_bridge.py)**

#### _Rewards:_
+ 256 xp
+ 191 gems

#### _Victory words:_
+ _COULD YOU BRING A PRINCESS?_

___

### _HINTS_

The peasants are trapped. We need to help them and clear the minefield. The Grffin Baby pet can help us with this task. It can carry units whose `maxHealth < 0.1 * hero.maxHealth` as items.

`pet.carryUnit(unit, x, y)`

Bring peasants and then use a munchkin to clear the minefield.

The unique ability of the Griffin Baby is `carryUnit`. Just say who and where to deliver an unit.

```javascript
var thrower = pet.findNearestByType("thrower");
pet.carryUnit(thrower, hero.pos.x + 3, hero.pos.y);
```

___
