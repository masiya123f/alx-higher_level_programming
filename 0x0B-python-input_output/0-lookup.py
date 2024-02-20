#!/usr/bin/python3
# This line is called a shebang. It tells the system that this script should be run with Python 3.

"""
Contains the lookup function
"""
# This is a docstring at the module level. It provides a brief description of what the module contains.

def lookup(obj):
    # This line defines a function named 'lookup' that takes one argument, 'obj'.

    """
    returns a list of available attributes and methods of an object
    """
    # This is a docstring at the function level. It explains what the function does.

    return dir(obj)
    # This line returns a list of the names of all attributes and methods that are available for the object 'obj'.
    # It uses the built-in Python function 'dir()'.
