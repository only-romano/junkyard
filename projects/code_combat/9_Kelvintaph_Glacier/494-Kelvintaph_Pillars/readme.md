## _Kelvintaph Pillars_

#### _Legend says:_
> An old folk tale describing how to stay warm in Kelvintaph doubles as a fun game.

#### _Goals:_
+ _Move the stack to another tower_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Return Statements**
+ **Array Indexes**
+ **Accessing Properties**
+ **Data Structures - Stacks**

#### _Solutions:_
+ **[JavaScript](kelvintaphPillars.js)**
+ **[Python](kelvintaph_pillars.py)**

#### _Rewards:_
+ 1431 xp
+ 431 gems

#### _Victory words:_
+ _A VACATION IS IN ORDER, MAY WE SUGGEST HANOI?_

___

### _HINTS_

There exists a sect of monks who reside on the highest peaks of Kelvintaph. In subzero temperatures they devised an activity that would keep their bodies warm and their minds active.

They start with 3 pillars, one occupied with discs with a variety of sizes stacked from largest on bottom to smallest on top. They move one disc at a time from one pillar to another without stacking a larger disc on a smaller disc. Completion is when they move the entire stack to another pillar.

Of course your adventuring party doesn't have any pillars or discs, so why not use the _expendable_ exciting peasants and a few stumps?

#### Stacks

Stacks are a type of data structure often seen in Computer Science. It follows a last-in, first-out (LIFO) rule in that the **last** element pushed in is the **first** element popped out. Note the use of `push` and `pop`, as these are the terms used to refer to stack architecture.

You will `push` the latest item onto the top of a stack and then `pop` it off. Along with this comes `peek`ing at the top element to see what it is before popping it off.

In this level you will have access to a set of commands to help with stacking these peasants properly.

```javascript
hero.pickUpItem(target);  // Picks up the top item of a stack.
// (Pops the target's stack and pushes it intoy yours)

hero.dropItem(target);  // Drops the top item of your stack onto another stack.
// (Pops your stack and pushes it into the target's)

hero.peekItem(target);  // Returns the last/top item of your stack.

hero.viewStack();  // Returns an array of the items of your stack with (length - 1)
// being the last/top element

target.peekItem();  // Returns the last/top item of the target's stack.

target.viewStack();  // Returns an array of the item of the target's stack
// with (length - 1) being the last/top element
```

___
