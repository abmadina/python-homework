import pandas as pd
import numpy as np

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)


df = df.rename(columns=lambda x: x.lower().replace(" ", "_"))
print(df)


print(df.head(3))

mean_age = df['age'].mean()
print("Mean age:", mean_age)

print(df[['first_name', 'city']])

df['salary'] = np.random.randint(50000, 100000, size=len(df))
print(df)

print(df.describe())

import pandas as pd

data = {
    'Month': ['Jan', 'Feb', 'Mar', 'Apr'],
    'Sales': [5000, 6000, 7500, 8000],
    'Expenses': [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)
print(sales_and_expenses)


print("Max Sales:", sales_and_expenses['Sales'].max())
print("Max Expenses:", sales_and_expenses['Expenses'].max())

print("Min Sales:", sales_and_expenses['Sales'].min())
print("Min Expenses:", sales_and_expenses['Expenses'].min())

print("Average Sales:", sales_and_expenses['Sales'].mean())
print("Average Expenses:", sales_and_expenses['Expenses'].mean())

import pandas as pd

data = {
    'Category': ['Rent', 'Utilities', 'Groceries', 'Entertainment'],
    'January': [1200, 200, 300, 150],
    'February': [1300, 220, 320, 160],
    'March': [1400, 240, 330, 170],
    'April': [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

expenses = expenses.set_index('Category')
print(expenses)

print("Max expense per category:")
print(expenses.max(axis=1))

print("Min expense per category:")
print(expenses.min(axis=1))

print("Average expense per category:")
print(expenses.mean(axis=1))
