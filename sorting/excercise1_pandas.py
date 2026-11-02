import pandas as pd

data = {
    "products": ["laptop", "mobile", "laptop", "headphones", "mobile", "USB-port"],
    "price": [55000, 20000, 55000, 2500, 20000, 550],
    "quantity": [20, 28, 20, 50, 28, 100]
}
df = pd.DataFrame(data)
print(df)

# check duplicates
print(df.duplicated())

# drop duplicate rows
df = df.drop_duplicates()
print(df)

# rename columns
df = df.rename(columns={"products": "Items", "price": "Price_INR"})
print(df)

# drop column
print(df.drop(columns=["quantity"]))
