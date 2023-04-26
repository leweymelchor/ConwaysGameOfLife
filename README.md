# Conways Game Of Life

### Description:

>The Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves. It is Turing complete and can simulate a universal constructor or any other Turing machine.

### See it in action below:

https://user-images.githubusercontent.com/102191748/234531687-23640f7c-724c-4128-82ec-fa0975b3cc04.mp4

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

### Example drawing:

https://user-images.githubusercontent.com/102191748/234531748-068768dd-b8cb-4405-a59d-e6a3cfffee6a.mp4

## Created By:

|Name|Email|GitHub|
|----|-----|-------|
|Lewey Melchor|dlmelchor12@gmail.com|https://github.com/leweymelchor|
