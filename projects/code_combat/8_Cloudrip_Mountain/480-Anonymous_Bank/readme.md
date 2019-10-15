## _Anonymous Bank_

#### _Legend says:_
> You don't need your ID to get money, only passwords.

#### _Goals:_
+ _Get treasures_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Array Indexes**
+ **Array Length**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](anonBank.js)**
+ **[Python](anon_bank.py)**

#### _Rewards:_
+ 283 xp
+ 121 gems

#### _Victory words:_
+ _"A HASTY WITHDRAWAL."_

___

### _HINTS_

To get to the treasures you need 4 passwords. Luckily, we caught a scout that had the passwords. Now, we just need to decipher the message to get them.

Words in the message are split by `;` and can be surrounded by redundant whitespaces. Also, we know that the passwords in the message only have 5 letters.

In this level you need to use various skills from recent levels. You will want to make use the following methods:

```javascript
someStr.split(separator);  // To get an array of words;
word.trim();  // To remove leading and trailing whitespaces;
cleannedWord.length;  // To get the word's length;
```

___
