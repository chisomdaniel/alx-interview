#!/usr/bin/python3
'''You have n number of locked boxes in front of you. Each box
is numbered sequentially from 0 to n - 1 and each box may contain
keys to the other boxes.

Write a method that determines if all the boxes can be opened.'''


def add_keys(keys, box):
    '''A function to add all the keys in a box to the other keys'''

    for i in box:
        if i not in keys:
            keys.append(i)

    return keys


def canUnlockAll(boxes):
    '''Check if all the box can be opened.

    Return True, if they can be opened, else False
    '''

    box_length = len(boxes)
    keys = [0]

    for i in keys:
        if (i < box_length) and (i >= 0):
            keys = add_keys(keys, boxes[i])

        if len(keys) == box_length:
            # print(keys)
            return True

    return False



boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))