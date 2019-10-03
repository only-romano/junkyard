## _Snowdrops_

#### _Legend says:_
> I love the spring! Look! Snowdrops are budding and piercing through the snow! Wait, on second thought, those are definitely not flowers.

#### _Goals:_
+ _Clear forest from firetraps_
+ _Nobody should be hurt_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Array Indexes**
+ **Array Length**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](snowdrops.js)**
+ **[Python](snowdrops.py)**

#### _Rewards:_
+ 566 xp
+ 191 gems

#### _Victory words:_
+ _EACH ARTILLERY SHELL IS A UNIQUE SNOWFLAKE._

___

### _HINTS_

Spring is coming! The time for the big cleaning! We need to clear the forest and we have the cannon and the forest map for that. But the map has rows with different lengths, so be sure before a shot. We can't afford to shoot everywhere - ammo is expensive and we have just enough to clean traps.

The map is an array of arrays, where 1 is clear and 0 is a trap. Like:

```
[[1, 1, 0],
 [0, 1],
 [1, 1, 0, 0, 1]]
```

Say the row and the column of the map where the artillery should shoot.
We prepared the cell coordinates (you'll find them in the sample code) which you need to check.

___

The map is an array of arrays, where 1 is clear and 0 is a trap. Like:

```javascript
var forestMap = [
    [1, 1, 0],
    [0, 1],
    [1, 1, 0, 0, 1]
];
```

As we can see rows of that arrays have different lengths. So we need to check the correctness of coordinates before to get access, else you can get an error.

```javascript
// The correct row, but the wrong column:
forestMap[0][4];  // undefined
// The wrong row, any column
forestMap[5][1];  // TypeError, because forestMap[5] is undefined
```

It's a good practice to check indexes before access them if you aren't sure it. For example, if you get access to random cell by random or outer source coordinates.

To check the existence of the cell you can check if it's less than the length of the array (We don't consider negative indexes here):

```javascript
var row = 1;
var col = 3;
if (row < forestMap.length) {
    // if 'row' is correct index
    if (col < forestMap[row].length) {
        // now we can get the cell
        hero.say(forestMap[row][col]);
    }
}
```

It can be written shorter with logic operators:

```javascript
// The second part is checked only if the first is true
if (row < forestMap.length && col < forestMap[row].length) {
    hero.say(forestMap[row][col]);
}
```

___
