import numpy as np
temperatures= np.array([
    [30.8,21,8.6],[16,29.7,12.5]
])
print("Temperatures:\n", temperatures)
print("shape of the array",temperatures.shape)
print("Dimension of the array",temperatures.ndim)
print("size of the array",temperatures.size)
print("Data type of the array:",temperatures.dtype)
print("updated array:",temperatures+5)