#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry"""

class BaseGeometry:
    """Represents base geometry"""

    def area(self):
        """Not yet implemented"""
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        """
        Checks for integer value

        Args:
            name: name of value
            value: value
        
        Raises:
            TypeError: if value isnt integer
            ValueError: if value is less than or equal to 0
        """

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
