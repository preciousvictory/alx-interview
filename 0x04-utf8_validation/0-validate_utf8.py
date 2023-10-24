#!/usr/bin/python3
"""-validate_utf8 file
"""


def validUTF8(data):
    """validUTF8"""

    valid = False

    for byte in data:
        if byte >> 8 != 0:
            valid = False
        else:
            valid = True
    return valid
