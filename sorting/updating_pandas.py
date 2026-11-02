import pandas as pd

data = {
    "employee": ["Aman", "Riya", "Rishabh", "Priya", "Gunjan"],
    "department": ["FINANCE", "AI", "AI", "HR", "HR"],
    "salary": [1200000, 45000000, 600000000, 850000, 7600000],
    "experience": [8, 10, 14, 5, 9]
}
df = pd.DataFrame(data)
print(df)

# sort the employee salary in ascending order
sortA = df.sort_values(by="salary")
print(sortA)

# sort the employee salary in descending order
sortD = df.sort_values(by="salary", ascending=False)
print(sortD)

# updating values
# syntax: df.loc[row_label, column_name] = value

df.loc[4, "salary"] = 40000
print(df)
df.loc[3, "salary"] = 900000
print(df)
