#!/usr/bin/python3
# Shebang for Python 3.

"""
This module contains the function is_same_class
"""
# Module docstring.

def is_same_class(obj, a_class):
    # Defines a function that checks if an object is of a specific class.

    """return true if obj is the exact class a_class, otherwise false"""
    # Function docstring.

    return (type(obj) == a_class)
    # Returns True if the type of 'obj' is exactly 'a_class', otherwise False.
