#!/usr/bin/python3
"""Define Rectangle subclass square"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle

class Square(Rectangle):
    """Represnts a Square"""

    def __init__(self, size):
        """
        Initialize new square

        Args:
            size: size of square
        """

        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
