import numpy as np

a= np.array([[1,2],[2,4]])
b= np.array([[1,1],[2,6]])

result= a@b
print(result)
#or we can also use np.dot() to perform matrix multiplication.
result2=np.dot(a,b)
print(result2)