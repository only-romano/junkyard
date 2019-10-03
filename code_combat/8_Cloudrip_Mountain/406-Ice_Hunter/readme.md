## _Ice Hunter_

#### _Legend says:_
> Not all yaks are the same. Don't vex the big old yaks.

#### _Goals:_
+ _Hunt for 4 yaks_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops with Conditionals**
+ **Return Statements**
+ **Accessing Properties**
+ **For Loops Range**

#### _Solutions:_
+ **[JavaScript](iceHunter.js)**
+ **[Python](ice_hunter.py)**

#### _Rewards:_
+ 249 xp
+ 118 gems

#### _Victory words:_
+ _THIS HIDE WILL HELP KEEP YOU WARM!_

___

### _HINTS_

Defeat the 4 yaks that have `"bos"` in their name.

Use the provided `isSubstring(word, substring)` function to check if a yak's `id` has the string `"bos"` in it.

___

The predefined function `isSubstring` is an implementation naive (brute-force) algorithm. We begin by iterating through the `index`’s in `word`, but we don't need iterate all of the indexes. We can stop at the `index` of `word.length - substring.length` because any further than that would prevent us from checking every character of the substring.

```javascript
function isSubstring(word, substring) {
    var rightEdge = word.length - substring.length;
    for (var i = 0; i <= rightEdge; i++) {
        // ...
    }
}
```

For example:

```
word = "Nachos"

sub = "hos"

We "shift" substring

Nachos
hos
 hos
  hos
   hos
```

As we can see if we move `substring` any futher then that it goes outside of the `word`.

Next, for each word's index we loop through indexes in `substring` and compare each letter in `substring` with the letter in `word`. We do this with the offset location `wordIndex + subIndex`. If any of letters don't coincide with a pair, then we `break` out of a loop and go to the next index in `word`.

```javascript
for (var j = 0; j < substring.length; j++) {
    var shiftedIndex = i + j;
    if (word[shiftedIndex] != substring[j]) {
        break;
    }
}
```

If we iterate through all letters in `substring` and haven't called `break` then it means what we have found the `substring`. To ensure we are at the last index we can compare `substring`’s index to be sure that it was the last index in `substring`.

```javascript
if (j == substring.length - 1) {
    return true;
}
```

If all loops end and we haven't found the `substring` then return `false`.

Your task is to call the function with arguments and use this result. Read through the the function code carefully because it will be helpful for upcoming levels.

___
