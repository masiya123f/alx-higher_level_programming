#!/usr/bin/python3
import numpy as np   # Import NumPy
lazy_matrix_mul = __import__('101-lazy_matrix_mul').lazy_matrix_mul

m_a = np.array([[1, 2], [3, 4]])  # Convert to NumPy arrays
m_b = np.array([[1, 2], [3, 4]])

print(lazy_matrix_mul(m_a, m_b))
print(lazy_matrix_mul(np.array([[1, 2]]), np.array([[3, 4], [5, 6]])))
