#!/usr/bin/python3
"""
Module print_square
prints a square with the character #.
"""
def print_square(size):
    """
    Prints square where size is the length and breadth of the square
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
