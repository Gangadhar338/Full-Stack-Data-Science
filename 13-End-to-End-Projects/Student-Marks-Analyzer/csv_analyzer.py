
import csv

def analyze_marks(name, marks):
    total = sum(marks)
    average = total / len(marks)

    if average >= 90:
        grade = "A"
    elif average >= 75:
        grade = "B"
    elif average >= 60:
        grade = "C"
    else:
        grade = "D"

    print(f"{name}: Total={total}, Average={average:.2f}, Grade={grade}")

with open("students.csv", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks = [
            int(row["subject1"]),
            int(row["subject2"]),
            int(row["subject3"])
        ]
        analyze_marks(row["name"], marks)
