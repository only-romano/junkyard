## _Pied Piper_

#### _Legend says:_
> Use your new advanced remote decoy to lure ogres in certain places.

#### _Goals:_
+ _Escape the village_
+ _Peasants must survive_

#### _Topics:_
+ **Basic Syntax**

#### _Solutions:_
+ **[JavaScript](piedPiper.js)**
+ **[Python](piedPiper.py)**

#### _Rewards:_
+ 190 xp
+ 160 gems

#### _Victory words:_
+ _HAVE YOU EXPECTED "WHAT DOES THE FOX SAY?" PHRASE HERE?_

___

### _HINTS_

Ogres use peasants as hostages. That's why we should use some decoy to lure ogres away from hostages.

The Blue Fox can change the form and lure ogres where you need. Lure scouts to the far canyon and brawler closer to yaks.

```javascript
pet.shapeShift();
pet.moveXY(40, 30);
```

___

The Blue Fox has the unique ability `shapeShift()` which allows the pet transform itself to the decoy -- the fleeing peasants. No enemy in the `30m` range can't stand to hit this easy target.

You've used `"decoy"` before, now you have stronger and controllable decoy, which allows you to lure ogres anywhere.

Yaks don't like ogres, so if you make brawlers to come close to yaks, you will solve the ogre problem.

___
