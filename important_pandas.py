import pandas as pd

df1 = {"name": ["Riya", "Rishabh", "Priya", "Aman"],"maths":[20,89,65,44],
"science":[90,38,99,26],"english":[86,89,99,56]}
df1=pd.DataFrame(df1)
print(df1)
print()
print(df1.head())
print()
print(df1.tail())
print(df1.shape)

#printing columns
print(df1["name"]) #selecting one column
#printing rows
print(df1.loc[0]) 


print(df1.loc[0:2]) #includes end index
print()
print(df1.iloc[1]) #selects rows using index position
print(df1.iloc[1:3]) #doesn't selects end index 