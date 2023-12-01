#!/usr/bin/python3
'''Calculate the perimeter of an island'''


def island_perimeter(grid):
    '''calculate the perimeter of the island'''
    start = False
    count = 0

    if grid == [] or grid == [[]] or grid is None:
        return 0

    length = len(grid[0])
    # vertical scan
    for i in range(length):
        idx = 0
        for each in grid:
            idx += 1
            if (each[i] == 1) and (start is False):
                count += 1
                start = True
            if ((each[i] == 0) or (idx == len(grid))) and (start is True):
                count += 1
                start = False

    # horizontal scan
    start = False
    for each in grid:
        idx = 0
        for j in each:
            idx += 1
            if (j == 1) and (start is False):
                count += 1
                start = True
            if ((j == 0) or (idx == length)) and (start is True):
                count += 1
                start = False

    return count
