## _Taunting_

#### _Legend says:_
> Ogres are so different.

#### _Goals:_
+ _Defeat the ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Accessing Properties**
+ **Boolean Equality**

#### _Items we've got (- or need):_
+ Weapon

#### _Solutions:_
+ **[JavaScript](taunt.js)**
+ **[Python](taunt.py)**

#### _Rewards:_
+ 60 xp
+ 62 gems

#### _Victory words:_
+ _BE CAREFUL WHEN YOU TAUNT._

___

### _HINTS_

You can easily defeat munchkins. But for brawlers, we've prepared some traps. If you see a "brawler" type ogre, then just call it (say anything).

You can distinguish ogres by their `type` property. Munchkins' type is `"munchkin"`, Brawlers' type is `"brawler"`.

All units and items have the `type` property. This property is very important, because allows you to define different tactics for various types of enemies/friends/items.

```javascript
if (enemy.type == "munchkin") {
    hero.attack(enemy);
}
else if (hero.type == "burl") {
    hero.say("I don't think it's a good idea");
}
```

___


