#!/usr/bin/python3
def add_integer(a, b=98):
    """Adds two integers or floats after casting them to integers.

    Args:
        a: The first number.
        b: The second number (has a default value of 98).

    Returns:
        The sum of a and b as an integer.

    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Cast floats to integers
    a = int(a)
    b = int(b)

    return a + b
