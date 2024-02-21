#!/usr/bin/python3
"""
This is a Python script. The line at the top tells the system that this script should be run using Python 3.
"""

# This is a function called 'write_file'. Functions are like little machines that do a specific job.
def write_file(filename="", text=""):
    """
    This function writes some text to a file.
    The 'filename' parameter is the name of the file we want to write to.
    The 'text' parameter is the text we want to write.
    If no filename or text is given, it will default to an empty string, which means no file and nothing to write.
    """
    
    # 'with' is used here to properly manage resources. It automatically closes the file after we're done with it.
    # 'open' is a function that opens a file. We give it the filename, the mode 'w' for write, and specify the encoding.
    with open(filename, 'w', encoding='utf=8') as f:
        
        # 'f.write(text)' writes the 'text' to the file.
        # The function then returns the number of characters that were written.
        return f.write(text)
