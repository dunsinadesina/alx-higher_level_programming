#!/usr/bin/python3
"""Defines a checking function"""

def is_same_class(obj, a_class):
    """
    checks if object is exactly the same an instance of the specified class

    Args: 
        obj: object to compare
        a_class: the class to compare with the object

        Returns:
        `True` if the object is exactly an instance of the
        specified class; otherwise `False`
    """

    if type(obj) == a_class:
        return True
    else:
        return False
