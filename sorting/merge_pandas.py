import pandas as pd

# merging two dataframes

data1 = {
    "employee_id": [101, 409, 781, 461],
    "employee_name": ["Alice", "Bob", "Charlie", "David"]
}
df1 = pd.DataFrame(data1)
print(df1)

data2 = {
    "employee_id": [103, 302, 222],
    "employee_name": ["Alan", "Carol", "Eve"]
}
df2 = pd.DataFrame(data2)
print(df2)

merged_df = pd.merge(df1, df2, on="employee_id")
print(merged_df)
