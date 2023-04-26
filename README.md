# Conways Game Of Life

![video](/Users/lewey/Documents/Coding/Coding Projects/GitHub/ConwaysGameOfLife/media/conways-game-of-life-example-play.mp4)
### Description:
>The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.[1] It is a zero-player game,[2][3] meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

### Rules:
> The universe of the Game of Life is an infinite, two-dimensional orthogonal grid of square cells, each of which is in one of two possible states, live or dead (or populated and unpopulated, respectively). Every cell interacts with its eight neighbours, which are the cells that are horizontally, vertically, or diagonally adjacent.

At each step in time, the following transitions occur:

- Any live cell with fewer than two live neighbours dies, as if by underpopulation.
- Any live cell with two or three live neighbours lives on to the next generation.
- Any live cell with more than three live neighbours dies, as if by overpopulation.
- Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

> These rules, which compare the behaviour of the automaton to real life, can be condensed into the following:

- Any live cell with two or three live neighbours survives.
- Any dead cell with three live neighbours becomes a live cell.
- All other live cells die in the next generation. Similarly, all other dead cells stay dead.

---

## Start up:

1. open terminal at file directory
2. activate virtual environment
    - `source .venv/bin/activate`
3. install requirements
    - `pip install -r requirements.txt`
4. run the game
    - `python main.py`
5. draw pattern on screen using your mouse
6. press space bar to start
7. additionally you may continue to update the game with your mouse once started
8. to end the game press space bar again
