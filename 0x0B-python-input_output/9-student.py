#!/usr/bin/python3
"""Defines a Class Student"""

class Student:
    """Represnets a student"""

    def __init__(self, first_name, last_name, age):
        """
        Initialize a new student

        Args:
            first_name(str): first name of student
            last_name: last name of student
            age: age of studnet
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

        def to_json(self):
            """Get dict representation of Student"""

            return (self.__dict__)
