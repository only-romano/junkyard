## _Ritual of Rectangling_

#### _Legend says:_
> Only geometry can save us and give us the Protector.

#### _Goals:_
+ _Defeat the giant ogre_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Functions**
+ **Return Statements**

#### _Solutions:_
+ **[JavaScript](rithualOfRect.js)**
+ **[Python](rithual_of_rect.py)**

#### _Rewards:_
+ 387 xp
+ 178 gems

#### _Victory words:_
+ _APPROXIMATELY AMAZING!_

___

### _HINTS_

That ogre is huge! But we know the geometric ritual and can summon the Ancient Warrior to fight for us.

We need four paladins which should form a rectangle with a specific perimeter and a specific area. When the retangle is formed, say: `"VENITE"`!

The paladins will continuously move, so watch them and say the magic word when the rectangle is correct.

Computers have trouble handling numbers with any certainty, so, use an 'almost equal' comparison to verify the rectangle is approximately the correct size. The magic spell has a 3% margin of error, so use that to your advantage!

___


These four paladins can summon a powerful unit to defeat this giant ogre! They will move around and you must tell them when they are forming the required rectangle.

Check their area and perimeter constantly until they meet the requirements.

Area of a rectangle is found by multiplying the length of two adjacent sides:

```javascript
function area(sideA, sideB) {
    // Return the3 product of the multiplication of sideA and sideB
}
```

Perimeter is found by adding the length of every side:

```javascript
function perimeter(sideA, sideB) {
    // A rectangel has four sides!
    // Return the sum of side A * 2 and SideB * 2!
}
```

Since the paladins are moving around, it is possible they will skip over the exact moment their perimeter and area are your desired values. This is why we use a 'approximately equal' function:

```javascript
function approxEqual(numberA, numberB) {
    var min = numberA * 0.97;
    var max = numberA * 1.03;
    // Return true if number B is above min and below max

    // Otherwise return false
    return false;
}
```

___
