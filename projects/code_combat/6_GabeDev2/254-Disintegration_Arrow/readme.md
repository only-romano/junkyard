## _Disintegration Arrow_

#### _Legend says:_
> Let's clear that battlefield.

#### _Goals:_
+ _Destroy at least 50 defeated ogres_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](disintegrationArrow.js)**

#### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _DON'T LEAVE A MESS AFTER YOURSELF. EVEN IT'S OGRES._

___

### _HINTS_

Previously, we've used the `destroy` method to remove obstacles or non-collected items.

`destroy` can also be used to increase the performance of your game.

In this level, ogre hordes are attacking a village defended by archers.

So after several minutes, there will be hundreds of defeated ogres.

Let's save the memory and resources by `destroy`ing the defeated ogres.

___

All units and items in the game have `destroy` method. Calling an item/unit method is like a property:

```javascript
var ogre = game.spawnXY("munchkin", 1, 1);  // Create...
ogre.destroy();  // and destroy.
```

___

Use `game.setActionFor` if you need to set an event handler for all units/items of the same type, which are created already or will be created.

```javascript
function onSpawn(event) {
    event.target.say("Here!");
}

var ogre1 = game.spawnXY("munchkin", 1, 1);

game.setActionFor("munchkin", "spawn", onSpawn);  // For All "munchkin"s
var ogre2 = game.spawnXY("munchkin", 2, 2);
```

___
