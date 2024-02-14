#!/usr/bin/python3
class LockedClass:
    """
    A class that restricts dynamic attribute creation, with an exception for 'first_name'.
    """

    __slots__ = ['first_name']

    def __setattr__(self, name, value):
        """Overrides the default attribute setting behavior.

        Args:
            name (str): The name of the attribute to be set.
            value (any): The value to be assigned to the attribute.
        """
        if name == 'first_name':
            super().__setattr__(name, value)
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
