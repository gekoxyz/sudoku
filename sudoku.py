import numpy as np
import random
import copy

"""
the method receives a position (with the coordinates x and y), a grid and a number
and checks if the number could be placed in the specified position while respecting
the sudoku rules
"""


def possible(y, x, n, grid):
    for i in range(0, 9):
        if grid[y][i] == n:  # check if number is in column
            return False
        if grid[i][x] == n:  # check if number is in row
            return False

    starting_x = (x // 3) * 3
    starting_y = (y // 3) * 3
    for y in range(0, 3):
        for x in range(0, 3):
            if grid[starting_y + y][starting_x + x] == n:
                return False

    return True


def solve(grid):
    for y in range(0, 9):
        for x in range(0, 9):
            if grid[y][x] == 0:
                for n in range(1, 10):  # the loop goes from 1 to 9
                    if possible(y, x, n, grid):
                        grid[y][x] = n
                        solve(grid)
                        # if the grid can't be solved after the choice it was
                        # a bad choice, so we set it back to 0
                        grid[y][x] = 0
                return
    # the sudoku is solved
    print(np.matrix(grid))

if __name__ == "__main__":
    # generate()

    grid = [[5,3,0,0,7,0,0,0,0],
           [6,0,0,1,9,5,0,0,0],
           [0,9,8,0,0,0,0,6,0],
           [8,0,0,0,6,0,0,0,3],
           [4,0,0,8,0,3,0,0,1],
           [7,0,0,0,2,0,0,0,6],
           [0,6,0,0,0,0,2,8,0],
           [0,0,0,4,1,9,0,0,5],
           [0,0,0,0,8,0,0,7,9]]

    print(np.matrix(grid))

    solve()