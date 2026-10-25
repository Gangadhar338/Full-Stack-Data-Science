
from pathlib import Path

root = Path(__file__).parent
examples = root / "01-Python" / "01-Fundamentals" / "examples"

files = {
    "01_hello.py": '''"""Lesson 1: Your first Python program."""

print("Hello, Data Science!")
print("I am learning Python step by step.")
''',

    "02_variables.py": '''"""Lesson 2: Variables and data types."""

name = "Rahul"
age = 21
height = 1.75
enrolled = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Enrolled:", enrolled)

print("\\nData types:")
print(type(name))
print(type(age))
print(type(height))
print(type(enrolled))
''',

    "03_operators.py": '''"""Lesson 3: Arithmetic, comparison and logical operators."""

a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)

print("Greater than:", a > b)
print("Equal:", a == b)
print("Both conditions:", a > 5 and b < 5)
''',

    "04_strings.py": '''"""Lesson 4: Working with strings."""

language = "Python"
topic = "Data Science"

print("Language:", language)
print("First character:", language[0])
print("Last character:", language[-1])
print("First three characters:", language[:3])
print("Uppercase:", language.upper())
print("Lowercase:", language.lower())
print("Combined:", language + " for " + topic)
print(f"I am learning {language} for {topic}.")
''',

    "05_input_output.py": '''"""Lesson 5: Reading input and displaying output."""

name = input("Enter your name: ").strip()
age_text = input("Enter your age: ").strip()

if not name:
    print("Name cannot be empty.")
else:
    try:
        age = int(age_text)
        if age < 0:
            print("Age cannot be negative.")
        else:
            print(f"Hello, {name}!")
            print(f"Next year, you will be {age + 1}.")
    except ValueError:
        print("Please enter your age as a whole number.")
'''
}

examples.mkdir(parents=True, exist_ok=True)

for filename, content in files.items():
    path = examples / filename
    path.write_text(content, encoding="utf-8")
    print(f"Created: {path.relative_to(root)}")

print("\nAll five example files created.")
