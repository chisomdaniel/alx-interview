#!/usr/bin/python3
'''Calculate the perimeter of an island'''


def island_perimeter(grid):
    '''calculate the perimeter of the island'''
    start = False
    count = 0

    if grid == [] or grid == [[]]:
        return 0

    length = len(grid[0])
    # vertical scan
    for i in range(length):
        for each in grid:
            if (each[i] == 1) and (start == False):
                count += 1
                start = True
            if (each[i] == 0) and (start == True):
                count += 1
                start = False
    
    # horizontal scan
    start = False
    for each in grid:
        for j in each:
            if (j == 1) and (start == False):
                count += 1
                start = True
            if (j == 0) and (start == True):
                count += 1
                start = False

    return count
