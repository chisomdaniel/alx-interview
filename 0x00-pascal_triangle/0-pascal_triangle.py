#!/usr/bin/python3
'''Pascal Trianle'''


def next_value(numbers: list):
    '''Returns the list of values of the next layer
    of the triangle provided the previous list of values'''

    if len(numbers) == 1:
        return ([1])

    num_list = [numbers[0] + numbers[1]]

    num = next_value(numbers[1:])

    return num_list + num

def pascal_triangle(n):
    '''returns a list of lists of integers representing
    the Pascal’s triangle of `n`'''

    if (n <= 0):
        return []

    pascal = []

    triangle = [1]
    for i in range(n):
        pascal.append(triangle)
        triangle = [1] + next_value(triangle)

    return pascal


