import pandas as pd

emp_data = {
    "employees": ["Rahul", "Siya", "Sneha", "Harsh"],
    "dept": ["AI", "HR", "AI", "Finance"],
    "salary": [45000, 88000, 78000, 120000],
    "experience": [4, 14, 5, 25]
}
df = pd.DataFrame(emp_data)
print(df)

# finding employee in the AI department
ai_emp = df[df["dept"] == "AI"]
print(ai_emp)

# finding employee whose salary is more than 80000
high_sal = df[df["salary"] > 80000]
print(high_sal)
