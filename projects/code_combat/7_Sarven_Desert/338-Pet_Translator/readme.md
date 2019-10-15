## _Pet Translator_

#### _Legend says:_
> The Sdrawkcab Mercenary Band provides substantial firepower... If anyone could speak their language.

#### _Goals:_
+ _Defeat the ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **Functions**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](petTranslator.js)**
+ **[Python](pet_translator.py)**

#### _Rewards:_
+ 190 xp
+ 160 gems

#### _Victory words:_
+ _GNIZAMA SAW TAHT!_

___

### _HINTS_

The Sdrawkcab Mercenaries are providing intel on an incoming ogre attack!

Use your pet to decipher what they say using the `event.message` property.

Our scouts have seen several groups of brawlers near the camp. Luckily, we have several hired cannons. Unluckily, the artillerymen don't understand our language.

While your hero is fighting, your pet should translate commands for the mercenaries.

The event handler parameter `event` contains the property `message`.

When a `"hear"` event is triggered, the handler function can access the message the pet heard using `event.message`.

```javascript
function repeat(event) {
    // The pet repeats the heard message.
    pet.say(event.message);
}
```

___
