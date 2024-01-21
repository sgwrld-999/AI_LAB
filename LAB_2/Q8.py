'''
Create two random arrays of any dimension and perform the following
operations:
    i. Concatenate two arrays.
    ii. Sort both the arrays.
    iii. Add the two arrays
    iv. Subtract the two arrays
    v. Multiply two arrays
'''
import numpy as np

# Create two random arrays
arr1 = np.random.rand(3, 4)
arr2 = np.random.rand(3, 4)

# i. Concatenate two arrays
arr_concatenated = np.concatenate((arr1, arr2))
print("Concatenated Array:")
print(arr_concatenated)

# ii. Sort both arrays
arr1_sorted = np.sort(arr1)
arr2_sorted = np.sort(arr2)
print("Sorted Array 1:")
print(arr1_sorted)
print("Sorted Array 2:")
print(arr2_sorted)

# iii. Add the two arrays
arr_sum = arr1 + arr2
print("Sum of Arrays:")
print(arr_sum)

# iv. Subtract the two arrays
arr_difference = arr1 - arr2
print("Difference of Arrays:")
print(arr_difference)

# v. Multiply two arrays
arr_product = arr1 * arr2
print("Product of Arrays:")
print(arr_product)

# vi. Divide the two arrays
arr_quotient = np.divide(arr1, arr2, out=np.zeros_like(arr1), where=(arr2 != 0))
print("Quotient of Arrays:")
print(arr_quotient)





