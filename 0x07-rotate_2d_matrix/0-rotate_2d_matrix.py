#!/usr/bin/python3
'''Rotate a 2D matrix'''


def rotate_2d_matrix(matrix):
    '''rotate a 2d matrix'''

    if matrix == []:
        return

    length = len(matrix[0])
    mod_list = []

    len_list = list(range(len(matrix)))
    len_list.reverse()
    for i in range(length):
        list2 = []
        for j in len_list:
            list2.append(matrix[j][i])
        mod_list.append(list2)

    matrix_len = len(matrix)
    for i in range(matrix_len):
        matrix.pop()

    for i in mod_list:
        matrix.append(i)
