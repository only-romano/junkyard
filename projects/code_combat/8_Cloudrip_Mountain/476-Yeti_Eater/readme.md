## _Yeti Eater_

#### _Legend says:_
> Defeat Yeti. Devour Yeti. Next Yeti!

#### _Goals:_
+ _Defeat the yetis_

#### _Topics:_
+ **Variables**
+ **While Loops with Conditionals**
+ **For Loops**
+ **Array Indexes**
+ **Array Length**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](yetiEater.js)**
+ **[Python](yeti_eater.py)**

#### _Rewards:_
+ 263 xp
+ 121 gems

#### _Victory words:_
+ _NOM, NOM, NOM_

___

### _HINTS_

Yetis surround us, so it will be a good hunt. Luckily, the wizard had time to cast the sleep spell.

Your hero can devour yetis' vital powers when they are defeated. So you have to defeat them in the order from the weakest to the strongest. Luckily (again), the wizard can sort enemies from the strongest to the weakest.

Reverse that list and act!

___

We know the ordered list of the yetis, but we need it in the reversed order. To get the reversed list of the given you just need to read it from the end to the start.

`for`-loop can be useful for it. We just need to change start, end and step values:

```javascript
var array = [1, 2, 3];
// Don't forget about use ">" instead "<"
for (var i = array.length - 1; i > -1; i -= 1) {
    hero.say(array[i]);
}
```

We use the end value `-1`, because we shouldn't skip the 0-th index. Also, be careful with the start value: it should be less than the array's length by one.

It can be written with `while` loop:

```javascript
var index = array.length - 1;
while (index > -1) {  // or "index >= 0"
    hero.say(array[i]);
    i -= 1;  // or "i--"
}
```

___
