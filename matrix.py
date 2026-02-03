# import numpy as np
# identity_matrix = np.identity(4)
# print("4x4 Identity Matrix:")
# print(identity_matrix)



# import numpy as np
# matrix1 = np.random.randint(1, 10, (3, 3))
# matrix2 = np.random.randint(1, 10, (3, 3))
#
# print("Matrix 1:")
# print(matrix1)
#
# print("\nMatrix 2:")
# print(matrix2)
# addition = matrix1 + matrix2
# print("\nMatrix Addition:")
# print(addition)
# multiplication = np.dot(matrix1, matrix2)
# print("\nMatrix Multiplication:")
# print(multiplication)


import numpy as np

print("Enter elements for 5x3 matrix:")
matrix1 = []
for i in range(5):
    row = list(map(int, input().split()))
    matrix1.append(row)

print("Enter elements for 3x2 matrix:")
matrix2 = []
for i in range(3):
    row = list(map(int, input().split()))
    matrix2.append(row)

# Convert lists to NumPy arrays
matrix1 = np.array(matrix1)
matrix2 = np.array(matrix2)

# Multiply matrices
product = np.dot(matrix1, matrix2)

print("\nProduct Matrix (5x2):")
print(product)
