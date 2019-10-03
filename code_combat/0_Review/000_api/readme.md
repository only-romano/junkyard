## Code Combat API

___


**Table of Contents:**

* [Math](#math)
    + [PI](#pi)
    + [Abs](#abs)
    + [Atan2](#atan2)
    + [Ceil](#ceil)
    + [Cos](#cos)
    + [Floor](#floor)
    + [Max](#max)
    + [Min](#min)
    + [Pow](#pow)
    + [Random](#random)
    + [Round](#round)
    + [Sin](#sin)
    + [Sqrt](#sqrt)
    + [Tan](#tan)
* [Array](#array)
    + [Concat](#concat)
    + [Entries](#entries)
    + [Every](#every)
    + [Filter](#filter)
    + [Find](#find)
    + [Find Index](#find-index)
    + [For Each](#for-each)
    + [Index Of](#index-of)
    + [Is Array](#is-array)
    + [Join](#join)
    + [Keys](#keys)
    + [Last Index Of](#last-index-of)
    + [Map](#map)
    + [Pop](#pop)
    + [Push](#push)
    + [Reduce](#reduce)
    + [Reduce Right](#reduce-right)
    + [Reverse](#reverse)
    + [Shift](#shift)
    + [Slice](#slice)
    + [Some](#some)
    + [Sort](#sort)
    + [Splice](#splice)
    + [To Local String](#to-local-string)
    + [To String](#to-string)
    + [Unshift](#unshift)

___


## Math

___

### _PI_

`Math.PI`

The ratio of the circumference of a circle to its diameter, approximately `3.14159`.

___

### _ABS_

`Math.abs(x)`

Returns the absolute value of a number. (It turns negative numbers into positive numbers, like `-6` -> `6`)

**Example:**

```javascript
Math.abs(-6);
```

**Required Parameters:**
+ `x`: `number` (ex. `-6`)

___

### _Atan2_

`Math.atan2(y, x)`

Returns the arctangent of the quotient of its arguments--a numeric value between `-π` and `π` representing the counterclockwise angle theta of an (`x, y`) point and the positive X axis.

**Example:**

```javascript
Math.atan2(90, 15);
```

**Required Parameters:**
+ `y`: `number` (ex. `90`)
+ `x`: `number` (ex. `15`)

___

### _Ceil_

`Math.ceil(x)`

Returns the smallest integer greater than or equal to a number.

**Example:**

```javascript
Math.ceil(5.5);
```

**Required Parameters:**
+ `x`: `number` (ex. `5.5`)

___

### _Cos_

`Math.cos(theta)`

Returns the cosine of a number (between -1 and 1).

**Example:**

```javascript
Math.cos(Math.PI / 4);
```

**Required Parameters:**
+ `theta`: `number` (ex. `Math.PI /4`) - _A number in radians_

___

### _Floor_

`Math.floor(x)`

largest integer less than or equal to a number.

**Example:**

```javascript
Math.floor(5.5);
```

**Required Parameters:**
+ `x`: `number` (ex. `5.5`)

___

### _Max_

`Math.max(args)`

Returns the largest of zero or more numbers.

**Example:**

```javascript
Math.max(hero.pos.x, 0, (etc));
```

**Required Parameters:**
+ `args`: `numbers` (ex. `0`) - _It takes as many arguments as you give it_

___

### _Min_

`Math.min(args)`

Returns the smallest of zero or more numbers.

**Example:**

```javascript
Math.min(hero.pos.x, 80, (etc));
```

**Required Parameters:**
+ `args`: `numbers` (ex. `80`) - _It takes as many arguments as you give it_

___

### _Pow_

`Math.pow(base, exponent)`

Returns `base` to the `exponent` power.

**Example:**

```javascript
Math.pow(7, 2);
```

**Required Parameters:**
+ `base`: `number` (ex. `7`) - _The base number_
+ `exponent`: `number` (ex. `2`) - _The exponent used to raise the `base`_

___

### _Random_

`Math.random()`

Returns a random number `x` such that `0 <= x < 1`

___

### _Round_

`Math.round(x)`

Returns the value of a number rounded to the nearest integer. It rounds to the next higher integer when the fractional part is .5.

**Example:**

```javascript
Math.round(5.5);
```

**Required Parameters:**
+ `x`: `number` (ex. `5.5`)

___

### _Sin_

`Math.sin(theta)`

Returns the sine of a number (between -1 and 1).

**Example:**

```javascript
Math.sin(Math.PI / 4);
```

**Required Parameters:**
+ `theta`: `number` (ex. `Math.PI /4`) - _A number in radians_

___

### _Sqrt_

`Math.sqrt(x)`

Returns the square root of a non-negative number. Equivalent to `Math.pow(x, 0.5)`.

**Example:**

```javascript
Math.sqrt(49);
```

**Required Parameters:**
+ `x`: `number` (ex. `49`)

___

### _Tan_

`Math.tan(theta)`

Returns the tangent of a number (between -1 and 1).

**Example:**

```javascript
Math.tan(Math.PI / 4);
```

**Required Parameters:**
+ `theta`: `number` (ex. `Math.PI /4`) - _A number in radians_

___


## Array

___

### _Concat_

`array.concat(args)`

The `concat()` method returns a `new array` comprised of the elements of the array on which it was called joined with other array(s) and/or value(s).

**Example:**

```javascript
var array1 = ["a", "b", "c"];
var array2 = [1, 2, 3];
var array3 = [4, 5, 6, 7];

 // creates array ["a", "b", "c", 1, 2, 3]; array1 and array2 are unchanged.
var newarray1 = array1.concat(array2);  

//creates array ["a", "b", "c", 1, 2, 3, 4, 5, 6, 7]; array1,array2,array3 are unchanged.
var newarray2 = array1.concat(array2, array3);
```

**Required Parameters:**
+ `args`: `arrays` (ex. `[1, 2, 3]`)

**Returns:**
+ `array`

___

### _Entries_

`array.entries()`

The `entries()` method returns a new `Array Iterator` object that contains the key/value pairs for each index in the array.

**Example:**

```javascript
var arr = ["a", "b", "c"];
var eArr = arr.entries();

hero.say(eArr.next().value); // [0, "a"]
hero.say(eArr.next().value); // [1, "b"]
hero.say(eArr.next().value); // [2, "c"]
```

**Returns:**
+ `array iterator`

___

### _Every_

`array.every(validator)`

The `every()` method tests whether **all elements** in the array pass the test implemented by the provided function.

**Example:**

```javascript
function isBigEnough(element, index, array) {
  return (element >= 10);
}
var passed = [12, 5, 8, 130, 44].every(isBigEnough);  // passed is false
passed = [12, 54, 18, 130, 44].every(isBigEnough);    // passed is true
```

**Required Parameters:**
+ `validator`: `function` (ex. `isBigEnough`)

**Returns:**
+ `boolean`

___

### _Filter_

`array.filter(func)`

The `filter()` method creates a **new array** with all elements that pass the test implemented by the provided function.

**Example:**

```javascript
//function isBigEnough returns the elements greater than 10.
function isBigEnough(element) {
  return element >= 10;
}
var filtered = [12, 5, 8, 130, 44].filter(isBigEnough); 
// filtered is [12, 130, 44]
```

**Required Parameters:**
+ `func`: `function` (ex. `isBigEnough`)

**Returns:**
+ `array`

___
