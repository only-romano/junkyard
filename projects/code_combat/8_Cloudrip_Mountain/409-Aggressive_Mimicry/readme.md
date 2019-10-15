## _Aggressive Mimicry_

#### _Legend says:_
> Watch for wolves in sheep's clothing.

#### _Goals:_
+ _Protect the village_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Array Indexes**
+ **Return Statements**
+ **For Loops Range**

#### _Solutions:_
+ **[JavaScript](aggressiveMimicry.js)**
+ **[Python](aggressive_mimicry.py)**

#### _Rewards:_
+ 249 xp
+ 118 gems

#### _Victory words:_
+ _WHERE DO THESE OGRES GET SUCH DARK COPY MAGICKS!?_

___

### _HINTS_

The mimics are coming! Ogres have disguised themselves as peasants.

Check for any friends that have `"Zog"` at the start of their name and attack!

Be sure to let real peasants through, and, attack any actual ogres.

When we check if the `text` starts with a word the first thing we should do is compare their length. If `text` is shorter than word then we know word cannot be inside text and the result is `false`.

```javascript
function startsWith(text, word) {
    if (text.length < word.length) {
        return false;
    }
    // ...
}
```

Next we compare the letters in `text` and word with the same indexes. If any of the pairs don't coincide, then the text does not match the word and the result is `false`.

```javascript
for (var index = 0; index < word.length; index++) {
    if (word[index] != text[index]) {
        return false;
    }
}
```

If we reach the end of the loop, it means that all the letters in word are also text. So we can say for sure, that text starts with word.

___
