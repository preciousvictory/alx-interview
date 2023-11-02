#!/usr/bin/python3
"""-validate_utf8 file
"""


def validUTF8(data):
    """validUTF8"""

    valid = False
    no_bytes = len(data)
    L = 0

    if len(data) == 0:
        return True

    for i in range(no_bytes):
        if type(data[i]) != int or data[i] > 0x10FFFF or data[i] < 0:
            return False
        # Byte 1 where first code point is U+0000 and last is U+007F
        elif data[i] <= 0x7F:
            if data[i] >> 8 == 0:
                valid = True
            else:
                return False
        # Byte 4 - first code point is U+10000 and last is U+10FFFF
        elif data[i] & 0b11111000 == 0b11110000:
            if data[i] >> 3 != 0b11110:
                return False
            else:
                L = 3
                try:
                    for a in range(1, L + 1):
                        if data[i + a] & 0b11000000 == 0b10000000:
                            valid = True
                        else:
                            return False
                    i += L
                except IndexError:
                    return False
        # Byte 3 where first code point is U+0800 and last is U+FFFF
        elif data[i] & 0b11110000 == 0b11100000:
            if data[i] >> 4 != 0b1110:
                return False
            else:
                L = 2
<<<<<<< HEAD
                for i in range(L):
                    if data[i + L] & 0b11000000 == 0b10000000:
                        return False
                    else:
                        valid = True
                i += L
        # Byte 4 - first code point is U+10000 and last is U+10FFFF
        elif data[i] & 0b11111000 == 0b11110000:
            if data[i] >> 3 != 0b11110:
                return False
            else:
                L = 3
                for i in range(L):
                    if data[i + L] & 0b11000000 == 0b10000000:
                        print(data[i + L])
                        return False
                    else:
                        valid = True
                i += L
        else:
            return False
    return True
=======
                try:
                    for a in range(1, L + 1):
                        if data[i + L] & 0b11000000 == 0b10000000:
                            valid = True
                        else:
                            return False
                    i += L
                except IndexError:
                    return False
        # Byte 2 where first code point is U+0080 and last is U+07FF
        elif data[i] & 0b11100000 == 0b11000000:
            try:
                L = 1
                if data[i + L] & 0b11000000 == 0b10000000:
                    valid = True
                else:
                    return False
                i += 1
            except IndexError:
                return False
    return valid
>>>>>>> bb7d085ab41def283d1a7d36e4e96bd731b4e6b8
