#!/usr/bin/python3
"""Defines a class Square"""

class Square:
    """Represents a square
    Attributes:
        __size (int): size of a side of the square
        __position (tuple): position of the square in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the square
        Args:
            size (int): size of a side of the square
            position (tuple): position of the square in 2D space
        Returns:
            None
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size
        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size
        Args:
            value (int): the size of a side of the square
        Returns:
            None
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        """Getter for position
        Returns:
            The position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position
        Args:
            value (tuple): the position of the square in 2D space
        Returns:
            None
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not all(isinstance(n, int) for n in value) or \
           not all(n >= 0 for n in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Calculates the square's area
        Returns:
            The area of the square
        """
        return self.__size ** 2

    def my_print(self):
        """Prints the square with the character #
        Returns:
            None
        """
        if self.__size == 0:
            print()
        else:
            print("\n" * self.__position[1], end="")
            print("\n".join(" " * self.__position[0] + "#" * self.__size for _ in range(self.__size)))
