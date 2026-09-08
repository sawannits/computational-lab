import numpy as np

# Taking a matrix
A = np.array([[1, 2],
              [3, 4]])

print("Matrix:")
print(A)

# Finding determinant
det = np.linalg.det(A)
print("\nDeterminant:")
print(det)

# Finding inverse
if det != 0:
    inverse = np.linalg.inv(A)
    print("\nInverse:")
    print(inverse)
else:
    print("\nInverse does not exist because determinant is zero.")

# Finding rank
rank = np.linalg.matrix_rank(A)
print("\nRank:")
print(rank)
