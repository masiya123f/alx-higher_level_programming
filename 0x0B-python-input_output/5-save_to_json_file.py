#!/usr/bin/python3
"""
This is a Python script. The line at the top tells the system that this script should be run using Python 3.
"""

# This line imports the 'json' module, which provides functions for working with JSON data.
import json

# This is a function called 'save_to_json_file'. Functions are like little machines that do a specific job.
def save_to_json_file(my_obj, filename):
    """
    This function takes a Python object 'my_obj' and a filename, and writes the object to the file in JSON format.
    JSON (JavaScript Object Notation) is a format for storing and transporting data.
    """
    
    # 'with' is used here to properly manage resources. It automatically closes the file after we're done with it.
    # 'open' is a function that opens a file. We give it the filename, the mode 'w' for write, and specify the encoding.
    with open(filename, 'w', encoding='utf-8') as f:
        
        # 'json.dump()' is a function that writes a Python object to a file in JSON format.
        json.dump(my_obj, f)
