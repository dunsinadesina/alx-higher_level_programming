#!/usr/bin/python3
import sys
def safe_print_integer_err(value):
    """a function that prints an integer.
    Args:
        value (int): integer
    Returns:
        True or False
    """
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
