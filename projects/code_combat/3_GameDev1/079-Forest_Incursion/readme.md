## _Forest Incursion_

####_Legend says:_
> Okar is slow and weak. Make him fast and strong!

#### _Goals:_
+ _Use the Golliath as the player_
+ _Change the player's `attackDamage`_
+ _Increase the player's `maxHealth`_
+ _Increase the player's `maxSpeed`_
+ _Complete your own level_

#### _Topics:_
+ **Basic Syntax**
+ **Arguments**
+ **Strings**
+ **Variables**
+ **Assigning Properties**

#### _Solutions:_
+ **[JavaScript](forestIncursion.js)**

#### _Rewards:_
+ 30 xp
+ 10 gems

#### _Victory words:_
+ _WHAT A COMEBACK!_

___

### _HINTS_

Then you call `spawnPlayerXY()`, it returns a player object for you to modify.

You can then change properties of the player like `maxSpeed`, `maxHealth`, `health` and `attackDamage`!

```javascript
var player = game.spawnPlayerXY("goliath", 20, 20);
player.maxHealth = 600;
player.maxSpeed = 12;
player.health = 600;
player.attackDamage = 9001;
```

___
