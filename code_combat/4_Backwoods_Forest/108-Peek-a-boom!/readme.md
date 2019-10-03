## _Peek-a-boom!_

#### _Legend says:_
> Hide between the trees to lay an explosive ambush!

#### _Goals:_
+ _Defeat the ogres_
+ _Humans must survive_
+ _The hero must survive_

#### _Topics:_
+ None

#### _Items we've got (- or need):_
+ Weapon

#### _Solutions:_
+ **[JavaScript](peek.js)**
+ **[Python](peek.py)**

#### _Rewards:_
+ 35 xp
+ 41 gems

#### _Victory words:_
+ _IT WOULDN'T BE AN AMBUSH WITHOUT THE ELEMENT OF SURPRISE!_

___

### _HINTS_

Ogre munchkins are on patrol for peasants!

When you see a munchkin, build a trap along the path. Otherwise, return to your hidey hole!

You can use an `else` to tell your hero to do an alternate action if the `if`-statement if `false`.

```javascript
if(enemy) {
    hero.attack(enemy);
}
else {
    hero.say("The path is clear! Run, peasants!")
}
```

Fill out the `if`-statement with a `buildXY` and build a `"fire-trap"` when the hero sees an enemy.

If there isn't an enemy (`else`), the hero should return to the wooden **X** mark.

```javascript
if (enemy) {
    // If there is enemy.
} else {
    // Else there isn't an enemy.
}
```

___
