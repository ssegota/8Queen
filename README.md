#8 Queens Evolutionary

This is a Python program that solves a 8 Queen puzzle.

From [Wikipedia](https://en.wikipedia.org/wiki/Eight_queens_puzzle):

> The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other; thus, a solution requires that no two queens share the same row, column, or diagonal.

##Short solution description

In the beginning code generates a 1000 random movesets(Positions of Queens). 

Then in each new generation movesets from the past are recombined at random, with a chance of random mutation. The code is using an exponential probability function to make it more likely to pick a value with better fitness from the sorted array.

When the solution is found, i.e. fitness function equals 8, the program stops and prints the solution.

##Results

Examples of solutions were generated using the software in this repository.

Positions of Queens are denoted by (X,Y) where X would present the horizontal or "letter" coordinate on the baord and Y the vertical or "number" coordinate on the board looking from the top. They are both in range of `[0,7]`. So a coordinate `[1,4]` in the below solution would be equal to chess board position of **E7**.

###Solution Example 1
Positions of Queens: [[2, 5], [7, 4], [1, 1], [6, 7], [3, 2], [0, 6], [4, 0], [5, 3]]
Board:
......Q.

.Q......

.....Q..

..Q.....

Q.......

...Q....

.......Q

....Q...

Solution vizualized using [lichess](https://lichess.org)

![board1][/images/logo.png/sol1.png]

With the graph of the fitness function through generations here:

![graph1][/images/logo.png/Figure_1.png]

###Solution Example 2

Positions of Queens: [[7, 3], [5, 7], [2, 0], [0, 5], [3, 6], [4, 4], [6, 1], [1, 2]]
Board:
.....Q..

..Q.....

Q.......

......Q.

....Q...

.......Q

.Q......

...Q....

Solution vizualized using [lichess](https://lichess.org)

![board2][/images/logo.png/sol2.png]

With the graph of the fitness function through generations here:

![graph2][/images/logo.png/Figure_2.png]

###Solution Example 3

Positions of Queens: [[7, 5]), [1, 0], [4, 1], [6, 2], [2, 7], [3, 3], [0, 4], [5, 6]]
Board:
....Q...

Q.......

.......Q

...Q....

.Q......

......Q.

..Q.....

.....Q..

Solution vizualized using [lichess](https://lichess.org)

![board2][/images/logo.png/sol3.png]

With the graph of the fitness function through generations here:

![graph2][/images/logo.png/Figure_3.png]

##Prerequisites

* Python 3+
* NumPy 1.15.1
* MatPlotLib 2.2.3

