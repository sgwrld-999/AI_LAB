#You are given a N X M integer array matrix with space-separated elements ( N= rows
# and M= columns).Calculate the transpose and flatten results. First, print the
# transposed array and then print the flatten.
import numpy as np

print("Enter the number of rows and columns respectively:")
row = int(input("Rows: "))
col = int(input("Columns: "))

matrix = np.zeros((row, col), dtype=int)

print("Enter the elements of the matrix:")
for i in range(row):
    for j in range(col):
        matrix[i][j] = int(input(f"Matrix[{i}][{j}]: "))

print("The OG Matrix:\n")
print(matrix)

transposed_matrix = np.transpose(matrix)
print("\nTransposed Matrix:")
print(transposed_matrix)

flattened_matrix = matrix.flatten()
print("\nFlattened Matrix:")
print(flattened_matrix)
