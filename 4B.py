import numpy as np

# Create a sample array
arr = np.array([10, 20, 30, 40, 50])

print("Original Array:", arr)

# 1. Arithmetic Operations (element-wise)
print("Addition (+ 5):", arr + 5)
print("Multiplication (* 2):", arr * 2)

# 2. Universal Functions (ufuncs)
print("Square Root:", np.sqrt(arr))
print("Exponential:", np.exp(arr))

# 3. Aggregation Operations
print("Sum of elements:", np.sum(arr))
print("Mean value:", np.mean(arr))
print("Maximum value:", np.max(arr))
print("Minimum value:", np.min(arr))
