#!/usr/bin/python3
'''0-minoperations file
'''


def minOperations(n):
    '''minOperations fewest number of operations needed to result
    in exactly n H characters
    '''
    if not isinstance(n, int):
        return 0
    text_file = 1
    count = 0
    copy = 0
    while text_file < n:
        # start copy (initialize)
        if copy == 0:
            copy = text_file
            text_file += copy
            count += 2
        elif n - text_file > 0 and (n - text_file) % text_file == 0:
            # copy all and paste
            copy = text_file
            text_file += copy
            count += 2
        elif text_file > 0:
            # paste
            text_file += copy
            count += 1

    return count
