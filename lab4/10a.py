import numpy as np

# Taking two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Addition
print("\nAddition:")
print(A + B)

# Subtraction
print("\nSubtraction:")
print(A - B)

# Multiplication
print("\nMultiplication:")
print(np.dot(A, B))

# Transpose
print("\nTranspose of A:")
print(A.T)

print("\nTranspose of B:")
print(B.T)
