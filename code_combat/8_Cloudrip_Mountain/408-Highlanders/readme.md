## _Highlanders_

#### _Legend says:_
> Ogres are using black magic! Only the highlanders are immune.

#### _Goals:_
+ _Win the battle_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Array Indexes**
+ **Array Length**
+ **Return Statements**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](highlanders.js)**
+ **[Python](highlanders.py)**

#### _Rewards:_
+ 249 xp
+ 116 gems

#### _Victory words:_
+ _THERE CAN ONLY BE ONE! OR A FEW... OR A WHOLE SQUAD!_

___

### _HINTS_

Those weird statues near the gates contain the blackest magic!

Pass through it without a shield and you will lose your soldiers.

Only send forth the magic-immune highlanders! Search through your friend's names to find which ones are highlanders.

In this level you need to only send forward soldiers with `"mac"` in their name.

Searching through strings is tough work, but consider each part step-by-step! Programmtically, if you will:

```javascript
var haystack = "Hello, world!";
var needle = "o, w";
var needleIndex = 0;
for (var i = 0; i < haystack.length; i++) {
    var letter = haystack[i];
    // Check the letter matches the letter at the current needleIndex
    if (letter === needle[needleIndex]) {
        // Increment the index by one so in the next iteration of the for-loop
        // Thes checks if the substring is still valid on a letter-by-letter basis.
        needleIndex += 1;
        // Check if the needle index is greater than needle length
        if (needleIndex >= needle.length) {
            // Since we've gone through each index of our needle string, we know it exists!
            hero.say("Yep! " + needle + " is in " + haystack + "!");
            break;
        }
    } else {
        // Reset the index because the potential sub-string no longer matches
        needleIndex = 0;
    }
}
```

___
