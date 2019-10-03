## _Convenient Enemy_

#### _Legend says:_
> Scissors cuts paper. Paper covers rock. Rock crushes scissors.

#### _Goals:_
+ _Protect peasants_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **Array Indexing**
+ **For Loops Range**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](convenientEnemy.js)**
+ **[Python](convenient_enemy.py)**

#### _Rewards:_
+ 249 xp
+ 118 gems

#### _Victory words:_
+ _HUMAN INTELLIGENCE IS SO GREAT!_

___

### _HINTS_

The peasants know which ogres are hiding in the forest.

Listen to them by taking the last word they say and summon the right troops to fight the ogres.

When we need to work with text, the `split` function can be really useful. For example, you are given a set of words separated by whitespaces as text. To get a list of words you can use the built-in string method: `someString.split(" ")`:

```javascript
var text = "word other one";
var words = text.split(" ");
hero.say(words[0]);  // word
hero.say(words[1]);  // other
hero.say(words[2]);  // one
```

The `" "` is just the character that the function will split by. It can be anything like `","`, or `"-"` are both common alternatives!

```javascript
var text = "word1,word2,word3";
var words = text.split(",");  // ["word1", "word2", "word3"]
// ...
text = "defend-from-ogres";
words = text.split("-");  // ["defend", "from", "ogres"]
```

___
