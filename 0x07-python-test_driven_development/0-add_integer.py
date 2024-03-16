#!/usr/bin/python3
"""Defines an add integer module"""
def add_integer(a, b=98):
    """Adds two numbers

    Args:
    a: first number
    b: second number, default = 98

    Raises:
    TypeError: if neither a nor b are int or float type

    Returns:
    sum
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    elif type(b) not in (int, float):
        raise TypeError("b must be an integer")
    else:
        return int(a) + int(b)

    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/0-add_integer.txt")
