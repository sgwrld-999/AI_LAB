''''
Write a NumPy program-
Create a 4 x 5 matrix with values ranging from 1 to 20 and find the following:

i. Create an array of 10 zeros,10 ones, 10 fives.
ii. Create an array of all the even integers from 10 to 50.
iii. Generate a random number between 0 and 1.
iv. Save the matrix (generated in question iv) to a text file and load it.
'''
import numpy as np

# i. Create an array of 10 zeros, 10 ones, 10 fives.
array_zeros = np.zeros(10)
array_ones = np.ones(10)
array_fives = np.full(10, 5)

# ii. Create an array of all the even integers from 10 to 50.
array_even_integers = np.arange(10, 51, 2)

# iii. Generate a random number between 0 and 1.
random_number = np.random.rand()

# iv. Create a 4 x 5 matrix with values ranging from 1 to 20.
matrix = np.arange(1, 21).reshape(4, 5)

# Save the matrix to a text file
np.savetxt('matrix.txt', matrix)

# Load the matrix from the text file
loaded_matrix = np.loadtxt('matrix.txt')

# Print the results
print("i. Array of 10 zeros:")
print(array_zeros)

print("\nArray of 10 ones:")
print(array_ones)

print("\nArray of 10 fives:")
print(array_fives)

print("\nii. Array of even integers from 10 to 50:")
print(array_even_integers)

print("\niii. Random number between 0 and 1:")
print(random_number)

print("\niv. Original Matrix:")
print(matrix)

print("\nLoaded Matrix from File:")
print(loaded_matrix)
