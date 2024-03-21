def add_matrices(A, B):
  """Adds two matrices.

  Args:
    A: A list of lists representing the first matrix.
    B: A list of lists representing the second matrix.

  Returns:
    A list of lists representing the sum of the two matrices.
  """

  result = [[0 for _ in range(len(A[0]))] for _ in range(len(A))]
  for i in range(len(A)):
    for j in range(len(A[0])):
      result[i][j] = A[i][j] + B[i][j]
  return result


def multiply_matrices(A, B):
  """Multiplies two matrices.

  Args:
    A: A list of lists representing the first matrix.
    B: A list of lists representing the second matrix.

  Returns:
    A list of lists representing the product of the two matrices.
  """

  result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]
  for i in range(len(A)):
    for j in range(len(B[0])):
      for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]
  return result


# Example usage:

A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

print(add_matrices(A, B))
# [[6, 8], [10, 12]]

print(multiply_matrices(A, B))
# [[19, 22], [43, 50]]