#!/usr/bin/python3
"""define class for singly linked lists"""
class Node:
    """represents a node for a simgly linked list"""
    def __init__(self, data, next_node=None):
        """initializes new node
        Args:
            data(int): the date of the new node
            next_node(node): the next node of the new node
        """
        self.data = data
        self.next_node = next_node
    @property
    def data(self):
        """get or set the data of the node"""
        return(self.__data)
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value
    @property
    def next_node(self):
        """get or set next node of node"""
        return(self.__next_node)
    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value
class SinglyLinkedList:
    """defines a singly linked list"""
    def __init__(self):
        """initializing the singlist list"""
        self.__head = None
