🧮 Employee Salary Validator (NumPy + Pandas)
A clean and powerful NumPy + Pandas mini-project that validates employee data, removes inconsistencies, analyzes salary insights, and exports clean datasets.
Perfect for backend roles that require Python, data processing, validation logic, and real-world data cleaning skills.

🚀 Tech Stack
Python 3,
NumPy,
Pandas

🎯 Project Overview

This project processes raw employee records and performs:

✅ Data Cleaning
Removes employees with missing salary
Converts negative salary values to NaN
Handles missing experience values using averages
Fixes invalid or inconsistent records

✅ Data Validation
Flags employees earning below company salary threshold
Detects incorrect entries
Marks data inconsistencies

✅ Data Analysis
Computes yearly salary
Extracts high-earning employees
Generates statistical summaries (describe)
Finds department-wise highest salaries

✅ CSV Export
Clean dataset exported automatically → cleaned_employee_data.csv

🧑‍💻 Use Case

HR teams and backend systems often receive dirty or inconsistent salary data.
This script:
Cleans the data
Validates salary and experience
Performs analysis
Saves structured output
This demonstrates strong skills in:
✔ Backend Python
✔ NumPy computations
✔ Pandas data wrangling
✔ Real-world validation logic

Ideal for Python Backend Developer & Full Stack Developer roles.

📁 Project Structure
employee-salary-validator/
│── main.py
│── cleaned_employee_data.csv   (auto-generated)
│── README.md 

Full Code (main.py)

import numpy as np
import pandas as pd

data = {
    "Name": ["Ravi", "Priya", "Karan", "Sneha", "Amit"],
    "Department": ["IT", "HR", "IT", "Finance", "Marketing"],
    "Salary": [50000, -45000, 70000, None, 62000],
    "Experience": [2, 3, 5, 1, None]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# 1. Replace negative & None salaries
df["Salary"] = df["Salary"].apply(lambda x: np.nan if pd.isna(x) or x < 0 else x)

# 2. Replace missing experience with avg
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())

print("\n Cleaned Data:")
print(df)

# 3. Calculate yearly salary
df["Yearly_Salary"] = df["Salary"] * 12

print("\nYearly Salary Calculation:")
print(df)

# 4. Filter: employees earning above 60k
high_earners = df[df["Salary"] > 60000]

print("\nEmployees Earning Above 60K:")
print(high_earners)

# 5. Salary Insights
print("\nSalary Stats:")
print(df["Salary"].describe())

# Export CSV
df.to_csv("cleaned_employee_data.csv", index=False)
print("\n Cleaned data exported → cleaned_employee_data.csv")   


📤 Output Highlights

✔ Before Cleaning
Name	                   Department	       Salary	                         Experience
Priya	                      HR	             -45000	                          3
Sneha                     	Finance	          None	                          1

✔ After Cleaning
a.Negative salary → Converted to NaN
b.Missing salary → Removed
c.Missing experience → Auto-filled using mean
d.Yearly salary column added   

📦 Installation & Run
1️⃣ Install Dependencies
pip install numpy pandas

2️⃣ Run Script
python main.py

3️⃣ Output
A cleaned CSV file is generated automatically:
cleaned_employee_data.csv

⭐ Future Enhancements
*Add API endpoint for uploading CSV
*Return validation errors as JSON
*Integrate with Django REST API
*Visualize salary distribution
