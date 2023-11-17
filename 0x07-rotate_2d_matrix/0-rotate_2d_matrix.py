#!/usr/bin/python3
"""0-rotate_2d_matrix
"""


def rotate_2d_matrix(matrix):
    """rotate_2d_matrix function
    """
    n = len(matrix) - 1
    temp = [[i for i in j] for j in matrix]

    r = 0
    for row in temp:
        c = 0
        for col in row:
            new_r = c % (n + 1)
            new_c = r + n
            if new_c > n:
                new_c %= n
            matrix[new_r][new_c] = col
            c += 1
        r += 1
