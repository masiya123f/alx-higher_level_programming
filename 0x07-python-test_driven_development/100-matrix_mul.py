#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    """Multiplies two matrices (m_a and m_b).

    Args:
        m_a: The first matrix (list of lists of integers or floats).
        m_b: The second matrix (list of lists of integers or floats).

    Returns:
        The resulting matrix as a new list of lists.

    Raises:
        TypeError: If m_a or m_b is not a list, a list of lists, or doesn't  contain valid numbers.
        ValueError: If matrices are empty, have incompatible shapes, or are not rectangles.
    """

    # Type & content validation
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    if not m_a or not m_a[0]:
        raise ValueError("m_a can't be empty")
    if not m_b or not m_b[0]:
        raise ValueError("m_b can't be empty")

    if not all((isinstance(item, (int, float)) for row in m_a for item in row)):
        raise TypeError("m_a should contain only integers or floats")
    if not all((isinstance(item, (int, float)) for row in m_b for item in row)):
        raise TypeError("m_b should contain only integers or floats")

    # Validate shape: ensure rows have the same size
    row_size_a = len(m_a[0])
    if not all(len(row) == row_size_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    row_size_b = len(m_b[0])
    if not all(len(row) == row_size_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # Compatibility check (columns in m_a must match rows in m_b)
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform the matrix multiplication (implementation omitted for brevity)
    # ...
