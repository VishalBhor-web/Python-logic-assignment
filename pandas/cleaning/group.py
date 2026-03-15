# 🔹 Sample Data (5–10 Rows)

import pandas as pd
import numpy as np

# Creating sample dataset
data = {
    "Employee": [
        "Amit", "Neha", "Rahul", "Sneha",
        "Vikram", "Priya", "Arjun", "Divya"
    ],
    "Department": [
        "IT", "HR", "IT", "Finance",
        "HR", "Finance", "IT", "HR"
    ],
    "Salary": [
        600000, 500000, np.nan, 700000,
        520000, np.nan, 650000, 480000
    ],
    "Temporary_Notes": [
        "On probation", "Contract",
        "Pending docs", "Verified",
        "Intern", "New joiner",
        "On leave", "Temporary role"
    ]
}

df = pd.DataFrame(data)

print(df)

# 2. Detect and print missing values
print("Missing Values Detection:")
print(df.isnull().sum())
print("-" * 30)

# 3. Fill missing Salary values using the column mean
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

# 4. Drop the Temporary_Notes column
df = df.drop(columns=["Temporary_Notes"])

# 5. Rename Salary to Annual_Salary
df = df.rename(columns={"Salary": "Annual_Salary"})

# 6. Group by Department and compute Mean and Count
summary_table = df.groupby("Department").agg(
    Mean_Salary=("Annual_Salary", "mean"),
    Employee_Count=("Employee", "count")
)

print("Final Summary Table:")
print(summary_table)
