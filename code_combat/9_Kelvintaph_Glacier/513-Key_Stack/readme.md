## _Key Stack_

#### _Legend says:_
> Three keys and three doors. Don't mix up.

#### _Goals:_
+ _Collect the treasures_
+ _The prasant must survive_

#### _Topics:_
+ **Basic Syntax**
+ **Data Structures - Stacks**

#### _Solutions:_
+ **[Python](treasured_in_ice.py)**

#### _Rewards:_
+ 3070 xp
+ 930 gems

#### _Victory words:_
+ _STOMP, CRASH, BANG!_

___

### _HINTS_

You must get in the dungeon and collect all chest of gems.

The peasant can pick up and drop items. Use it to opens doors. However, if he drops a key far from a door then the key breaks. Also, doors close after a short time. So the peasant should pick up all keys, then go to the doors.

When the peasant picks up an item it appears on the top. He can drop only the top item. So the order of collecting of keys is important.

A stack is a collection where you add elements to the "top" of the ordering and remove from the "top" as well. The only accessible element is the one added latest. A stack is sometimes called a Last In, First Out ("LIFO") structure.

The peasant's inventory is a stack. He can `'pickUpItem'` (PUSH) to the top of the inventory and `'dropItem'` (POP) the last item in the stack. It's like a box where you can put some elements one up to another. However, you can see and take only the last one. If you want to take the element from the bottom you need get them all before. We can implement a stack with an array.

```python
stack = []
stack.append(3)  # PUSH 3 -> [3]
stack.append(5)  # PUSH 5 -> [3, 5]
top = stack.pop()  # POP -> [3]
```

___
