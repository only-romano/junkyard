## _Reindeer Wakeup_

#### _Legend says:_
> Help the blind herder wake up his reindeer by using arrays to track them.

#### _Goals:_
+ _Call out the sleeping reindeer_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Array Indexes**
+ **Array Length**
+ **Accessing Properties**
+ **Assigning Properties**

#### _Solutions:_
+ **[JavaScript](raindeerWakeup.js)**
+ **[Python](raindeer_wakeup.py)**

#### _Rewards:_
+ 259 xp
+ 119 gems

#### _Victory words:_
+ _PUT ON A LITTLE MAKEUP!_

___

### _HINTS_

It's time for the reindeer to get up and start their day! Merek the old herder is the only one they'll listen to, but he's blind and needs help to tell who's awake and who's asleep.

Use an _array_ to keep track of which reindeer are awake and in the field, and which are asleep in their pens. Tell Merek which reindeer are awake, and then he'll tell them to get up and play.

___

In this level, you will use _arrays_ to keep track of the reindeer. You start with two arrays:
1. An array that is used to mark which reindeer are asleep and which are awake;
2. An array of the reindeer themselves.

The first step is to figure out which reindeer are awake. To do this, loop through the reindeer. For each one, check its position. If its Y coordinate is more than 30, then it's not in its pen and it must be awake. When a reindeer is awake, mark its slot in the `deerStatus` array to "awake".

After figuring out which reindeer are up, loop through the `deerStatus` array and tell Merek what's what. If he hears you say that a reindeer is "asleep", he'll command it to wake up.

If everything goes well, all the reindeer will be awake and ready to start the day!

By now, you're used to looping over arrays using `while` and `for` loops:

```javascript
for (var i = 0; i < enemies.length; i++) {
    var enemy = enemies[i];
}
```

But you can access any element of an array at any time in any order, as long as it exists:

```javascript
var  a = [null, "one". "two"];
hero.say(a[1]);  // Says "one"
hero.say(a[2]);  // Says "two"
hero.say(a[0]);  // Says nothing
hero.say(a[3]);  // Error! Array starts at 0 and ends at 2.
```

You can also change the elements of an array however you like:

```javascript
var a = [null, "no", "maybe"];
hero.say(a[1]);  // Says "no"
a[1] = "yes";
hero.say(a[1]);  // Says "yes"
```

You'll have to make some changes to the `deerStatus` array to solve this level!

___
