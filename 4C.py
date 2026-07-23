import numpy as np

# Creating an array with 10 elements
arr_10 = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])
print("Original Array with 10 elements:")
print(arr_10)

# Slicing elements from index 1 up to index 5 (Note: Index 5 is excluded, so it takes indices 1, 2, 3, 4)
# If you strictly want elements corresponding to positions 1st to 5th (indices 0 to 4):
sliced_array = arr_10[0:5]

print("\nSliced Array (1st to 5th elements):")
print(sliced_array)
