## _Ice Life_

#### _Legend says:_
> Life is the Game.

#### _Goals:_
+ _Achieve population 120_
+ _Bonus: Achieve population 150_
+ _Bonus: Achieve population 180_

#### _Topics:_
+ **Basic Syntax**
+ **Reading the Docs**

#### _Solutions:_
+ **[JavaScript](iceLife.js)**
+ **[Python](ice_life.py)**

#### _Rewards:_
+ 512-1024 xp
+ 256-512 gems

#### _Victory words:_
+ _THERE ARE NO RESTRICTIONS FOR LIFE. IT'S ENOUGH FOR A SMALL TOWN. YOU SHOULD BE A MAYOR._

___

### _HINTS_

[The Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) is a cellular automaton devised by the British mathematician John Horton Conway.

This is the limited version of that game: the field is limited and you can init only small part of the field. Create the init state with the 2d array of 1s and 0s and watch for the result.

Try to achieve the maximum population.

___

The universe of the Game of Life is an infinite (**it's not our case**) two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, alive or dead, or _populated_ or _unpopulated_ (the difference may seem minor, except when viewing it as an early model of human/urban behaviour simulation or how one views a blank space on a grid). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent. At each step in time, the following transitions occur:
1. Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

___
