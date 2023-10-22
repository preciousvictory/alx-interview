#!/usr/bin/python3
"""0-stats
a script that reads stdin line by line and computes metrics
"""
import sys
import ipaddress


def print_stats(filesize, code_count):
    print(f'File size: {filesize}')
    for code, value in code_count.items():
        if value > 0:
            print('{}: {}'.format(code, value))


if __name__ == '__main__':
    codes = ["200", "301", "400", "401", "403", "404", "405", "500"]
    code_count = {x: 0 for x in codes}
    count, filesize = 0, 0

    try:
        for line in sys.stdin:
            count += 1
            if 'q' == line.rstrip():
                break

            data = line.split(" ")
            if len(data) != 9:
                continue

            try:
                status_code = data[-2]
                if status_code in codes:
                    code_count[status_code] += 1
                filesize += int(data[-1])
            except BaseException:
                pass

            if count % 10 == 0:
                print_stats(filesize, code_count)
    except KeyboardInterrupt:
        print_stats(filesize, code_count)
        raise
    finally:
        print_stats(filesize, code_count)
