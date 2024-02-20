#!/usr/bin/python3
# Shebang for Python 3.

"""
Contains the is_kind_of_class function
"""
# Module docstring.

def is_kind_of_class(obj, a_class):
    # Defines a function that checks if an object is an instance or inherited from a specific class.

    """True if obj is an instance or inherited from a_class, else False"""
    # Function docstring.

    return (isinstance(obj, a_class))
    # Returns True if 'obj' is an instance or inherited from 'a_class', otherwise False.
