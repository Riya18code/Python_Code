import numpy as np

salaries =np.array([10000,20000,50000,np.nan,49000])
print(np.isnan(salaries)) #check for nan value

attendence=np.array([98,74,32,np.nan,62])
cleaned_attendence= np.nan_to_num(attendence,nan=np.nanmean(attendence))

print(cleaned_attendence)

low_attendence=cleaned_attendence[cleaned_attendence<80]
print(low_attendence)