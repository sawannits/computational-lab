# Two matrices
A = [[1, 2],
     [3, 4]]

B = [[5, 6],
     [7, 8]]

# Addition
addition = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        addition[i][j] = A[i][j] + B[i][j]

print("Addition:")
for row in addition:
    print(row)


# Subtraction
subtraction = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        subtraction[i][j] = A[i][j] - B[i][j]

print("\nSubtraction:")
for row in subtraction:
    print(row)


# Multiplication
multiplication = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        for k in range(2):
            multiplication[i][j] += A[i][k] * B[k][j]

print("\nMultiplication:")
for row in multiplication:
    print(row)


# Transpose of A
transpose = [[0, 0], [0, 0]]

for i in range(2):
    for j in range(2):
        transpose[j][i] = A[i][j]

print("\nTranspose of A:")
for row in transpose:
    print(row)
