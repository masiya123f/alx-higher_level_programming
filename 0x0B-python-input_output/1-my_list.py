#!/usr/bin/python3
# Shebang for Python 3.

"""
contains the MyList class
"""
# Module docstring.

class MyList(list):
    # MyList class inherits from list.

    """a subclass of list"""
    # Class docstring.

    def __init__(self):
        # Initializer method.

        """initializes the object"""
        # Method docstring.

        super().__init__()
        # Calls list's initializer.

    def print_sorted(self):
        # Method to print sorted list.

        """prints the sorted list"""
        # Method docstring.

        print(sorted(self))
        # Prints sorted list.
