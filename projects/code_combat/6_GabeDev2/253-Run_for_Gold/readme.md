## _Run For Gold_

#### _Legend says:_
> The most valuable items disappear first.

#### _Goals:_
+ _Destroy som e items after a while_
+ _Increase score according to the value of items_
+ _No more than 50 items on the firld at a time_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](runForGold.js)**

#### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _THE RIGHT PRIORITIES ARE THE KEY TO SUCCESS._

___

### _HINTS_

To make this simple collecting game we need to master time management.

Use time-stamps to track when it's time to spawn new treasures:

```python
if game.time > game.spawnTime:
    spawnSomething()
    game.spawnTime += spawnInterval
```

Also, we can save a timestamp as an item's property to track when it's time to `destroy()` that item.

In this level, we're using the `"spawn"` event to track the state of each item inside a `while-true` loop.

Inside the loop, when it's time to `destroy` the item, you don't need to break the loop because when an item/unit is destroyed the event handler is stopped too.

___
