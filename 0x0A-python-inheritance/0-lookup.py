#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of attribute and method names.
    """
    attributes = dir(obj)
    return [attr for attr in attributes if not attr.startswith('__')]
