## _Count Emptiness_

#### _Legend says:_
> Too long of pauses. Trim the riddling speech.

#### _Goals:_
+ _Find treasures_

#### _Topics:_
+ **Basic Syntax**
+ **Strings**
+ **Variables**
+ **Functions**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](countEmptyness.js)**
+ **[Python](count_emptiness.py)**

#### _Rewards:_
+ 283 xp
+ 121 gems

#### _Victory words:_
+ _HOW DOES ONE COUNT WHICH ISN'T THERE?_

___

### _HINTS_

Count leading and trailing whitespaces in the Riddler's message. That number is the number of steps that you need to find treasures.

Use `trim` method to cut leading and trailing whitespaces and then compare lengths of the original and trimmed strings to find the required number.

`someStr.trim()` method returns a copy of the string `someStr` with leading and trailing whitespace removed. It's an useful method when you need to **clean** strings before processing.

```javascript
var someStr = "   leading and trailing    ";
var cleaned = someStr.trim();
hero.say(cleaned);  // "leading and trailing"
hero.say(someStr.length);  // 27
hero.say(cleaned.length);  // 20
```

___
