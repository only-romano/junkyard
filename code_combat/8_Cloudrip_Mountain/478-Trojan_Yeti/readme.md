## _Trojan Yeti_

#### _Legend says:_
> Do you know that you can use shapeshifters as a time-bomb?

#### _Goals:_
+ _Defeat the ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Return Statements**
+ **Array Length**
+ **Accessing Properties**
+ **Vectors**

#### _Solutions:_
+ **[JavaScript](trojanYeti.js)**
+ **[Python](trojan_yeti.py)**

#### _Rewards:_
+ 283 xp
+ 121 gems

#### _Victory words:_
+ _THE NEFARIOUS YETIS OF TROY._

___

### _HINTS_

Some of our peasants are wereyeti and they will transform soon.

Process the messy list of names from the sergeant and send shapeshifters into the ogre camp.

___

Usually text data isn't **clean** and it must be processed before it can be used. For example, in this level, names in the list are separated by commas and have excess whitespace. To get **clean** names, we need to split the list by commas and then `trim()` leading and trailing whitespaces for each word.

```javascript
var someList = "   words   , split   ,weird,   way";
var words = someList.split(",");
var secondWord = words[1];
console.log(secondWord);  // " split   " -> excess whitespace.
var cleanedSecondWord = secondWord.trim();
console.log(cleanedSecondWord);  // "split" -> it's better.
```

___
