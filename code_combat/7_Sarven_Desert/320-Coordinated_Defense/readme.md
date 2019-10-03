## _Coordinated Defense_

#### _Legend says:_
> Sometimes you must spread out your troops

#### _Goals:_
+ _Protect the peasants_

#### _Topics:_
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Accessing Properties**
+ **Array Indexes**
+ **Array Length**

#### _Solutions:_
+ **[JavaScript](coordinatedDefense.js)**
+ **[Python](coorcinated_derfense.py)**

#### _Rewards:_
+ 257 xp
+ 200 gems

#### _Victory words:_
+ _A BATTLEFIELD BALLET._

___

### _HINTS_

`hero.findEnemies()` returns an array of all the enemies you can see.

Attack the first enemy (index 0) in the array. Your allies will attack the others.

You need to check that the array of enemies isn't empty. One way to do this is to check that the length of the array is greater than 0:

```javascript
var enemies = hero.findEnemies();
if (enemies.length > 0) {
    // 'enemies' contains at least one element.
}
```

The length of an array is the number of elements contained in the array. An empty array has a length of `0`.

It is a good practice to check the length of the array if you need to read elements from it.

If you just need to read the first element, then it's enough to check that the array isn't empty.

```javascript
var items = hero.findItems();
if (items.length) {
    // the length of "items" isn't 0
    hero.say(items[0]);
}
```

However if you are looking for another element like the third element, then you need to check the array length more precisely:

```javascript
if (items.length >= 3) {
    // "items" contains at least 3 elements
    hero.say(items[2]);
}
```

___
