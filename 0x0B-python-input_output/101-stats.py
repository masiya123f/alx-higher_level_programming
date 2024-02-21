#!/usr/bin/python3
"""
This is a Python script. The line at the top tells the system that this script should be run using Python 3.
"""

# This is a function called 'print_stats'. It prints the accumulated metrics.
def print_stats(size, status_codes):
    """
    Print accumulated metrics.

    Args:
        size (int): The accumulated read file size.
        status_codes (dict): The accumulated count of status codes.
    """
    # This line prints the total file size.
    print("File size: {}".format(size))
    # This loop goes through each status code in sorted order.
    for key in sorted(status_codes):
        # It prints the status code and its count.
        print("{}: {}".format(key, status_codes[key]))

# This line checks if this file is being run directly or being imported as a module. If it's run directly, the code within this if block will be executed.
if __name__ == "__main__":
    import sys

    # These lines initialize the total size, the status codes dictionary, the valid codes list, and the count.
    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    # This 'try' block attempts to read lines from standard input.
    try:
        for line in sys.stdin:
            # If the count is 10, it prints the stats and resets the count.
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                # Otherwise, it increments the count.
                count += 1

            # This line splits the line into words.
            line = line.split()

            # This 'try' block attempts to add the size of the file (the last word on the line) to the total size.
            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            # This 'try' block attempts to increment the count of the status code (the second to last word on the line) in the status codes dictionary.
            try:
                if line[-2] in valid_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        # After the loop, it prints the stats one last time.
        print_stats(size, status_codes)

    # This 'except' block catches a KeyboardInterrupt exception (which happens when you press CTRL+C), prints the stats, and then re-raises the exception.
    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
