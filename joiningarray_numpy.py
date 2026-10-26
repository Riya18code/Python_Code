import numpy as np

a= np.array([[1,2,3],[4,5,6]])
b= np.array([[7,8,9],[10,11,12]])
vertical=np.concatenate((a,b),axis=0)
horizontal=np.concatenate((a,b),axis=1)
print(vertical)
print(horizontal)
