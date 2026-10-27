import numpy as np

marks= np.array([[40,45,50],[80,67,92],[57,99,12]])
scaled_marks= marks/100

print("scaled marks:",scaled_marks)

#machine learning model often requires data to be scaled to a specific range,such as 0 to 1.