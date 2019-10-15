## _Triage_

#### _Legend says:_
> Wounded soldiers need healing, but we need to help the most wounded first.

#### _Goals:_
+ _Triage the patients_

#### _Topics:_
+ **Strings**
+ **Variables**
+ **Array Length**
+ **Iterating Over Arrays**
+ **Accessing Properties**
+ **Assigning Properties**

#### _Solutions:_
+ **[JavaScript](triage.js)**
+ **[Python](triage.py)**

#### _Rewards:_
+ 325 xp
+ 124 gems

#### _Victory words:_
+ _YOU HELPED EVERYONE THROUGH EFFICIENT USE OF RESOURCES!_

___

### _HINTS_

Sort the wounded soldiers into three arrays.

One array is for the `mage` who will de-curse the slowed soldiers.

One array is for the `doctor` who will heal the seriously injured soldiers (less than half health).

The third array is for the `helper` who will find a place for the mildly injured soldiers to rest.

Remember, you can add to an array using:

```javascript
doctorPatients.push(soldier);
```

The sample code shows you how to add the **slowed** soldiers to the `magePatients` array, to remind you how it's done.

So, first you should add the soldiers with `soldier.health` less than `soldier.maxHealth / 2` into the `doctorPatients` array.

Then, any soldiers that are neither **slowed** or at less than half health, should be added to the `helperPatients` array.

That's it! The sample code then adds the arrays of patients to the appropriate person, who will then be able to do their job.

___
