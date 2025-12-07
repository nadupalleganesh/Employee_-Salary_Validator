import pandas as pd
import numpy as np

# ----------------------------------------
# STEP 1: Load Employee CSV
# ----------------------------------------

# Sample dataset (You can replace with uploaded CSV)
data = {
    "id": [1, 2, 3, 4, 5, 5],
    "name": ["Ganesh", "Rahul", None, "Teja", "Kiran", "Kiran"],
    "age": [25, None, 30, 22, 28, 28],
    "department": ["IT", "HR", "Finance", "IT", "HR", "HR"],
    "salary": ["50000", "45000", "60000", None, "40000", "40000"],
    "bonus": [5000, 4000, None, 3000, 3500, 3500],
    "city": ["Hyderabad", "Chennai", "NCR", None, "Chennai", "Chennai"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)
print("\n")


# ----------------------------------------
# STEP 2: Data Cleaning
# ----------------------------------------

# Remove duplicates
df = df.drop_duplicates()

# Handle missing names → fill with "Unknown"
df["name"] = df["name"].fillna("Unknown")

# Handle missing age → fill with mean age
df["age"] = df["age"].fillna(df["age"].mean())

# Replace None in city
df["city"] = df["city"].fillna("Unknown")

# Convert salary to numeric
df["salary"] = pd.to_numeric(df["salary"], errors="coerce")

# Convert bonus to numeric
df["bonus"] = pd.to_numeric(df["bonus"], errors="coerce")

# Handle missing salary & bonus
df["salary"] = df["salary"].fillna(0)
df["bonus"] = df["bonus"].fillna(0)

print("Cleaned Data:")
print(df)
print("\n")


# ----------------------------------------
# STEP 3: Business Logic (NumPy Operations)
# ----------------------------------------

# Total salary = salary + bonus (vectorized operation)
df["total_salary"] = df["salary"] + df["bonus"]

# Tax 10%
df["tax"] = df["salary"] * 0.10

# Net salary
df["net_salary"] = df["total_salary"] - df["tax"]

print("Data After Salary Computation:")
print(df)
print("\n")


# ----------------------------------------
# STEP 4: Filtering (Backend API Style)
# ----------------------------------------

high_salary = df[df["salary"] > 45000]
print("Employees with Salary > 45000:")
print(high_salary)
print("\n")

from_hyd = df[df["city"] == "Hyderabad"]
print("Employees from Hyderabad:")
print(from_hyd)
print("\n")

age_above_25 = df[df["age"] > 25]
print("Employees Age > 25:")
print(age_above_25)
print("\n")


# ----------------------------------------
# STEP 5: Insights (Analytics)
# ----------------------------------------

# Average salary per department
avg_salary = df.groupby("department")["salary"].mean()
print("Avg Salary per Department:")
print(avg_salary)
print("\n")

# Highest paid employee
highest = df.sort_values("net_salary", ascending=False).head(1)
print("Highest Paid Employee:")
print(highest)
print("\n")

# City-wise employee count
city_count = df["city"].value_counts()
print("Employees per City:")
print(city_count)
print("\n")


# ----------------------------------------
# STEP 6: Export cleaned CSV
# ----------------------------------------

df.to_csv("cleaned_employee_data.csv", index=False)
print("File saved: cleaned_employee_data.csv")

    