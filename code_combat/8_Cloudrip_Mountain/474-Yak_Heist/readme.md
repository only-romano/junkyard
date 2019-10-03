## _Yak Heist_

#### _Legend says:_
> Big burls need big bait! Find an above average Yak to lay the trap for a Burleous Majorus!

#### _Goals:_
+ _Pick the closest, big yak_
+ _Don't harm any yaks_

#### _Topics:_
+ **Variables**
+ **If Statements**
+ **Return Statements**
+ **Array Indexes**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](yakHunt.js)**
+ **[Python](yak_hunt.py)**

#### _Rewards:_
+ 263 xp
+ 121 gems

#### _Victory words:_
+ _YAKS: HEISTED._

___

### _HINTS_

Senick needs to lay the trap for the Burleous Majorus!

And a big burl needs a big trap... With big bait! Find the closest, above-average sand-yak for Senick to swindle.

In this level you'll need to find the average size of yaks AND find the 'best' yak.

Finding the best yak is no longer a matter of finding the closest, or largest, but the hero must combine these two properties together to find an optimal choice! Instead of checking the distances exclusively, be sure to check the `avgSize` of the Yak as well so Senick doesn't end up grabbing a tiny Yak.

To find the `avgSize` be sure to fill out the `avg` function! Remember how to find an average:

```javascript
var enemies = hero.findEnemies();
var sum = 0;
for (var i = 0; i < enemies.length; i++) {
    sum += enemies[i].health;
}

var avg = sum / enemies.length;
hero.say("The average health of my enemies is: " + avg);
```

___
