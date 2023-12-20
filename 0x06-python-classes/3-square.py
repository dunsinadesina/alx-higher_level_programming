#!/usr/bin/python3
"""defines a class Square"""
class Square:
    """Represents a square"""
    def __init__(self, size=0):
        """intitialze a new Square
        Args:
            size(int): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Return area of the new square"""
        return (self.__size * self.__size)
