#!/usr/bin/python3
"""-validate_utf8 file
"""


def validUTF8(data):
    """validUTF8"""

    valid = False
    no_bytes = len(data)
    L = 0

    for i in range(no_bytes):
        if i >> 8 != 0 or type(data[i]) != int or data[i] > 0x10FFFF or data[i] < 0:
            return False
        # Byte 1 where first code point is U+0000 and last is U+007F
        elif data[i] <= 0x007F:
            if data[i] >> 8 == 0:
                valid = True
        # Byte 2 where first code point is U+0080 and last is U+07FF
        elif data[i] >= 0x0080 and data[i] <= 0x07FF:
            if data[i] >> 5 != 110:
                return False
            else:
                L = 1
                if data[i + L] >> 6 != 10:
                    return False
                else:
                    valid = True
        # Byte 2 where first code point is U+0800 and last is U+FFFF
        elif data[i] >= 0x0800 and data[i] <= 0xFFFF:
            if data[i] >> 4 != 1110:
                return False
            else:
                L = 2
                for i in L:
                    if data[i + L] >> 6 != 10:
                        return False
                    else:
                        valid = True
                i += L
        # Byte 4 - first code point is U+10000 and last is U+10FFFF
        elif data[i] >= 0x10000 and data[i] <= 0x10FFFF:
            if data[i] >> 3 != 11110:
                return False
            else:
                L = 3
                for i in L:
                    if data[i + L] >> 6 != 10:
                        return False
                    else:
                        valid = True
                i += L
    return valid
