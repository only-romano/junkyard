## _Reindeer Tender_

#### _Legend says:_
> Put the reindeer down in their pens by checking and modifying arrays.

#### _Goals:_
+ _Assign reindeer to pens_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Array Length**
+ **Object Literals**
+ **Accessing Properties**
+ **Assigning Properties**

#### _Solutions:_
+ **[JavaScript](reindeerTender.js)**
+ **[Python](reindeer_tender.py)**

#### _Rewards:_
+ 259 xp
+ 119 gems

#### _Victory words:_
+ _ALL THAT BLITZING AND DASHING THROUGH THE SNOW TUCKERED THEM OUT!_

___

### _HINTS_

These reindeer have had a long day of playing in the snow, eating hay, and whatever else it is that reindeer do. Now you need to put them in their pens so they can get some sleep.

Use arrays to keep track of which pens already have reindeer in them, and assign the other reindeer to empty stalls.

___

In this level, you will use _arrays_ to organize the reindeer. You start with three arrays:
1. An array of positions that the reindeer will go to.
2. An array that is used to mark which reindeer are in which pens.
3. An array of the reindeer themselves.

The first step is to figure out which reindeer are already in their pens. To do this, loop through the reindeer. For each one, loop through each pen position. If the pen position matches the reindeer's position, it's already there. Use the `penOccupants` and `friends` arrays to keep track of which reindeer are already asleep -- when a reindeer is in a pen, move the reindeer from the `friends` array to the `penOccupants` array to track it.

Next, you'll go through the `friends` array again to look at the remaining reindeer (the ones that _aren't_ already in pens). For each one, Look through the `penOccupants` array for the first spot that _doesn't_ have a reindeer in it. When you find one, command the reindeer to move to the spot.

If everything goes well, you'll have one reindeer sleeping peacefully in each pen!

By now, you're used to looping over arrays using `while` and `for` loops:

```javascript
for (var i = 0; i < enemies.length; i++) {
    var enemy = enemies[i];
}
```

But you can access any element of an array at any time in any order, as long as it exists:

```javascript
var a = [ null, "one", "two" ];
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

You'll need to change the `penOccupants` and `friends` arrays quite a bit to get through this level!

___
