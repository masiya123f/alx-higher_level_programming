#!/usr/bin/python3

import sys

def infinite_add():
    if len(sys.argv) == 1:
        print(0)
    else:
        sum = 0
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print(sum)

if __name__ == "__main__":
    infinite_add()

