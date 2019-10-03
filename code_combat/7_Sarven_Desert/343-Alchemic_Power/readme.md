## _Alchemic Power_

#### _Legend says:_
> A skilled alchemist can change flow of a battle.

#### _Goals:_
+ _Defeat the ogres_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **While Loops**
+ **If Statements**
+ **If/Else Statements**
+ **Accessing Properties**

#### _Solutions:_
+ **[JavaScript](alchemicPower.js)**
+ **[Python](alchemic_power.py)**

#### _Rewards:_
+ 190 xp
+ 160 gems

#### _Victory words:_
+ _UNLIMITED POWER!_

___

### _HINTS_

Alchemic potions are our secret advantage. While your hero is fighting, your pet should wait for the command  `"Fetch"` from the alchemist and deliver a potion to the hero when it is heard.

Use the event handler parameter `event` to get the message that was said. It's contained in the property `event.message`. When the message isn't "Fetch" your pet should return to the red mark. Use `pet.fetch(item)` to take and bring an item to the hero.

Events include data about what has occured to cause the Event Handler to fire.

For the `"hear"` event, the first parameter (usually named `event`) contains valuable information about who the `speaker` was and what `message` they said.

For example:

```javascript
function onHear(event) {
    var who = event.speaker;  // This will be Omarn
    var what = event.message;  // This will be "Drink this!"
    pet.say(who + " said " + what);
    pet.say("Squawk");  // Squawk
}

pet.on("hear", onHear);
// Then Omarn says: "Drink this!"
```

Use this to listen for the correct message, and have your pet fetch potions when the time is right!

___
