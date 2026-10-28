import numpy as np

np.random.seed(10)

subjects = np.array(["Math", "Science", "English", "Computer"])
students = np.array(["Riya", "Aman", "Priya", "Karan", "Neha"])

marks = np.array([
    [85, 78, 92, 88],
    [65, np.nan, 70, 75],
    [90, 95, 88, 94],
    [55, 60, 65, np.nan],
    [72, 80, 78, 85]
])
print("Missing values:")
print(np.isnan(marks))

print("Total missing values:", np.isnan(marks).sum())
subject_average = np.nanmean(marks, axis=0)

print("Subject averages:", subject_average)

cleaned_marks = np.where(np.isnan(marks), subject_average, marks)
student_total = np.sum(cleaned_marks, axis=1)
student_average = np.mean(cleaned_marks, axis=1)

print("Student totals:", student_total)
print("Student averages:", student_average)
top_student_index = np.argmax(student_total)

print("Top student:", students[top_student_index])
print("Top student total:", student_total[top_student_index])