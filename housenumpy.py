import numpy as np

# here Each row represents one house
houses = np.array([
    [800, 2, 10],
    [1200, 3, 5],
    [600, 1, 20],
    [1500, 4, 2]
])

# Select the area of every house
areas = houses[:, 0]

# Select the bedrooms of every house
bedrooms = houses[:, 1]

# Find houses with area greater than 1000 sq ft
large_houses = houses[houses[:, 0] > 1000]

print("Areas:", areas)
print("Bedrooms:", bedrooms)
print("Large houses:\n", large_houses)