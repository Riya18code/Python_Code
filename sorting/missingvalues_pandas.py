import pandas as pd
import numpy as np
data= {
    "Name":["John", "Alice","Bob",np.nan,"David",np.nan,"Eve"],
    "Age":[25,np.nan,50,30,np.nan,56,np.nan],
    "Salary":[50000,np.nan,80000,60000,np.nan,90000,np.nan]}
df= pd.DataFrame(data)
print(df)

#detect missing values
print(df.isnull())
#or
print(df.isna())
#count total missing values
print(df.isnull().sum().sum())
#filling missing values with 0
filled_df= df.fillna(0)
print(filled_df)
#removing missing values
cleaned_df = df.dropna()
print(cleaned_df)
