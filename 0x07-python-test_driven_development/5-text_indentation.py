#!/usr/bin/python3
def text_indentation(text):
    """Prints a text with 2 new lines after characters '.', '?', and ':'.

    Args:
        text:  The text to be printed.

    Raises:
        TypeError: If `text` is not a string.
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"
    i = 0

    while i < len(text):
        print(text[i], end="")  # Print without automatic newline

        if text[i] in delimiters:
            print("\n\n", end="")  # Two newlines after delimiter
            i += 1  # Skip to the next character after the delimiter

            #  Handle consecutive spaces
            while i < len(text) and text[i] == ' ':
                i += 1
        else:
            i += 1
