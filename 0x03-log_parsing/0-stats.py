#!/usr/bin/python3

import sys

total_file_size = 0
status_code_counts = {200: 0, 301: 0, 400: 0,
                      401: 0, 403: 0, 404: 0, 405: 0, 500: 0}

try:
    for idx, line in enumerate(sys.stdin, start=1):
        parts = line.split()
        if len(parts) == 7 and parts[6].isdigit():
            file_size = int(parts[6])
            status_code = int(parts[5])
            total_file_size += file_size
            status_code_counts[status_code] = status_code_counts.get(
                status_code, 0) + 1

            if idx % 10 == 0:
                print("File size:", total_file_size)
                for code in sorted(status_code_counts):
                    if status_code_counts[code] > 0:
                        print(f"{code}: {status_code_counts[code]}")
                print()

except KeyboardInterrupt:
    pass

finally:
    print("File size:", total_file_size)
    for code in sorted(status_code_counts):
        if status_code_counts[code] > 0:
            print(f"{code}: {status_code_counts[code]}")
