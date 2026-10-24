import numpy as np

rupee = np.array([1200, 1500, 900, 2000, 1800])

print(rupee[0])
print(rupee[2])
print(rupee[4])
print(rupee[-1])
print(rupee[1:4])
print(rupee[::-1])
#2d
marks = np.array([
    [80, 75, 90],
    [65, 85, 70],
    [95, 92, 88]
])

print(marks[0, 0])
print(marks[1, 2])
print(marks[2, 1])