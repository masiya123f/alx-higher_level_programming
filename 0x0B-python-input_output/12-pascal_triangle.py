#!/usr/bin/python3
# 14-pascal_triangle.py
"""
This is a Python script. The line at the top tells the system that this script should be run using Python 3.
"""

# This is a function called 'pascal_triangle'. Functions are like little machines that do a specific job.
def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    
    # If 'n' is less than or equal to 0, the function returns an empty list.
    if n <= 0:
        return []

    # This line creates a list of lists, where the first list is just [1].
    triangles = [[1]]
    
    # This loop continues until the length of 'triangles' is equal to 'n'.
    while len(triangles) != n:
        
        # 'tri' is the last list in 'triangles'.
        tri = triangles[-1]
        
        # 'tmp' is a new list that starts with the number 1.
        tmp = [1]
        
        # This loop goes through each pair of numbers in 'tri' (except the last number).
        for i in range(len(tri) - 1):
            
            # It adds each pair of numbers and appends the result to 'tmp'.
            tmp.append(tri[i] + tri[i + 1])
        
        # After the loop, it appends another 1 to the end of 'tmp'.
        tmp.append(1)
        
        # It then appends 'tmp' to 'triangles'.
        triangles.append(tmp)
    
    # Finally, it returns 'triangles'.
    return triangles
