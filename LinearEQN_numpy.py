import numpy as np
#solving for equation:-2x+y=8 and x+3y=13

A= np.array([[2,1],[1,3]])
B= np.array([8,13])
Solution= np.linalg.solve(A,B)
print(Solution)
