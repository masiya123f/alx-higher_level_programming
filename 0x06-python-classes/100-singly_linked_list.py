#!/usr/bin/python3
"""Defines a class Node and a class SinglyLinkedList."""

class Node:
    """Represents a node in a singly linked list.
    Attributes:
        data (int): data stored in the node.
        next_node (Node, optional): the next node in the list. Defaults to None.
    """

    def __init__(self, data, next_node=None):
        """Initializes the Node.
        Args:
            data (int): data stored in the node.
            next_node (Node, optional): the next node in the list. Defaults to None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Getter for data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Setter for data."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Getter for next_node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Setter for next_node."""
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Represents a singly linked list.
    Attributes:
        __head (Node): the first node in the list.
    """

    def __init__(self):
        """Initializes the SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list (increasing order).
        Args:
            value (int): data of the new Node.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            tmp = self.__head
            while tmp.next_node is not None and tmp.next_node.data < value:
                tmp = tmp.next_node
            new_node.next_node = tmp.next_node
            tmp.next_node = new_node

    def __str__(self):
        """Returns a string representation of the SinglyLinkedList."""
        nodes = []
        tmp = self.__head
        while tmp is not None:
            nodes.append(str(tmp.data))
            tmp = tmp.next_node
        return "\n".join(nodes)
