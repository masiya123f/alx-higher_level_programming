#!/usr/bin/python3
# This line indicates that the script should be run using Python 3.

"""
Contains the read_file function
"""
# This is a module-level docstring that briefly describes what is in the module.

def read_file(file_path=""):
    """
    Reads a text file (UTF8) and prints it to stdout
    """
    # This is a function called 'read_file' that takes one argument 'file_path'. 
    # If no argument is provided, it defaults to an empty string.

    with open(file_path, "r", encoding="utf-8") as file:
        # This line opens the file with the given 'file_path' in read mode ('r') with UTF-8 encoding. 
        # 'file' is a file object we can use to perform various operations on the file.

        print(file.read(), end="")
        # This line reads the entire content of the file with 'file.read()' and then prints it. 
        # The 'end=""' argument in the print function prevents it from printing a newline character after the output.
