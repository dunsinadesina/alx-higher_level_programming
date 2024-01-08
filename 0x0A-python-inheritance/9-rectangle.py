#!/usr/bin/python3
"""Defines a class Rectangle inherited fro BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Represents a rectangle using basegeometry"""

    def __init__(self, width, height):
        """
        Initialize rectangle

        Args:
            width: width of rectangle
            height: height of rectangle
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return '[Rectangle] ' + str(self.__width) + '/' + str(self.__height)
