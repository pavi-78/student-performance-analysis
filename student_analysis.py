
import pandas as pd

data = {
    "Student": ["Anu", "Rahul", "Priya", "Kiran", "Sneha"],
    "Maths": [85, 67, 92, 45, 78],
    "Science": [88, 72, 95, 50, 81],
    "English": [90, 75, 89, 55, 84],
    "Attendance": [95, 80, 98, 65, 88]
}

df = pd.DataFrame(data)

print("STUDENT PERFORMANCE ANALYSIS")
print(df)

df["Average"] = df[["Maths", "Science", "English"]].mean(axis=1)

print("\nSTUDENT AVERAGE MARKS")
print(df[["Student", "Average"]].round(2))
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


df["Grade"] = df["Average"].apply(calculate_grade)

print("\nSTUDENT PERFORMANCE REPORT")
print(df[["Student", "Average", "Grade", "Attendance"]].round(2))
df["Status"] = df.apply(
    lambda row: "Needs Support"
    if row["Average"] < 60 or row["Attendance"] < 75
    else "Good",
    axis=1
)

print("\nSTUDENT SUPPORT REPORT")
print(df[["Student", "Average", "Attendance", "Status"]])


import matplotlib.pyplot as plt

plt.figure(figsize=(8, 5))

bars = plt.bar(df["Student"], df["Average"])

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height + 1,
        f"{height:.2f}",
        ha="center"
    )


plt.title("Student Average Marks")
plt.xlabel("Student")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.tight_layout()

plt.show()

  

