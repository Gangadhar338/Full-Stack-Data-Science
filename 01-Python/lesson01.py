# Full-Stack Data Science
# Lesson 1: Python Fundamentals

student_name = "Student"
scores = [85, 92, 78, 90, 88]

total = sum(scores)
average = total / len(scores)

print("Student:", student_name)
print("Scores:", scores)
print("Total:", total)
print("Average:", round(average, 2))

if average >= 90:
    print("Result: Excellent")
elif average >= 75:
    print("Result: Good")
else:
    print("Result: Keep practising")
