#!/usr/bin/python3
"""Defines a class checking function"""

def inherits_from(obj, a_class):
    """
    Checks if obj is the same class or inherit from a_class(sub-class)

    Args:
        obj (any): The object to compare
        a_class (any): The class to compare with the object

    Returns:
        True if the object is an instance or inherit from the
        specified class; otherwise False
    """
    if isinstance(obj, a_class) and  issubclass(a_class, obj.__class__) is False:
        return True
    else:
        return False
