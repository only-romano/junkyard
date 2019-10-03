## _Accounts Department_

#### _Legend says:_
> Coins and gems have different value. Count them carefully.

#### _Goals:_
+ _Change game score based on values of items_
+ _Get at least 220 score_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](accountsDepartment.js)**

#### _Rewards:_
+ 10 xp
+ 10 gems

#### _Victory words:_
+ _I THINK THOSE SKELETONS WERE AUDITORS._

___

### _HINTS_

Let's look at a new type of events: `"collect"`.

This event allows you to track items which are collected by some character.

Gems and various types of coins have different values. With the `"collect"` event we can count the total value of all collected items.

```python
def onCollect(event):
    who = event.target
    what = event.other
    game.score += what.value
    who.say("I found " + what)

somebody.on("collect", onCollect)
```

Let's make a simple collection game with randomly generated treasures.

Collect at least 220 gold.

The `"collect"` event data has two important properties: `target` and `other`.

`target` is the subject of the action -- who's collected something (and the "owner" of the event).

`other` is the object of the collection -- what is collected.

So it's like the sssentence: `target has collected` other.

We use the term `other` instead of something like `item` because there will be more events in the future that have a subject and object, and `other` can be used consistently for all of these.

It's also a convention used in professional game engines you may see when you go on to make your own
games outside of CodeCombat!

The `"collect"` event is triggered when a collector "steps on" an item (collect it). In this case, default collection action happens (for example, healing by potions) and the item disappears.

You can track those events and count them plus add your own actions for them (Ex. increase attack damage for potions). Be creative!

___
