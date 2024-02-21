#!/usr/bin/python3
"""
This is a Python script. The line at the top tells the system that this script should be run using Python 3.
"""

# This line imports the 'json' module, which provides functions for working with JSON data.
import json

# This is a function called 'load_from_json_file'. Functions are like little machines that do a specific job.
def load_from_json_file(filename):
    """
    This function takes a filename and creates a Python object from a JSON file.
    JSON (JavaScript Object Notation) is a format for storing and transporting data.
    """
    
    # 'with' is used here to properly manage resources. It automatically closes the file after we're done with it.
    # 'open' is a function that opens a file. We give it the filename.
    with open(filename) as f:
        
        # 'json.load()' is a function that reads a JSON file and converts it into a Python object.
        return json.load(f)
