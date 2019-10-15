## _Vision of Ogres_

#### _Legend says:_
> Ogres have the Illusion spell, but we know how it works.

#### _Goals:_
+ _Defeat the ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **While Loops with Conditionals**
+ **Return Statements**
+ **For Loops Range**

#### _Solutions:_
+ **[JavaScript](visionOfOgres.js)**
+ **[Python](vision_of_ogres.py)**

#### _Rewards:_
+ 283 xp
+ 121 gems

#### _Victory words:_
+ _PRETTY SNEAKY, ILLUSIONS._

___

### _HINTS_

Only one of ogres in each wave is real. Destroy him and others will fall. You can recognize real ogres by name. Each has three words in their name. The real ogre has **a middle name which starts and ends with the same letter (case-irrelevant)**.

Don't forget to use the lower-case function to avoid case comparison problems.

P.S.: Don't break mirrors, splinters are sharp.

In this level you need to use various skills from recent levels. Use the following methods:

```javascript
var words = someStr.split(separator);  // To get an array of words;
var lowerWord = word.toLowerCase();  // To remove leading and trailing whitespaces;
lowwerWord[0];  // The first letter
lowerWord[lowerWord.length];  // The last letter
```

Don't forget to use the lower-case function to avoid case comparison problems.

```javascript
var word = "Aahz";
hero.say(word[0] == word[1]);  // false
word = word.toLowerCase();
hero.say(word[0] == word[1]);  // true
```

___
