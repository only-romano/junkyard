## _Cluttered Corridors_

#### _Legend says:_
> Somebody should put this place in order.

#### _Goals:_
+ _Help the pet find the exit_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **If Statements**
+ **Nested If Statements**
+ **Accessing Properties**
+ **Event Data**

#### _Solutions:_
+ **[JavaScript](clutteredCorridors.js)**
+ **[Python](cluttered_corridors.py)**

#### _Rewards:_
+ 249 xp
+ 118 gems

#### _Victory words:_
+ _WHEN YOU'RE A GIANT CAT, THE WORLD IS YOUR LITTER BOX._

___

### _HINTS_

Help the pet find the exit to this cluttered room full of boxes.

Listen for hints from the statues, they know the route. One little problem -- they aren't good with letter cases.

One of the good uses of string conversion to lower/upper case is **case-irrelevant** comparison. For the computer the `"A"` and `"a"` are different letters therefore `"CodeCombat" != "codecombat"`.

To compare without case we can convert both of words (texts) to lower/upper case and then compare them.

```javascript
var word1 = "HerO";
var word2 = "hERo";
// "HerO" != "hERo"
if (word1 == word2) {
    hero.say("It'll never happen.");
}
if (word1.toLowerCase() == word2.toLowerCase()) {
    hero.say("hero is hero");
}
```

Sometimes it can be usefull convert and reassign variables:

```javascript
var phrase = "wEIRD phrAsE";
phrase = phrase.toLowerCase();
if (phrase == "weird phrase") {
    hero.say("Now it's better");
}
```

___
