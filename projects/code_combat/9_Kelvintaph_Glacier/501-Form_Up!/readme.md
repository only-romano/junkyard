## _Form Up!_

#### _Legend says:_
> We'll make the true soldiers from that crowd.

#### _Goals:_
+ _Form up recruits_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops with Conditionals**
+ **Return Statements**
+ **Object Literals**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](formUp.js)**
+ **[Python](form_up.py)**

#### _Rewards:_
+ 3070 xp
+ 930 gems

#### _Victory words:_
+ _HUP, 2, 3, 4._

___

### _HINTS_

Those soldiers before the gate are new recruits, and aren't trained. We should form up them by their height. Their 'health' property is proportional to their height.

Form up them from the smallest to the biggest (from left to right). Use `command` and predefined functions to make some formation from those recruits.

___

In this level, we'll implement the selection sort algorithm (not-in-place). That algorithm is not effective, but simple.

You have an unsorted array. Create the new empty array, which will contain our sorted data.

```javascript
var unsorted = [10, 12, 3, 1, 2, 6];
var sorted = [];
```

Next, we iterate the unsorted array and find the smallest element.  Remove it from the first array and put in the end of the result array.

```javascript
var smallest = minFunction(unsorted);
result.push(smallest);
unsorted.splice(unsorted.indexOf(smallest), 1);
```

Repeat the last step while the unsorted array isn't empty.

```javascript
while (unsorted.length) {
    // Find the smallest and move it
}
```

For the current level **you don't need to remove elements** (soldiers) from the unsorted array, because soldiers "disappear" from the `recruits` array when you command them.

Don't forget to implement the function for searching of the weakest soldier. You've done it already in previous levels, so it shouldn't be hard.

_Optional (Advanced) information_:

The complexity of that algorithm is `O(N^2)`, where `N` is the number of soldiers.

For the worst case you iterate the array `N` times and for each step it has lengths: `N, N-1,... 2, 1`.

```
N * (N + (N-1) + ... + 3 + 2 + 1) == N * (N + 1) / 2 &lt; N * N
```

___
