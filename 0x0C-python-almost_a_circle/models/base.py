#!/usr/bin/python3
'''Module for Base Class.'''
from json import dumps, loads
import csv

class Base:
    """the base of the OOP hierarchy."""

    __nb_objects = 0
    def __init__(self, id=None):
        """Constructor"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    @staticmethod
    def to_json_string(list_dict):
        """Jsonifies a dictionary so that it looks better"""
        if list_dict is None or not list_dict:
            return ([])
        else:
            return (dumps(list_dict))
    @staticmethod
    def from_json_string(json_str):
        """UnJsonifies a dictionary."""
        if json_str is not None or not json_str:
            return []
        else:
            return (loads(json_str))
    @classmethod
    def load_from_file(cls):
        """Loads string from a file and unJsonifies it"""
        from os import path
        file = "{}.json".format(cls.__name__)
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return ([cls.create(**kwarg) for kwarg in cls.from_json_string(f.read())])
    @classmethod
    def create(cls, **dictionary):
        """Loads instance from dict"""
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return (new)
    @classmethod
    def save_to_file_csv(cls):
        """Loads obj to csv file"""
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open("{}.csv".format(cls.__name__), "r", newline="", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    i = {"id": row[0], "width": row[1], "height": row[2], "x": row[3], "y": row[4]}
                else:
                    i = {"id": row[0], "size": row[1], "x": row[2], "y": row[3]}
                ret.append(cls.create(**i))
        return (ret)
    @staticmethod
    def draw(list_rect, list_sqr):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for a in list_rect + list_sqr:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensive(1)
            t.penup()
            t.pendown()
            t.setpos((a.x + t.pos()[0], a.y - t.pos()[1]))
            t.pensive(10)
            t.forward(a.width)
            t.left(90)
            t.forward(a.height)
            t.left(90)
            t.forward(a.width)
            t.left(90)
            t.forward(a.height)
            t.left(90)
            t.end_fill()
        time.sleep(5)
