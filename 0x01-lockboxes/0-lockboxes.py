#!/usr/bin/python3
"""
0-lockboxes
"""


def canUnlockAll(boxes):
    """
    lockboxes
    You need to know if you can access all of the boxes,
    that is get all the key from each box

    Box zero starts unlocked, so you have access to the keys in box zero.
    If box zero has keys for box 1, 4, and 6, then you can open all those
    boxes and get the keys in those boxes too.

    You are collecting a group of keys from the boxes you have keys for.
    After you can no longer collect more keys, check if  all the boxes opened?

    True if all boxes are opened and False if not
    """
     if (type(boxes)) is not list:
        return False
    elif (len(boxes)) == 0:
        return False

    unlocked = [0]

    for index, box in enumerate(boxes):
        if not box:
            continue
        if index in unlocked:
            for i in box:
                if i not in unlocked:
                    unlocked.append(i)

    check_unlocked = False
    for i in range(len(boxes)):
        if i not in unlocked:
            check_unlocked = False
        else:
            check_unlocked = True

    return check_unlocked
