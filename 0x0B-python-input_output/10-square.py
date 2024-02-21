#!/usr/bin/python3
"""
This is a Python script. The line at the top tells the system that this script should be run using Python 3.
"""

# This is a class called 'Student'. Classes are like blueprints for creating objects. An object is an instance of a class.
class Student:
    """Represent a student."""

    # This is the initializer method for the class. It gets called when you create a new 'Student' object.
    def __init__(self, first_name, last_name, age):
        """
        Initialize a new Student.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        # These lines set the attributes of the student. Attributes are like variables that belong to an object.
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    # This is a method of the class. Methods are like functions that belong to an object.
    def to_json(self, attrs=None):
        """
        Get a dictionary representation of the Student.

        If attrs is a list of strings, represents only those attributes
        included in the list.

        Args:
            attrs (list): (Optional) The attributes to represent.
        """
        # This 'if' statement checks if 'attrs' is a list of strings.
        if (type(attrs) == list and
                all(type(ele) == str for ele in attrs)):
            # If it is, it returns a dictionary where the keys are the attribute names and the values are the attribute values.
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        # If 'attrs' is not a list of strings, it returns a dictionary of all the object's attributes.
        return self.__dict__
