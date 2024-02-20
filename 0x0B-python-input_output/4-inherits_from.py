#!/usr/bin/python3
# Shebang for Python 3.

"""
Contains the inherits_from function
"""
# Module docstring.

def inherits_from(obj, a_class):
    # Defines a function that checks if an object is a subclass of a specific class.

    """returns true if obj is a subclass of a_class, otherwise false"""
    # Function docstring.

    return(issubclass(type(obj), a_class) and type(obj) != a_class)
    # Returns True if 'obj' is a subclass of 'a_class', but not an instance of 'a_class' itself, otherwise False.
