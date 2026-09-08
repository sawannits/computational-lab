import numpy as np

# Taking a matrix
A = np.array([[4, 1],
              [2, 3]])

print("Matrix:")
print(A)

# Finding eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

print("\nEigenvalues:")
print(eigenvalues)

print("\nEigenvectors:")
print(eigenvectors)
