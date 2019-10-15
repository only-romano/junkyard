## _Quick-Fort_

#### _Legend says:_
> Do ogres annoy you? You feel insecure? Only today - the fast-building fort for 0.99 gold!

#### _Goals:_
+ _Defeat the ogres_
+ _Peasants must survive_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **For Loops**
+ **Array Indexes**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](quickFort.js)**
+ **[Python](quik_fort.py)**

#### _Rewards:_
+ 379 xp
+ 175 gems

#### _Victory words:_
+ _RAPID CONSTRUCTION IN DIRE TIMES._

___

### _HINTS_

We should quickly build a fort!

Each peasant has one speciality and can build only one type of constructions:
1. Carpenter - fences;
2. Mason - towers;
3. Builder - tents.

The foreman mixed their names in one list, but in the specific order. The list looks like [builder, mason, carpenter, builder, mason, carpenter, ...] 

Iterate over all the workers and have them build a tower, tent, or fence. Say the peasant's name outloud as well as their task so they can perform their duties.

___

Ogres often use the valley. It should be easy to block and destroy their army here. We should quickly build a fort!

This is the engineering peasant squad. Each peasant has one speciality and can build only one type of construction. Carpenters can build fences; masons - towers; builders - tents.

The foreman mixed their names in one list, but in a specific order. The list looks like `[builder, mason, carpenter, builder, mason, carpenter, ...]`. Use that list and assign the proper task for each peasant.

`for-loops` could be useful to choose each n-th element from an array. For example: Choose each third element from the array starting from 1st:

```javascript
for (var i = 1; i < array.length; i += 3) {
    hero.say(array[i]);
}
```

___
