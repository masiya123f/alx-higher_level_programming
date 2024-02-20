#!/usr/bin/python3
# Shebang for Python 3.

"""
Contains the class MyNum
"""

class MyNum(int):
    # Defines a class named 'MyNum' that inherits from 'int'.

    """rebel version of an integer, perfect for opposite day!"""
    # Class docstring.

    def __new__(cls, *args, **kwargs):
        # Defines the method to create a new instance of the class.

        """create a new instance of the class"""
        # Method docstring.

        return super(MyNum, cls).__new__(cls, *args, **kwargs)
        # Calls the method to create a new instance of the superclass (int).

    def __eq__(self, other):
        # Defines the method to check if two objects are equal.

        """what was != is now =="""
        # Method docstring.

        return int(self) != other
        # Returns True if 'self' is not equal to 'other', otherwise False.

    def __ne__(self, other):
        # Defines the method to check if two objects are not equal.

        """what was == is now !="""
        # Method docstring.

        return int(self) == other
        # Returns True if 'self' is equal to 'other', otherwise False.
