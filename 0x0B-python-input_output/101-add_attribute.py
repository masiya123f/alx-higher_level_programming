#!/usr/bin/python3
# This is the shebang that sets the interpreter for this script to Python 3.

"""Defines a function that adds properties to objects."""
# This is a docstring that provides a brief description of what the module does.

def add_property(object, property, val):
    # This line defines a function named 'add_property' that takes three parameters: 'object', 'property', and 'val'.

    """Add a new property to an object if possible.
    Args:
        object (any): The object to add a property to.
        property (str): The name of the property to add to object.
        val (any): The value of property.
    Raises:
        TypeError: If the property cannot be added.
    """
    # This is a docstring that provides a detailed description of what the function does, its arguments, and exceptions it raises.

    if not hasattr(object, "__dict__"):
        # This line checks if 'object' has a '__dict__' attribute. If it doesn't, it means that 'object' can't have arbitrary attributes added to it.

        raise TypeError("can't add new property")
        # This line raises a TypeError with the message "can't add new property".

    setattr(object, property, val)
    # This line sets the attribute 'property' of 'object' to 'val'. If 'property' doesn't exist, it's created.
