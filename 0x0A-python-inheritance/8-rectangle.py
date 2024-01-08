#!/usr/bin/python3
"""Defines a rectangle fro class basegeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle using basegeometry"""

    def __init__(self, width, height):
        """
            Initialize rectangle

            Args:
                width(int): width of rectangle
                height(int): height of rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
