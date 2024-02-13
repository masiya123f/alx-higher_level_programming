#!/usr/bin/python3

def matrix_divided(matrix, div):
  """Divides all elements of a matrix.

  Args:
      matrix: List of lists containing integers or floats.
      div: The divisor (integer or float).

  Returns:
      A new list of lists where each element is a result of the division.

  Raises:
      TypeError: If `matrix` is not a list of lists of integers/floats.
      TypeError: If rows of `matrix` are not of the same size.
      TypeError: If `div` is not a number.
      ZeroDivisionError: If `div` is zero.
  """

  if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
    raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

  row_size = len(matrix[0])  # Reference for checking subsequent row sizes
  for row in matrix:
    if len(row) != row_size:
      raise TypeError("Each row of the matrix must have the same size")

    if not all(isinstance(item, (int, float)) for item in row):
      raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

  if not isinstance(div, (int, float)):
    raise TypeError("div must be a number")

  if div == 0:
    raise ZeroDivisionError("division by zero")

  result_matrix = [[round(num / div, 2) for num in row] for row in matrix]
  return result_matrix
