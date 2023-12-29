#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    returns the perimeter of the island described in grid
    grid is a list of list of integers:
    - 0 represents water
    - 1 represents land
    Each cell is square, with a side length of 1
    Cells are connected horizontally/vertically (not diagonally).
    grid is rectangular, with its width and height not exceeding 100
    The grid is completely surrounded by water
    There is only one island (or nothing).
    The island doesn’t have “lakes” (water inside that isn’t connected to
    the water surrounding the island).

    Args:
        grid (list of list of int): the grid representing the island

    Returns:
        int: the perimeter of the island
    """

    rows = len(grid)
    cols = len(grid[0])

    perimeter = 0
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:

                try:
                    # check top
                    if i == 0 or grid[i - 1][j] == 0:
                        perimeter += 1
                    # check left
                    if j == 0 or grid[i][j - 1] == 0:
                        perimeter += 1
                    # check right
                    if j == cols - 1 or  grid[i][j + 1] == 0:
                        perimeter += 1
                    # check bottom
                    if i == rows - 1 or grid[i + 1][j] == 0:
                        perimeter += 1
                except IndexError as e:
                    pass

    return perimeter
