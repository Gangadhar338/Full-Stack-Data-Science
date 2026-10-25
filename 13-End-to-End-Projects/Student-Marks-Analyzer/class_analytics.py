
import csv

students = []

with open("students.csv", newline="", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file)

    for row in reader:
        marks = [
            int(row["subject1"]),
            int(row["subject2"]),
            int(row["subject3"])
        ]

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

        students.append({
            "name": row["name"],
            "total": total,
            "average": average,
            "grade": grade
        })

if not students:
    raise ValueError("No student records found in students.csv")

students.sort(key=lambda student: student["average"], reverse=True)

print("\nSTUDENT RANKING")
print("-" * 45)

for rank, student in enumerate(students, start=1):
    print(
        f"{rank}. {student['name']} | "
        f"Total: {student['total']} | "
        f"Average: {student['average']:.2f} | "
        f"Grade: {student['grade']}"
    )

class_average = sum(s["average"] for s in students) / len(students)
highest = max(students, key=lambda s: s["average"])
lowest = min(students, key=lambda s: s["average"])

print("\nCLASS ANALYTICS")
print("-" * 45)
print(f"Number of students: {len(students)}")
print(f"Class average: {class_average:.2f}")
print(f"Highest scorer: {highest['name']} ({highest['average']:.2f})")
print(f"Lowest scorer: {lowest['name']} ({lowest['average']:.2f})")

with open("report.csv", "w", newline="", encoding="utf-8") as file:
    fields = ["rank", "name", "total", "average", "grade"]
    writer = csv.DictWriter(file, fieldnames=fields)
    writer.writeheader()

    for rank, student in enumerate(students, start=1):
        writer.writerow({
            "rank": rank,
            "name": student["name"],
            "total": student["total"],
            "average": f"{student['average']:.2f}",
            "grade": student["grade"]
        })

print("\nReport saved to report.csv")
