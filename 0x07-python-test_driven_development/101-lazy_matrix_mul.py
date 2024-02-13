#!/usr/bin/python3
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a: The first matrix.
        m_b: The second matrix.

    Returns:
        The resulting matrix from the multiplication.

    Raises:
       TypeError: If m_a or m_b is not a NumPy ndarray.
       ValueError: If m_a and m_b cannot be multiplied (incompatible shapes).
    """
    if not isinstance(m_a, np.ndarray):
        raise TypeError("m_a must be a NumPy ndarray")

    if not isinstance(m_b, np.ndarray):
        raise TypeError("m_b must be a NumPy ndarray")

    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e 
