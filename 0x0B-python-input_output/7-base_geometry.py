#!/usr/bin/python3
# Shebang for Python 3.

"""
Contains the class BasicShape
"""
# Module docstring.

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
