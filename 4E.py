import numpy as np

# Sample array
arr = np.array([12, 45, 23, 67, 45, 89, 67, 89])

# Find the maximum value in the array
max_val = np.max(arr)
print(f"Maximum value in the array is: {max_val}")

# Create a boolean filter array where elements equal the maximum value
filter_arr = (arr == max_val)
print("Filter Array (Booleans):", filter_arr)

# Apply the filter to extract the maximum values
result = arr[filter_arr]
print("Filtered Maximum Values:", result)
