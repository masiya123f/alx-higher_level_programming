#!/usr/bin/python3

import sys

args = sys.argv[1:]
num_args = len(args)

if num_args == 0:
    print("0 argument.")
    print(".")
else:
    print(f"{num_args} {'argument' if num_args == 1 else 'arguments'}:")
    for i, arg in enumerate(args, 1):
        print(f"{i}: {arg}")
