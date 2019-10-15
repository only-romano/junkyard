## _Secondary - Wizard_

___


**Table of Contents:**

* [Druid](#druid)
    * [Book of Life I](#book-of-life-I)
    * [Book of Life II](#book-of-life-II)
    * [Book of Life III](#book-of-life-II)
    * [Book of Life IV](#book-of-life-IV)
    * [Book of Life V](#book-of-life-V)
* [Elemental](#elemental)
    * [Elemental Codex I](#elemental-codex-I)
    * [Elemental Codex II](#elemental-codex-II)
    * [Elemental Codex III](#elemental-codex-III)
    * [Elemental Codex IV](#elemental-codex-IV)
    * [Elemental Codex V](#elemental-codex-V)
* [Necromance](#necromance)
    * [Unholy Tome I](#unholy-tome-I)
    * [Unholy Tome II](#unholy-tome-II)
    * [Unholy Tome III](#unholy-tome-III)
    * [Unholy Tome IV](#unholy-tome-IV)
    * [Unholy Tome V](#unholy-tome-V)

___


### _Druid_

___

#### _BOOK OF LIFE I_

Grants Regen, which heals 12 hit points per second for 5 seconds with a 7.5 second cooldown.

![](img/life1.png)

##### _`hero.canCast(spell [, target])`_ method

Whether the given spell is ready. If a target is specified, also checks whether the target can be affected.

**Example:**

```javascript
hero.canCast("drain-life", hero.findNearestEnemy());
```

**Required Parameters:**
+ `spell`: `string` (ex. `"drain-life"`) - _The name of the spell to check_

**Optional Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The unit to check spell efficacy against_

**Returns:**
+ `boolean`

##### _`hero.cast(spell, target)`_ method

Cast a spell at a target. Use `canCast` to see whether the spell is ready, and look at `spellNames` to see which spells are available.

**Example:**

```javascript
hero.cast("drain-life", hero.findNearestEnemy());
```

**Required Parameters:**
+ `spell`: `string` (ex. `"drain-life"`) - _The name of the spell to cast_
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The unit to cast spell on_

##### _`hero.cast("regen", target)`_ method

Casts a `"regen"` spell on `target` if within `30m`, giving the target an extra `20.2` HP every `0.2s` for `5` seconds.

**Level 5 Stats:**
+ Name: `"regen"`
+ Regen: `20.2/0.2s` (`101/s`)
+ Duration: `5s`
+ Range: `30m`
+ Time: `0.75s`
+ Cooldown: `7.5s`

**Example:**

```javascript
hero.cast("regen", hero);
```

**Required Parameters:**
+ `target`: `object` (ex. `hero`) - _The target to regenerate_


##### _`hero.spellNames`_ property

The names of the spells this hero can cast.

___

#### _BOOK OF LIFE II_

Grants Shrink, which halves a target's health and doubles its speed for 5 seconds with a cooldown of 7.5 seconds. Increases Regen to restore 17.5 health per second.

![](img/life2.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("regen", target)`
+ `hero.spellNames`

##### _`hero.cast("shrink", target)`_ method

Casts a `"shrink"` spell on `target` if within `30m`, causing shrinkage, faster movement by a factor of `2`, and weaker attacks by a factor of `0,5` for `5` seconds.

**Level 5 Stats:**
+ Name: `"shrink"`
+ Health: `-50%`
+ Scale: `-1`
+ Speed: `+100%`
+ Duration: `5s`
+ Range: `30m`
+ Time: `0.75s`
+ Cooldown: `1.3s`

**Example:**

```javascript
hero.cast("shrink", hero.getNearestEnemy());
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.getNearestEnemy()`) - _The target to shrink_


##### _`hero.spells`_ property

Which spells this hero can cast.

___

#### _BOOK OF LIFE III_

Grants Grow, which doubles a target's health and halves its speed for 5 seconds with a 7.5 second cooldown. Increases Regen's healing to 36 hit points per second. Lowers Shrink's cooldown to 3.7 seconds.

![](img/life3.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("regen", target)`
+ `hero.cast("shrink", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("grow", target)`_ method

Casts a `"grow"` spell on `target` if within `30m`, causing growth, slower movement by a factor of `0.5`; and greater health and stronger attacks by a factor of `2` for `5` seconds.

**Level 5 Stats:**
+ Name: `"grow"`
+ Health: `+100%`
+ Scale: `+1`
+ Speed: `-50%`
+ Duration: `5s`
+ Range: `30m`
+ Time: `0.75s`
+ Cooldown: `1.3s`

**Example:**

```javascript
hero.cast("grow", target);
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.findNearestFriend()`) - _The target to grow_

___

#### _BOOK OF LIFE IV_

Grants Time Warp. Increases Regeneration to 51.5 hit points per second. Reduces the Shrink and Grow cooldowns to 2.6 seconds.

![](img/life4.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("grow", target)`
+ `hero.cast("regen", target)`
+ `hero.cast("shrink", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("time-warp")`_ method

Casts a mighty `'time-warp'` spell, which adjusts the speed of all units (including the `hero` and any `missiles`) caught within `20m` by a factor of `0.25` for `4s`.

**Level 5 Stats:**
+ Name: `"time-warp"`
+ Speed: `-75%`
+ Duration: `4s`
+ Range: `20m`
+ Time: `0.5s`
+ Cooldown: `7.5s`

**Example:**

```javascript
hero.cast("time-warp");
```

___

#### _BOOK OF LIFE V_

Enables Dispel. Increases Regen to 101 hit points per second. Reduces Grow and Shrink cooldown times to 1.3 seconds.

![](img/Life5.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("grow", target)`
+ `hero.cast("regen", target)`
+ `hero.cast("shrink", target)`
+ `hero.cast("time-warp")`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("dispel", target)`_ method

Casts a `"dispel"` spell on `target` if within `40m`, dispeling all effects.

**Level 5 Stats:**
+ Name: `"dispel"`
+ Range: `40m`
+ Time: `0.4s`
+ Cooldown: `2s`

**Example:**

```javascript
if (hero.canCast("dispel", enemy) && enemy.hasEffect("grow")) {
    hero.cast("dispel", enemy);
}
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The target on which to cast "dispel"_

___


### _Elemental_

___

#### _ELEMENTAL CODEX I_

Grants Haste, which increases speed 2x for 4.5 seconds with a 10 second cooldown.

![](img/elemet1.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.spellNames`

##### _`hero.cast("haste", target)`_ method

Casts a `"haste"` spell on `target` if within 30m, causing faster movement and attack speed by a factor of `2` for `5` seconds.

+ Name: `"haste"`
+ Speed: `+ 100%`
+ Duration: `5s`
+ Range: `30m`
+ Time: `0.5s`
+ Cooldown: `10s`

**Example:**

```javascript
hero.cast("haste", hero);
```

**Required Parameters:**
+ `target`: `object` (ex. `hero`) - _The target to haste_

___

#### _ELEMENTAL CODEX II_

Grants Slow, which reduces a target's speed by 50% for 5 seconds with a 10 second cooldown.

![](img/elemet2.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("haste", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("slow", target)`_ method

Casts a `"slow"` spell on target if within `30m`, slowing down its movement and attack (and all passage of time) by a factor of `0.5` for `5` seconds.

+ Name: `"slow"`
+ Speed: `- 50%`
+ Duration: `5s`
+ Range: `30m`
+ Time: `0.5s`
+ Cooldown: `10s`

**Example:**

```javascript
hero.cast("slow", hero.findNearestEnemy());
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The target on which to cast "slow"_

___

#### _ELEMENTAL CODEX III_

Grants Shockwave, which deals 50 damage to enemies in a 20 meter radius around the target and knocks them back. Shockwave has a 15 second cooldown.

![](img/elemet3.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("haste", target)`
+ `hero.cast("slow", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("shockwave", target)`_ method

Casts a `"shockwave"` spell on `target` if within `20m`, blasting it back away from the caster and dealing up to `spells.shockwave.damage` to units caught in the epicenter.

**Level 5 Stats:**
+ Name: `"shockwave"`
+ Damage: `125`
+ Range: `20m`
+ Time: `0.75s`
+ Cooldown: `15s`

**Example:**

```javascript
hero.cast("shockwave", hero.findNearestEnemy());
```

**Optional Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The target on which to cast "shockwave", if not centered on caster._

___

#### _ELEMENTAL CODEX IV_

Grants Swap. Increases Shockwave's damage to 79 with increased knockback.

![](img/elemet4.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("haste", target)`
+ `hero.cast("shockwave", target)`
+ `hero.cast("slow", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("swap", target)`_ method

Casts a `"swap"` spell on `target` if within `30m`, swapping its position with yours.

+ Name: `"swap"`
+ Range: `30m`
+ Time: `0.25s`
+ Cooldown: `5s`

**Example:**

```javascript
hero.cast("swap", hero.findNearestEnemy());
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The target on which to cast "swap"_

___

#### _ELEMENTAL CODEX V_

Grants Flame Armor. Increases Shockwave's damage to 125 with increased knockback.

![](img/elemet5.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("haste", target)`
+ `hero.cast("shockwave", target)`
+ `hero.cast("slow", target)`
+ `hero.cast("swap", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("flame-armor", target)`_ method

Casts a `"flame-armor"` spell on `target` if within `40m`, granting `1.4` `health` and `maxHealth` for `10` seconds. During that time, any enemy that attacks with a melee weapon takes `30` damage each time they attack.

+ Name: `"flame-armor"`
+ Damage: `30`
+ Health: `+40%`
+ Range: `40m`
+ Time: `0.5s`
+ Cooldown: `5s`

**Example:**

```javascript
hero.cast("flame-armor", hero);
```

**Required Parameters:**
+ `target`: `object` (ex. `hero`) - _The target on which to cast "flame-armor"_

___


### _Necromance_

___

#### _UNHOLY TOME I_

Grants Drain Life, which drains 8 DPS from a target up to 15 meters away.

![](img/unholy1.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.spellNames`

##### _`hero.cast("drain-life", target)`_ method

Casts a `"drain-life"` spell on `target` if within `15m`, stealing `6` health from it and giving it to the hero.

**Level 5 Stats:**
+ Name: `"drain-life""`
+ Damage: `57.1`
+ Heals: `57.1`
+ Range: `15m`
+ Time: `0.75s`
+ Cooldown: --

**Example:**

```javascript
hero.cast("drain-life", hero.findNearestEnemy());
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The target on which to cast "drain-life"_

___

#### _UNHOLY TOME II_

Grants Fear, which causes a target enemy to flee for 5 seconds with a 10 second cooldown. Drain Life increased to 18 DPS.

![](img/unholy2.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("drain-life", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("fear", target)`_ method

Casts a `"fear"` spell on `target` if within 25m, causing it to run in terror for 5 seconds.

**Level 5 Stats:**
+ Name: `"fear""`
+ Duration: `5s`
+ Range: `25m`
+ Time: `0.75s`
+ Cooldown: `10s`

**Example:**

```javascript
hero.cast("fear", hero.findNearestEnemy());
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The target on which to cast "fear"_

___

#### _UNHOLY TOME III_

Enables Raise-Dead, which raises 100 power worth of dead units at half health for 10 seconds at random in a 20 meter range. Drain Life DPS increased to 24.

![](img/unholy3.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("drain-life", target)`
+ `hero.cast("fear", target)`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("raise-dead")`_ method

Casts a `'raise-dead'` spell, bringing back `1200` power worth of corpses back to life as zombies for `10` at half health and speed. The zombies are chosen randomly from corpses within `20m`.

**Level 5 Stats:**
+ Name: `"raise-dead""`
+ Power: `1200`
+ Radius: `20m`
+ Duration: `10s`
+ Time: `0.5s`
+ Cooldown: `10s`

**Example:**

```javascript
if (hero.canCast('raise-dead'))
    hero.cast('raise-dead');
```

##### _`hero.findCorpses()`_ method

Returns an `array` of all dead units (friend and foe alike).

___

#### _UNHOLY TOME IV_

Grants Poison Cloud, which deals 30 DPS for 5s in a 10 meter range and has a 15-second cooldown. Increases Drain Life DPS to 45. Increases the total power of targets Raise Dead can affect.

![](img/unholy4.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("drain-life", target)`
+ `hero.cast("fear", target)`
+ `hero.cast("raise-dead")`
+ `hero.findCorpses()`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("poison-cloud", target)`_ method

Casts a `"poison-cloud"` spell on `target` if within `30m`, poisoning every unit within a radius of `10`.

**Level 5 Stats:**
+ Name: `"poison-cloud""`
+ Damage: `50/s`
+ Duration: `5s`
+ Range: `30m`
+ Radius: `10m`
+ Time: `0.75s`
+ Cooldown: `15s`

**Example:**

```javascript
hero.cast("poison-cloud", hero.findNearestEnemy());
```

**Required Parameters:**
+ `target`: `object` (ex. `hero.findNearestEnemy()`) - _The target unit or position to poison_

___

#### _UNHOLY TOME V_

Grants Summon Undead. Increases Drain Life DPS to 76. Increases the number of targets Raise Dead affects. Increases Poison Cloud DPS to 50.

![](img/unholy5.png)

+ `hero.canCast(spell [, target])`
+ `hero.cast(spell, target)`
+ `hero.cast("drain-life", target)`
+ `hero.cast("fear", target)`
+ `hero.cast("poison-cloud", target)`
+ `hero.cast("raise-dead")`
+ `hero.findCorpses()`
+ `hero.spellNames`
+ `hero.spells`

##### _`hero.cast("summon-undead")`_ method

Casts a `"summon-undead"` spell to summon `2` undead minions.

**Level 5 Stats:**
+ Name: `"summon-undead""`
+ Count: `2`
+ Time: `0.75s`
+ Cooldown: `7.5s`

**Example:**

```javascript
hero.cast("summon-undead");
```

___
