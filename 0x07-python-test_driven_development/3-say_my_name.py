#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """Prints a formatted string with the provided first and last names.

    Args:
        first_name: The first name (required).
        last_name: The last name (optional).

    Raises:
        TypeError: If `first_name` or `last_name` is not a string.
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
