#!/usr/bin/python3
"""Defines an inherited class list"""

class MyList(list):
    """
    A class to customize the list class
    """

    def print_sorted(self):
        """
        Prints list in ascending order
        Sorts the list then print the output"""

        if issubclass(MyList, list):
            print(sorted(self))
