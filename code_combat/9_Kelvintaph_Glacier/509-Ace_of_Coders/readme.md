## _Ace of Coders_

#### _Legend says:_
> If you don't have chips to play, then use skeletons.

#### _Goals:_
+ _Defeat the enemy hero_
+ _Your hero must survive_

#### _Topics:_
+ **Arrays**
+ **For Loops**
+ **Functions**
+ **Vectors**
+ **Math Library Operations**
+ **Algorithms**

#### _Solutions:_
+ **[Python](ace_of_coders.py)**

#### _Rewards:_
+ 3070 xp
+ 930 gems

#### _Victory words:_
+ _IT LOOKS LIKE THE LAST THING YOU NEEDED WAS A SKELETON KEY!_

___

### _HINTS_

In this level you will play as Okar Stompfoot in red versus Okar Stompfoot in blue!

You start with 200 gold, and each Control Point you control gives you 3 gold per second.

Your main objectives are to:
+ Capture strategic control points,
+ Build an army, and
+ **Defeat the enemy hero**.

The simulation timestep is 0.25 seconds, and you have up to 3 minutes to win. Any ties will be broken by ice yaks, army strength, and gold collected.

#### Units

The units available in the level are as follows:

<table>
<thead>
<tr>
<th>Unit Type</th>
<th style="text-align:right">DPS</th>
<th style="text-align:right">Range</th>
<th style="text-align:right">HP</th>
<th style="text-align:right">Speed</th>
<th style="text-align:right">Cost</th>
</tr>
</thead>
<tbody>
<tr>
<td><code>"soldier"</code></td>
<td style="text-align:right">12.0</td>
<td style="text-align:right">3</td>
<td style="text-align:right">200</td>
<td style="text-align:right">6</td>
<td style="text-align:right">20</td>
</tr>
<tr>
<td><code>"archer"</code></td>
<td style="text-align:right">26.0</td>
<td style="text-align:right">25</td>
<td style="text-align:right">30</td>
<td style="text-align:right">9</td>
<td style="text-align:right">25</td>
</tr>
<tr>
<td><code>"artillery"</code></td>
<td style="text-align:right">250/3.6</td>
<td style="text-align:right">65</td>
<td style="text-align:right">100</td>
<td style="text-align:right">4</td>
<td style="text-align:right">75</td>
</tr>
<tr>
<td><code>"arrow-tower"</code></td>
<td style="text-align:right">70.0</td>
<td style="text-align:right">30</td>
<td style="text-align:right">600</td>
<td style="text-align:right">0</td>
<td style="text-align:right">100</td>
</tr>
<tr>
<td><code>"goliath"</code></td>
<td style="text-align:right">120.0</td>
<td style="text-align:right">5</td>
<td style="text-align:right">6000</td>
<td style="text-align:right">4</td>
<td style="text-align:right">0</td>
</tr>
</tbody>
</table>

Your hero can summon every unit type and can command all of his units (`"arrow-tower"`s will auto-attack without any commands).

#### Control Points

Capturing Control Points is essential towards defeating the enemy hero. The unit closest to a Control Point (within 10 meters) captures the point for its team to start earning its 3 gold per second income.

You can get all the Control Points in an array with `getControlPoints()`, and as a object with `getControlPointsMap()`. Hover over the method documentation popups for more information. Depending on whether you are playing as red or blue, the near and far point names will be reversed so that your code can run on either side.

#### Strategy

There is no single winning strategy. The best strategies will focus on:
+ Building an army with a mix of unit types
+ Capturing Control Points strategically
+ A system for moving troops to where they are needed most
+ Countering enemy attacks on captured Control Points
+ Utilizing your hero's special abilities
+ Choosing when to defend and when to attack with `time` or reacting to your opponent
+ Deciding whether to target enemy troops or the enemy hero

___
