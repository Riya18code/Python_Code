import pandas as pd

data = {
    "Employee": ["Naman", "Alice", "Priya", "Zoya", "Rohit", "Sam", "Aman", "Akash"],
    "Department": ["IT", "HR", "Finance", "IT", "Finance", "HR", "AI", "AI"],
    "Sales": [50000, 60000, 70000, 56000, 28000, 450000, 60000, 100000],
    "City": ["Delhi", "Mumbai", "Delhi", "Kolkata", "Kasoli", "Delhi", "Mumbai", "Varansi"]
}
df = pd.DataFrame(data)
print(df)

# Group by Department → calculate total sales for each department
department_sales = df.groupby("Department")["Sales"].sum()
print(department_sales)

# average sales
average_sales = df.groupby("Department")["Sales"].mean()
print(average_sales)

print(df.groupby("Department")["Sales"].max())
print(df.groupby("Department")["Sales"].min())
print(df.groupby("Department")["Employee"].count())
print(df.groupby("Department")["Employee"].nunique())

# group by multiple columns
city_department_sales = df.groupby(["City", "Department"])["Sales"].sum()
print(city_department_sales)
