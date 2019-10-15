## _Over the Garden Wall_

#### _Legend says:_
> Build a fence around your farm!

#### _Goals:_
+ _The humans must survive_
+ _Spawn at least 8 fence sections_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Strings**

#### _Solutions:_
+ **[JavaScript](overTheGardenWall.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _WALLS KEEP PEOPLE OUT. IT’S A ROCK FACT!_

___

### _HINTS_

This is the first `game` development level.

You will learn how to make your own games!

You need to spawn 4 more `"fence"`s (for a total of 8, including the ones given to you) to protect these villagers from marauding ogres:

```javascript
game.spawnXY("fence", 39, 6);
game.spawnXY("fence", 39, 10);
```

You should spawn a fence every `4` metres in the Y axis:

```javascript
game.spawnXY("fence", 39, 6);
game.spawnXY("fence", 39, 10);
game.spawnXY("fence", 39, 14);
```

You should `spawnXY` fences at the same x coordinate (`39`), but vary the y coordinate.

Each fence segment should be `4` metres more than the previous `"fence"`s y position.

___
