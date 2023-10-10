#!/usr/bin/env python
'''0-minoperations'''


def minOperations(n):
    if not isinstance(n, int):
        return 0

    text_file = 1
    count = 0
    copy = 0
    while text_file < n:
        if text_file == 0:
            copy = text_file
            text_file += copy
            count += 2
        elif n - text_file > 0 and (n - text_file) % text_file == 0:
            copy = text_file
            text_file += copy
            count += 2
        elif text_file > 0:
            text_file += copy
            count += 1

    return count
