## _Berserker_

#### _Legend says:_
> Ogres think that fences can stop game masters.

#### _Goals:_
+ _Increase and decrease the hero's scale_
+ _Destroy at least 3 fences_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](berserker.js)**

#### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _WALLS? THERE WERE SOME WALLS?!_

___

### _HINTS_

**Grab mushroom and go through the fences!!!**

When one object touches another object, it triggers a `"collide"` event.

___

Using a `"collide"` event is similar to using a `"collect"` event:

```python
def onCollide(event):
    who = event.target
    withWhat = event.other
    who.say("I collided with " + withWhat.id)
```

Note that some objects do not cause collisions! Things like units and fences do.

The `"collide"` event is similar to the `"collect"` event. It has similar event data and triggers when you step on something. However `"collide"` works with "hard" objects, like obstacles or units.

Avoid assigning the `"collide"` event handler for many objects for the performance reasons. Try to choose the object which is more important.

For example, if you want to track collisions of the player and walls only, then it's better to assign the event handler for the player instead of all the walls.

Don't mix up `target` and `other` properties in the event data. The `"collide"` event is two-way event:

```javascript
var player = player.spawnPlayerXY("knight", 10, 10);
var wall = game.spawnXY("fence", 20, 20);

function onCollide(event) {
    var subject = event.target;
    var object = event.other;
}

wall.on("collide", onCollide);
player.on("collide", onCollide);
```

In the given example the event triggers twice when the `player` collides with the `wall` and the `onCollide` function is called twice too. However, `target` and `other` will be swapped:
+ the player's event: `target` -> `player`, `other` -> `wall`
+ the wall's event: `target` -> `wall`, `other` -> `player`

___
