#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """pascal_triangle"""
    if n <= 0:
        return []

    pascal_tr = []
    if n == 1:
        pascal_tr.append([1])
    elif n == 2:
        pascal_tr.append([1])
        pascal_tr.append([1, 1])
    else:
        pascal_tr.append([1])
        pascal_tr.append([1, 1])
        for v in range(3, n + 1):
            tri_list = []
            cursor = 0

            tri_list.insert(1, 1)
            tri_list.insert(n - 1, 1)
            for p in range(v - 2):
                prev_list = pascal_tr[-1]
                value = prev_list[cursor] + prev_list[cursor + 1]
                tri_list.insert(p + 1, value)
                cursor += 1
                prev_list = tri_list
            pascal_tr.append(tri_list)
    return pascal_tr
