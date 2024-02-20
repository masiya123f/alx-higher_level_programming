#!/usr/bin/python3
# Shebang for Python 3.

"""
Contains the class BasicShape and subclass Quadrilateral
"""

BasicShape = __import__('7-base_geometry').BaseGeometry


class Quadrilateral(BasicShape):
    # Defines a class named 'Quadrilateral' that inherits from 'BasicShape'.

    """A representation of a quadrilateral"""
    # Class docstring.

    def __init__(self, breadth, length):
        # Defines the initializer method for the class.

        """instantiation of the quadrilateral"""
        # Method docstring.

        self.integer_validator("breadth", breadth)
        # Validates that 'breadth' is an integer greater than 0.

        self.__width = breadth
        # Sets the private instance attribute '__width' to 'breadth'.

        self.integer_validator("length", length)
        # Validates that 'length' is an integer greater than 0.

        self.__height = length
        # Sets the private instance attribute '__height' to 'length'.
