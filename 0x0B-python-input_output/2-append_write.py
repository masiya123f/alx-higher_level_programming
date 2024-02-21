#!/usr/bin/python3
"""
This is a Python script. The line at the top tells the system that this script should be run using Python 3.
"""

# This is a function called 'append_write'. Functions are like little machines that do a specific job.
def append_write(filename="", text=""):
    """
    This function appends some text to a file.
    The 'filename' parameter is the name of the file we want to append to.
    The 'text' parameter is the text we want to append.
    If no filename or text is given, it will default to an empty string, which means no file and nothing to append.
    """
    
    # 'with' is used here to properly manage resources. It automatically closes the file after we're done with it.
    # 'open' is a function that opens a file. We give it the filename, the mode 'a' for append, and specify the encoding.
    with open(filename, 'a', encoding='utf=8') as f:
        
        # 'f.write(text)' appends the 'text' to the file.
        # The function then returns the number of characters that were appended.
        return f.write(text)
