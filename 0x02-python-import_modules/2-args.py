#!/usr/bin/python3
import sys
if __name__ == "__main__":
    """print number and arguments"""
    counter = len(sys.argv) - 1
    if counter  == 0:
        print("0 argument{}.".format('s' if counter != 1 else ''))
    else:
        print("{} argument{}:".format(counter, 's' if counter != 1 else ''))
    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
