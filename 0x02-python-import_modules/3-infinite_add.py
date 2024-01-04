#!/usr/bin/python3
from sys import argv

def infinite_add(args):
    result = 0
    for arg in args:
        result += int(arg)
    return result

if __name__ == "__main__":
    args = argv[1:]
    result = infinite_add(args)
    print(result)
