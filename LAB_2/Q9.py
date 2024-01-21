# Create a random matrix of 8 x 7 (where columns are the features and rows
# are the patterns) and find the maximum and minimum values from each feature.

import numpy as np

matrix = np.random.rand(8, 7)

print("The OG Matrix:\n")
print(matrix)

print("The maximum of the OG Matrix:\n")
print(np.max(matrix))

print("The minimum of the OG Matrix:\n")
print(np.min(matrix))

