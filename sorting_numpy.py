import numpy as np
arr =np.array([3,1,4,2,7,6,11,5])
print(np.sort(arr))

print(np.argsort(arr))
print(np.sort(arr)[::-1])
marks=np.array([[10,40,11,34],[90,78,54,22],[12,73,9,0]])
print(np.sort(marks,axis=1)) #sorts the each row independently

print(np.sort(marks,axis=0)) #sorts the each column independently
