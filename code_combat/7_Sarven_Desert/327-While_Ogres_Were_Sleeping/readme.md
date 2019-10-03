## _While Ogres Were Sleeping_

#### _Legend says:_
> Choose your targets wisely. Don't wake the sleeping ogres.

#### _Goals:_
+ _Defeat a munchkin_
+ _Collect a coin_
+ _Defeat a skeleton_
+ _Escape from the camp_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops with Conditionals**
+ **If Statements**
+ **Accessing Properties**
+ **Boolean Greater/Less**

#### _Solutions:_
+ **[JavaScript](whileOgresWereSleeping.js)**
+ **[Python](while_ogres_were_sleeping.py)**

#### _Rewards:_
+ 299 xp
+ 224 gems

#### _Victory words:_
+ _EFFICIENT AND CALCULATING. BUT NOT COLD, IT'S THE DESERT!_

___

### _HINTS_

The ogres are sleeping, so proceed carefully:

First, attack only if `enemy.team` is `"ogres"` **AND** `enemy.health` is less than `10`.

Second, collect coins only if `coin.value` is less than `5` **AND** `hero.distanceTo(coin)` is less than `7`.

Third, attack only if `enemy.health` is less than `10` **AND** `enemy.type` is `"skeleton"`.

Ogres are sleeping in the middle of the desert. A perfect time to strike!

Navigate around their camp and defeat choice ogres and loot certain coins.

Remember that the `<`, `>`, `<=`, and `>=` operators just compare two elements and return a boolean value of `true` or `false`.

```javascript
var enemy = hero.findNearestEnemy();
// Read it like it's written:
// If the distance is less than 10m AND the enemy's health is less than 10!
if (hero.distanceTo(enemy) < 10 && enemy.health < 10) {
    // Defeat the weak enemy!
}
```

___
