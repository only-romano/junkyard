## _Freeze Tag_

#### _Legend says:_
> Let's play Tag.

#### _Goals:_
+ _Change behavior for tagged archers_
+ _Win the game_

#### _Topics:_
+ **Basic Syntax**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](freezeTag.js)**

#### _Rewards:_
+ 30 xp
+ 30 gems

#### _Victory words:_
+ _HM, IS IT FAIR TO PLAY WITH THE TELEKINESIS ABILITY?_

___

### _HINTS_

When one object touches another object, it triggers a `"collide"` event.

You can use it on other spawnables, not only the hero.

In this game the hero can tag archers and "freeze" them, other archers can untag "frozen" archers. Don't mix up who is `event.target` and `event.other`.

___
