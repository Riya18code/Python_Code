import numpy as np  # The standard naming convention of numpy(python library)

# Create 1D and 2D arrays from standard Python lists
arr_1d = np.array([1, 2, 3, 4, 5])
arr_2d = np.array([[1, 2, 3], [4, 5, 6]])

# Generate arrays pre-filled with specific values
zeros = np.zeros((3, 3))       # 3x3 matrix of 0.0
ones = np.ones((2, 4))         # 2x4 matrix of 1.0
full = np.full((2, 2), 7)      # 2x2 matrix filled with 7
identity = np.eye(3)           # 3x3 identity matrix

# Generate arrays with numerical ranges
sequence = np.arange(0, 10, 2) # Array from 0 to 8, stepping by 2: [0, 2, 4, 6, 8]
linear_space = np.linspace(0, 1, 5) # 5 evenly spaced points between 0 and 1


arr = np.array([[1, 2, 3], [4, 5, 6]])

print("Dimensions",arr.ndim)    
print("Shape",arr.shape)  
print("Size",arr.size)  
print("Data Type",arr.dtype)  