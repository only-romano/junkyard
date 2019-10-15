## _Northwest_

#### _Legend says:_
> Always listen to guides in the Mountains.

#### _Goals:_
+ _Bring the potion to the hero_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Array Length**
+ **Return Statements**
+ **Accessing Properties**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](northwest.js)**
+ **[Python](northwest.py)**

#### _Rewards:_
+ 249 xp
+ 118 gems

#### _Victory words:_
+ _NORTH BY NORTH BY WEST BY WEST._

___

### _HINTS_

Enable your pet hear the nearby peasants giving directions back to the hero.

Check if the string spoken by the peasant matches any of the known words (`"north"`, `"west"`, or `"fetch"`).

Substring searching has two important points. First, how we limit the indexes in the `text` where we search for a `word`. Second, how we use a `shifted index` for letter comparison.

We limit the index we search in the `text` because we are looking for a `word` "inside" of the `text`. For example: `text = "go'wester"` and `word = north`:

```
go'wester|
north    |  <- textIndex = 0
 north   |  <- textIndex = 1 and shiftIndex = 1 + wordIndex
  north  |
   north |
    north|  <- textIndex = text.length - word.length
     nort|h <- That's why we limit the index
```

For each index in `text` we loop through characters in `word`. We **move** (shift) `word` by one letter for each full comparison step. Then we compare `word` and `text` character by character:

```
go'wester   <-  the 'text' we will search inside of for 'word'
  north     <-  the 'word' to search for; the outer loop text Index starting at 2
  01234     <-  wordIndex value; we will search each character in 'word' from 0 to 4
  23456     <-  shifterIndex value; we search in 'text' from 2 to 6 (wordIndex + textIndex)
```

___
