#!/usr/bin/python3
def safe_print_integer(value):
    """print an integer
    Args:
        value (int): the integer to print
    Return:
        True or False
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
