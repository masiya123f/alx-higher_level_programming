#!/usr/bin/python3
# Shebang for Python 3.

"""
Contains the class BasicShape and subclass Quadrilateral
"""

Quadrilateral = __import__('9-rectangle').Rectangle


class Cube(Quadrilateral):
    # Defines a class named 'Cube' that inherits from 'Quadrilateral'.

    """A representation of a cube"""
    # Class docstring.

    def __init__(self, edge_length):
        # Defines the initializer method for the class.

        """instantiation of the cube"""
        # Method docstring.

        self.integer_validator("edge_length", edge_length)
        # Validates that 'edge_length' is an integer greater than 0.

        self.__size = edge_length
        # Sets the private instance attribute '__size' to 'edge_length'.

        super().__init__(edge_length, edge_length)
        # Calls the initializer of the superclass (Quadrilateral) with 'edge_length' as both parameters.

    def area(self):
        # Defines a method named 'area'.

        """"returns the area of the cube"""
        # Method docstring.

        return self.__size ** 2
        # Returns the area of the cube.
