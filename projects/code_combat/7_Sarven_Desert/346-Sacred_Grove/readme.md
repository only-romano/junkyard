## _Sacred Grove_

#### _Legend says:_
> The grove in a desert is a miracle. Protect it from evil ogres

#### _Goals:_
+ _Protect the forest from the ogres_

#### _Topics:_
+ **Reading the Docs**

#### _Solutions:_
+ **[JavaScript](sacretGrove.js)**
+ **[Python](sacred_grove.py)**

#### _Rewards:_
+ 160 xp
+ 160 gems

#### _Victory words:_
+ _DON’T LOOK INTO THE PUGICORN’S EYES — IT’S A TRAP._

___

### _HINTS_

Protect the sacred grove from ogres. Don’t let an ogre even step into the grove.

Your hero and paladins protect three passages. The last guardian is your pet -- Pugicorn.

The Pugicorn can `charm` an enemy, so it will fight on your side some time.

Use the Power of Cuteness!

___

The pugicorn's special ability is `charm`. The pet charms an enemy whose `maxHealth < hero.maxHealth / 5` and the enemy protects the pet some time.

```javascript
var ogre = pet.findNearestByType("ogre");
if (pet.isReady("charm") && ogre) {
    pet.charm(ogre);
}
```

___
