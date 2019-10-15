## _Grim Determination_

#### _Legend says:_
> Command your paladins to withstand the ogre warlocks' assault with grim determination.

#### _Goals:_
+ _Protect Reynaldo_
+ _Bonus: Don't lose any paladins_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Return Statements**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](grimDetermination.js)**
+ **[Python](grim_determination.py)**

#### _Rewards:_
+ 263-393 xp
+ 121-180 gems

#### _Victory words:_
+ _BEHIND LAY FIRE, AHEAD DAMNATION. THEY SET THEIR SHIELDS WITH GRIM DETERMINATION._

___

### _HINTS_

Paladins are capable of casting a spell! They can cast the spell: `heal` on nearby targets, when it's off cooldown.

```javascript
var paladin = hero.findNearest(hero.findByType("paladin"))
if paladin.canCast("heal", hero) {
    hero.command(paladin, "cast", "heal", hero);
}
```

___

This level introduces the Paladin ally. Paladins can cast a healing spell, and can use a shield to withstand more damage then usual.

The sample code gives you a `lowestHealthPaladin` function, which returns the paladin with the lowest health, if any are damaged.

Fill in `commandPaladin` using `lowestHealthPaladin` along with `canCast("heal",target)` and `command(paladin, "cast", "heal", target)` and `command(paladin, "shield")` to keep your paladins alive.

Write `commandPeasant` to have your peasants collect coins.

Write `commandGriffin` to have your Griffin Riders attack the enemy.

Finally, in the main loop, you should summon Griffin Riders when you have enough gold.

_**Tip**: Paladins also carry a mace to `attack` with!_

___
