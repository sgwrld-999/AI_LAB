'''Given an array of integers- [10,16,71,9],[71,91,31,51].Write a program to print-
    i. Dimension of the array
    ii. Shape of the array
    iii.Size of the array
'''
import numpy as np

# Create a NumPy array
arr = np.array([[10, 16, 71, 91, 31],[10, 16, 71, 91, 31]])

# Use NumPy functions on the array
print("The dimension of the array is:", arr.ndim)
print("The shape of the array is:", arr.shape)
print("The size of the array is:", arr.size)

'''The shape `(5,)` indicates a one-dimensional NumPy array with 5 elements. 
The comma is included to represent the shape as a tuple, even though it's a single-element tuple in this case.'''