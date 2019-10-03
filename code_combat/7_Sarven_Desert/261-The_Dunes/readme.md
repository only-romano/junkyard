## _The Dunes_

#### _Legend says:_
> Behold, the desert, full of glory, danger, and sand. Lots of sand.

#### _Goals:_
+ _Attack ogres_
+ _Collect all the coins_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Nested If Statements**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](theDunes.js)** _warrior_
+ **[Python](the_dunes.py)** _wizard_

#### _Rewards:_
+ 135 xp
+ 124 gems

#### _Victory words:_
+ _VAST EXPANSES OF TREASURE, GLORY, AND SAND UNFOLD BEFORE YOU._

___

### _HINTS_

Check the `enemy.type` to decide which enemies to attack.

```javascript
if(enemy.type == "sand-yak" || enemy.type == "burl") {
    // Don't attack these types of enemies.
} else {
    // Else it's a different type, so attack.
}
```

Remember the Endangered Burl level? In this level, we check the `enemy.type` property to make sure you attack only ogres, not `"sand-yak"` or `"burl"` enemies.

Sand yaks are mighty, ferocious beasts of varying sizes and speeds. If you attack or get too close to them, they'll trample you in seconds, but if you keep your distance, they'll stay peaceful.

Check out how the sample code uses the **OR** operator:

```javascript
if (enemy.type == "sand-yak" || enemy.type == "burl") {
    // Don't attack! Keep collectiong coins.
}
```

It means, _if_ this _or_ that, _then_... This lets you combine the `"sand-yak"` and `"burl"` type checks into one if statement.

___
