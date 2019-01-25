# twenty-four
Solver for the game Twenty-Four (24)

usage: TwentyFour.py [-h] [-t TARGET] [-s] a b c d

positional arguments:
  a                     First number
  b                     Second number
  c                     Third number
  d                     Fourth number

optional arguments:
  -h, --help            show this help message and exit
  -t TARGET, --target TARGET
                        The target number. For the game of TwentyFour it is 24
  -s, --solution        Print the solutions

# Example
> python TwentyFour.py 4 7 9 2
[4, 7, 9, 2] is solveable

> python TwentyFour.py 4 7 9 2 -s
(2 * (9 - (4 - 7)))
((2 * 4) + (7 + 9))
(2 * ((7 + 9) - 4))
(2 * ((7 - 4) + 9))
(2 * ((9 - 4) + 7))
(9 + (7 + (2 * 4)))
((2 * 4) + (7 + 9))
(7 + ((2 * 4) + 9))
(2 * (7 - (4 - 9)))

> python TwentyFour.py 3 7 9 2 -t 29
[3, 7, 9, 5] is solveable

> python TwentyFour.py 3 7 9 2 -t 29 -s
((2 * (7 + 9)) - 3)
(9 + (2 * (3 + 7)))
