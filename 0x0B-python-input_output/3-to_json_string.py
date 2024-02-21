#!/usr/bin/python3
"""
This is a Python script. The line at the top tells the system that this script should be run using Python 3.
"""

# This line imports the 'json' module, which provides functions for working with JSON data.
import json

# This is a function called 'to_json_string'. Functions are like little machines that do a specific job.
def to_json_string(my_obj):
    """
    This function takes an object 'my_obj' and converts it to a JSON string.
    JSON (JavaScript Object Notation) is a format for storing and transporting data.
    """
    
    # 'json.dumps()' is a function that converts a Python object into a JSON string.
    return json.dumps(my_obj)
