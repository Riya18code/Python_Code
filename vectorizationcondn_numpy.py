import numpy as np

marks= np.array([17,45,60,75,20])
updated_marks=marks+5
passed=updated_marks>=40
passed=np.where(updated_marks>=40,"pass","fail")
print("updated marks:",updated_marks)
print("passed marks:",passed)