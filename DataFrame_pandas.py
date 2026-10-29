import pandas as pd

data = {"name": ["Riya", "Rishabh", "Priya", "Aman"], "marks": [90, 89, 76, 100]}
df1 = pd.DataFrame(data)
print(df1)

data2 = {"name": ["Rahul", "Siya", "Aditya"], "maths": [40, 55, 21], "science": [90, 86, 43], "english": [56, 41, 62]}
df2 = pd.DataFrame(data2)
print(df2)
