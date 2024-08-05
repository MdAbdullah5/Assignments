import numpy as np

# Create a 1D array
arr = np.array([1, 2, 3, 4, 5, 6])

# Reshape to a 2x3 matrix
reshaped_arr = arr.reshape(2, 3)

# Print original and reshaped array
print("Original array:")
print(arr)
print("Reshaped array:")
print(reshaped_arr)