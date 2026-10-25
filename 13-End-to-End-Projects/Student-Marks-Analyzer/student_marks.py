
students = {
    "Ravi": [85, 90, 78],
    "Priya": [92, 88, 95],
    "Arjun": [70, 75, 80],
    "Sneha": [60, 68, 72]
}

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

    print(f"\nStudent: {name}")
    print(f"Marks: {marks}")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}")

for name, marks in students.items():
    analyze_marks(name, marks)
