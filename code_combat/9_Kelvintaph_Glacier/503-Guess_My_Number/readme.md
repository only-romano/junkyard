## _Guess My Number_

#### _Legend says:_
> Try to guess the Riddler's number within 10 attempts. Of course, he is cheating, but you can manage it!

#### _Goals:_
+ _Guess the number_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Nested If Statements**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](guessNum.js)**
+ **[Python](guess_num.py)**

#### _Rewards:_
+ 3070 xp
+ 930 gems

#### _Victory words:_
+ _YOU HAVE GUESSED: CORRECT!_

___

### _HINTS_

You have 10 tries to figure out which number the Riddler is thinking of. 

He will tell you higher or lower, and you must divide and conquer this riddle!

Let's play the game. It's simple: Riddler thought of a number, for you to try to guess.

If the number is less or greater than your guess, the Riddler will tell you higher or lower.
Riddler is an infamous cheater, but with 10 attempts you can win anyway.

For each attempt an ogre appears . If it's a Scout (`ogre.type == 'scout'`), then the Riddler's number is less than your guess. If an ogre is a Munchkin (`ogre.type == 'munchkin'`), then the Riddler's number is greater than your guess.

You need to defeat the ogre before saying the next guess!

___
