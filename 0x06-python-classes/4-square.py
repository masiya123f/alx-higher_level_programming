#!/usr/bin/python3
""" defines a square """

class Square:
    """ square with private instance attribute size """

    def __init__(self, size=0):
        """
        Initializes a square
        Args:
            size: size of side of square
        """
        self.size = size

    @property
    def size(self):
        """
        Getter for size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter for size
        Args:
            value: size of a side of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Finds the area of the square
        Returns:
            The area of the square
        """
        return self.__size ** 2
