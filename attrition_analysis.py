import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# 1. LOAD DATA
# ==========================

df = pd.read_csv("employee_attrition.csv")

print("=" * 50)
print("FIRST 5 ROWS")
print(df.head())

# ==========================
# 2. DATA OVERVIEW
# ==========================

print("\n" + "=" * 50)
print("DATASET INFO")
print(df.info())

print("\n" + "=" * 50)
print("MISSING VALUES")
print(df.isnull().sum())

print("\n" + "=" * 50)
print("TOTAL EMPLOYEES")
print(len(df))

# ==========================
# 3. ATTRITION RATE
# ==========================

print("\n" + "=" * 50)
print("ATTRITION COUNT")

attrition_count = df["Attrition"].value_counts()

print(attrition_count)

attrition_rate = (
    attrition_count["Yes"] /
    len(df)
) * 100

print("\nAttrition Rate:", round(attrition_rate, 2), "%")

# ==========================
# 4. ATTRITION BY DEPARTMENT
# ==========================

print("\n" + "=" * 50)
print("ATTRITION BY DEPARTMENT")

dept_attrition = (
    df[df["Attrition"] == "Yes"]
    .groupby("Department")
    .size()
)

print(dept_attrition)

# ==========================
# 5. ATTRITION BY AGE GROUP
# ==========================

bins = [20, 30, 40, 50, 60]

labels = [
    "20-30",
    "31-40",
    "41-50",
    "51-60"
]

df["AgeGroup"] = pd.cut(
    df["Age"],
    bins=bins,
    labels=labels
)

age_attrition = (
    df[df["Attrition"] == "Yes"]
    .groupby("AgeGroup")
    .size()
)

print("\n" + "=" * 50)
print("ATTRITION BY AGE GROUP")

print(age_attrition)

# ==========================
# 6. SALARY ANALYSIS
# ==========================

print("\n" + "=" * 50)
print("SALARY ANALYSIS")

left_salary = (
    df[df["Attrition"] == "Yes"]
    ["Salary"]
    .mean()
)

stay_salary = (
    df[df["Attrition"] == "No"]
    ["Salary"]
    .mean()
)

print("Average Salary (Left):", round(left_salary, 2))
print("Average Salary (Stayed):", round(stay_salary, 2))

# ==========================
# 7. JOB SATISFACTION ANALYSIS
# ==========================

print("\n" + "=" * 50)
print("JOB SATISFACTION ANALYSIS")

satisfaction = (
    df.groupby("Attrition")
    ["JobSatisfaction"]
    .mean()
)

print(satisfaction)

# ==========================
# 8. CHART 1
# DEPARTMENT ATTRITION
# ==========================

plt.figure(figsize=(8, 5))

dept_attrition.plot(
    kind="bar"
)

plt.title(
    "Attrition by Department"
)

plt.xlabel(
    "Department"
)

plt.ylabel(
    "Employees Left"
)

plt.tight_layout()

plt.show()

# ==========================
# 9. CHART 2
# ATTRITION DISTRIBUTION
# ==========================

plt.figure(figsize=(6, 6))

df["Attrition"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title(
    "Attrition Distribution"
)

plt.ylabel("")

plt.show()

# ==========================
# 10. CHART 3
# AGE GROUP ATTRITION
# ==========================

plt.figure(figsize=(8, 5))

age_attrition.plot(
    kind="bar"
)

plt.title(
    "Attrition by Age Group"
)

plt.xlabel(
    "Age Group"
)

plt.ylabel(
    "Employees Left"
)

plt.tight_layout()

plt.show()

# ==========================
# 11. BUSINESS INSIGHTS
# ==========================

print("\n" + "=" * 50)
print("BUSINESS INSIGHTS")

top_department = dept_attrition.idxmax()
top_age_group = age_attrition.idxmax()

print(
    f"1. Attrition Rate is {round(attrition_rate,2)}%"
)

print(
    f"2. Highest attrition occurs in {top_department} department."
)

print(
    f"3. Highest attrition occurs in age group {top_age_group}."
)

print(
    f"4. Average salary of employees who left: {round(left_salary,2)}"
)

print(
    f"5. Average salary of employees who stayed: {round(stay_salary,2)}"
)

print(
    "6. Compare job satisfaction scores to determine if low satisfaction contributes to attrition."
)

print("=" * 50)
print("PROJECT COMPLETED")