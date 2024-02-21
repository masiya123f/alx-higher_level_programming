#!/usr/bin/python3
"""
This is a Python script. The line at the top tells the system that this script should be run using Python 3.
"""

# This line imports the 'sys' module, which provides access to some variables used or maintained by the Python interpreter.

import sys

# This line checks if this file is being run directly or being imported as a module. If it's run directly, the code within this if block will be executed.
if __name__ == "__main__":
    
    # These lines import the 'save_to_json_file' and 'load_from_json_file' functions from other Python scripts.
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

    # This 'try' block attempts to load a list from the file "add_item.json". If the file does not exist, it will raise a 'FileNotFoundError'.
    try:
        items = load_from_json_file("add_item.json")
    # The 'except' block catches the error and creates a new list instead.
    except FileNotFoundError:
        items = []
    
    # This line extends the 'items' list with the arguments passed to the script (except the first one, which is the script name itself).
    items.extend(sys.argv[1:])
    
    # Finally, it saves the 'items' list back to the file "add_item.json" in JSON format.
    save_to_json_file(items, "add_item.json")
