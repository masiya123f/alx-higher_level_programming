#!/usr/bin/python3
"""
This is a Python script. The line at the top tells the system that this script should be run using Python 3.
"""

# This is a function called 'read_file'. Functions are like little machines that do a specific job.
def read_file(filename=""):
    """
    This function reads a text file and prints it to the screen.
    The 'filename' parameter is the name of the file we want to read.
    If no filename is given, it will default to an empty string, which means no file.
    """
    
    # 'with' is used here to properly manage resources. It automatically closes the file after we're done with it.
    # 'open' is a function that opens a file. We give it the filename, the mode 'r' for read, and specify the encoding.
    with open(filename, "r", encoding="utf-8") as f:
        
        # 'f.read()' reads the entire contents of the file.
        # 'print' displays those contents to the screen.
        # 'end=""' means that we don't want to add a newline character at the end, which 'print' usually does by default.
        print(f.read(), end="")

