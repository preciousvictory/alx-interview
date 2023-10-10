#!/usr/bin/env python3
'''0-minoperations
'''


def minOperations(n):
    '''minOperations
    fewest number of operations needed to result in exactly n H characters
    '''
    if not isinstance(n, int):
        return 0

    text_file = 1
    count = 0
    copy = 0
    while text_file < n:
        '''start copy (initialize)'''
        if copy == 0:
            copy = text_file
            text_file += copy
            count += 2
        '''
        if the number of characters in the file remaining to reach exactly n
        characters and if number of characters remaining divisible by the numbe
        of characters already in the file'''
        elif n - text_file > 0 and (n - text_file) % text_file == 0:
            copy = text_file
            text_file += copy
            count += 2
        elif text_file > 0:
            text_file += copy
            count += 1

    return count
