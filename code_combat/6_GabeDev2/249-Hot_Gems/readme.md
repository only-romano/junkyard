## _Hot Gems_

#### _Legend says:_
> Hot Gems can be dangerous. It's better to avoid them. Ok, maybe one... or two.

#### _Goals:_
+ _Gems must reduce health_
+ _Gold coin must increase health_
+ _Collect at least 1 gem_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](hotGems.js)**

#### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _THE GREED HURTS US._

___

### _HINTS_

Let's practice using the `"collect"` event.

This event allows you to track items collected by some character.

In this level, we'll make it so Gems are hot and hurt the hero, while Gold Coins are cool and heal the hero.

However, the collect goal doesn't distinguish between them, so the player can collect both of them.

Don't forget to collect at least one gem to be sure it works!

```python
def onCollect(event):
    who = event.target
    what = event.other
    if what.type == "potion":
        who.say("Oh, it's poisoned.")
        who.defeat()

somebody.on("collect", onCollect)
```

___
