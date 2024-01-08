#!/usr/bin/python3
"""Defines a Rectangle subclass Square"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represnts a square"""

    def __init__(self, size):
        """
            Initialize a new square

            Args:
                size: size of square

        """
        self.integer_validator(size, size)
        super().__init__(size, size)
        self.__size = size
