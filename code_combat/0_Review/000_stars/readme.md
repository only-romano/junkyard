## _Stars_

___


**Table of Contents:**

* [Boss Star I](#boss-star-i)
* [Boss Star II](#boss-star-ii)
* [Boss Star III](#boss-star-iii)

___

### _Boss Star I_

This token of leadership lets you summon and command soldiers–as long as you have the gold.

![](img/star1.png)


#### `hero.costOf`

Returns the gold cost for the given build or summon type.

**Example:**
```javascript
hero.costOf("soldier");
```

**Required Parameters:**
+ `buildType`: `string` (ex. `"soldier"`) - _The type of unit to build_

**Returns:**
+ `number`


#### `hero.summon(summonType)`

Summons a friendly unit for you to command, if you have enough gold.

**Example:**
```javascript
hero.summon("soldier");
```

**Required Parameters:**
+ `summonType`: `string` (ex. `"soldier"`) - _The type of unit to summon_


#### `hero.command()`

`command` allows you to call any of `commandableMethods` (ex. `['move', 'attack', 'defend']`) on allied minions. You can command minions of types in `commandableTypes` (ex. `['soldier', 'archer']`.

_(you may not be able to summon all of these types)_

**Example:**
```javascript
var friend = hero.getNearestFriend();
hero.command(friend, 'move', hero.pos);
```

**Required Parameters:**
+ `summonType`: `string` (ex. `"soldier"`) - _The type of unit to summon_


#### `hero.commandableTypes`

> `array`

These are all the allied minion types that you can command.

_(you may not be able to summon all of these types)_


#### `hero.commandableMethods`

> `array`

These are all the method names that you can call on allied minion units.

___

### _Boss Star II_

Summons and commands soldiers and archers.

![](img/star2.png)

> Available skills:
+ `hero.costOf`
+ `hero.summon(summonType)` (`"soldier"`, `"archer"`)
+ `hero.command()`
+ `hero.commandableMethods` (`"move"`, `"attack"`, `"defend"`, `"buildXY"`)
+ `hero.commandableTypes` (`"soldier"`, `"archer"`, `"griffin-rider"`, `"peasant"`)


#### `hero.built`

> `array`

A list of units the hero has built or summoned. You can use information from these units to help decide on a building strategy.

**Example:**

```javascript
var summonTypes = ["archer", "soldier", "griffin-rider", "archer"];
var summonType = summonTypes[hero.built.length % summonTypes.length];
if hero.gold >= hero.costOf(summonType) {
    hero.summon(summonType);
}
```

___

### _Boss Star III_

Summons and commands soldiers, archers, griffin riders, and peasants.

![](img/star3.png)

> Available skills:
+ `hero.costOf`
+ `hero.summon(summonType)` (`"soldier"`, `"archer"`, `"griffin-rider"`, `"peasant"`)
+ `hero.command()`
+ `hero.commandableMethods` (`move`, `attack`, `defend`, `cast`, `buildXY`, `shield`)
+ `hero.commandableTypes` (`"soldier"`, `"archer"`, `"griffin-rider"`, `"peasant"`, `"paladin"`)
+ `hero.built`

___
