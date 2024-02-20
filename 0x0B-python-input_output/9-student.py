#!/usr/bin/python3
# Shebang for Python 3.

"""
Contains the class BasicShape and subclass Quadrilateral
"""

class BasicShape:
    # Defines a class named 'BasicShape'.

    """A class with public instance methods calculate_area and integer_validator"""
    # Class docstring.

    def calculate_area(instance):
        # Defines a method named 'calculate_area'.

        """raises an exception when called"""
        # Method docstring.

        raise Exception("calculate_area() is not implemented")
        # Raises an exception with the message "calculate_area() is not implemented".

    def integer_validator(instance, attribute, quantity):
        # Defines a method named 'integer_validator'.

        """validates that quantity is an integer greater than 0"""
        # Method docstring.

        if type(quantity) is not int:
            raise TypeError("{:s} must be an integer".format(attribute))
        # Raises a TypeError if 'quantity' is not an integer.

        if quantity <= 0:
            raise ValueError("{:s} must be greater than 0".format(attribute))
        # Raises a ValueError if 'quantity' is less than or equal to 0.


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

    def calculate_area(self):
        # Defines a method named 'calculate_area'.

        """returns the area of the quadrilateral"""
        # Method docstring.

        return self.__width * self.__height
        # Returns the area of the quadrilateral.

    def __str__(self):
        # Defines the string representation of the object.

        """informal string representation of the quadrilateral"""
        # Method docstring.

        return "[Quadrilateral] {:d}/{:d}".format(self.__width, self.__height)
        # Returns a string that represents the quadrilateral.
