## _The One Wizard_

#### _Legend says:_
> Challenge: defeat ogres using all the programming skills you've learned so far!

#### _Goals:_
+ _Defeat at least 12 ogres_
+ _Bonus: Defeat 17 ogres_
+ _Bonus: Defeat 32 ogres_
+ _Bonus: Defeat 44 ogres_

#### _Topics:_
+ **Basic Syntax**

#### _Items we've got (- or need):_
+ None

#### _Solutions:_
+ **[JavaScript](oneWizard.js)**
+ **[Python](one_wizard.py)**

#### _Rewards:_
+ 68-187 xp
+ 41-111 gems

#### _Victory words:_
+ _BE CAREFUL WITH MAGIC. DANGEROUS BUT FRAGILE. THE MAGIC IS MY SWORD AND ARMOR. YOUR MIND IS TRUE MAGIC._

___

### _HINTS_

![](img/librarian-pose-width.png)

It's time for another **special Challenge Level**!

You need to know how to use wizard spells.

Use `hero.cast("spell-name", spellTarget)` to cast `"spell-name"` at `spellTarget`.

Spells have a cooldown period (similar to abilities like cleave) so it's best to check if if a spell is ready with `hero.canCast`.

You can tell if a spell is ready with `hero.canCast("spell-name")` which returns `true` of `false` like `hero.isReady`.

```javascript
if (hero.canCast("chain-lighting")) {
    hero.cast("chain-lightning", enemy);
}
```

Read the Hints to learn more about available spells.

Solve this puzzle by **creatively** using all of the coding skills you’ve learned so far.

There is more than one way to complete this level; try to find a solution that **defeat the most ogres**!

___

The wizard uses a wand which is a ranged weapon. The attack range is `30m`.

On this level you can use three spells:
+ `"lightning-bolt"` is a powerful spell which hits one unit. It doesn't have range limit and can be cast on any enemy which you see. Cooldown: `10s`, Damage: `300hp`.
+ `"chain-lightning"` hits up to `12` enemies who are close to each other in a row. It has the same attack range as your wand: `30m`. Cooldown: `15s`. Damage: `200-50hp`.
+ `"regen"` is a healing spell. After casting it on yourself the spell heals `12hp/s` for `5s`. Cooldown: `5s`.

___

Have you noticed the button on the ground to your left? Step on it and the ogres will be in trouble.

However you can use it only once, so it's better to use in an emergency only.

You can detect big ogres by their `type`:

```javascript
if (enemy.type == "ogre") {
    // ...
}
```

Spells take time to cast (`0.75s`) so for some spells with short cooldown, you can "spam" yourself by casting repeatedly.

For example, `regen` duration is `5s` but the cooldown is `2s` with `0.75s` casting time. So maybe it's better to wait for a quiet moment to cast it.

___
