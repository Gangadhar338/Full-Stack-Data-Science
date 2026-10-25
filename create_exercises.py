
from pathlib import Path

root = Path(__file__).parent
base = root / "01-Python" / "01-Fundamentals"
exercise_dir = base / "exercises"
solution_dir = base / "solutions"

exercise_dir.mkdir(parents=True, exist_ok=True)
solution_dir.mkdir(parents=True, exist_ok=True)

exercises = {
    "01-variables.md": (
        "# Exercise 1: Variables\n\n"
        "1. Create variables for your name, age, city, height, and whether you are learning Python.\n"
        "2. Print each variable and its type using type().\n"
        "3. Print your age five years from now.\n"
        "4. Explain the difference between int, float, str, and bool.\n"
    ),
    "02-operators.md": (
        "# Exercise 2: Operators\n\n"
        "Use a = 17 and b = 5.\n\n"
        "1. Calculate sum, difference, and product.\n"
        "2. Print a / b and a // b.\n"
        "3. Find the remainder using %.\n"
        "4. Calculate a ** b.\n"
        "5. Check whether a is greater than b.\n"
        "6. Explain the difference between / and //.\n"
    ),
    "03-strings.md": (
        "# Exercise 3: Strings\n\n"
        'Use text = "Data Science".\n\n'
        "1. Print the text in uppercase and lowercase.\n"
        "2. Print its first and last characters.\n"
        "3. Print the first four characters.\n"
        "4. Find its length using len().\n"
        '5. Check whether "Science" appears in the text.\n'
        "6. Display a sentence using an f-string.\n"
    ),
    "04-input-validation.md": (
        "# Exercise 4: Input Validation\n\n"
        "Write a program that asks for a name and age.\n\n"
        "1. Remove extra spaces from the name.\n"
        "2. Reject an empty name.\n"
        "3. Convert age input to an integer.\n"
        "4. Handle non-numeric input with try/except.\n"
        "5. Reject negative ages.\n"
        "6. Display the age next year for valid input.\n"
    ),
}

solutions = {
    "01-variables.py": (
        'name = "Student"\n'
        "age = 21\n"
        'city = "Vijayawada"\n'
        "height = 1.75\n"
        "learning_python = True\n\n"
        "print(name, type(name))\n"
        "print(age, type(age))\n"
        "print(city, type(city))\n"
        "print(height, type(height))\n"
        "print(learning_python, type(learning_python))\n"
        "print('Age in five years:', age + 5)\n"
    ),
    "02-operators.py": (
        "a = 17\n"
        "b = 5\n\n"
        "print('Sum:', a + b)\n"
        "print('Difference:', a - b)\n"
        "print('Product:', a * b)\n"
        "print('Division:', a / b)\n"
        "print('Floor division:', a // b)\n"
        "print('Remainder:', a % b)\n"
        "print('Power:', a ** b)\n"
        "print('a greater than b:', a > b)\n"
    ),
    "03-strings.py": (
        'text = "Data Science"\n\n'
        "print(text.upper())\n"
        "print(text.lower())\n"
        "print(text[0])\n"
        "print(text[-1])\n"
        "print(text[:4])\n"
        "print(len(text))\n"
        "print('Science' in text)\n"
        "print(f'I am learning {text}')\n"
    ),
    "04-input-validation.py": (
        'name = input("Enter your name: ").strip()\n\n'
        "if not name:\n"
        "    print('Name cannot be empty.')\n"
        "else:\n"
        '    age_text = input("Enter your age: ").strip()\n'
        "    try:\n"
        "        age = int(age_text)\n"
        "        if age < 0:\n"
        "            print('Age cannot be negative.')\n"
        "        else:\n"
        "            print(f'Hello, {name}!')\n"
        "            print(f'Next year, you will be {age + 1}.')\n"
        "    except ValueError:\n"
        "        print('Please enter a whole number for age.')\n"
    ),
}

for filename, content in exercises.items():
    (exercise_dir / filename).write_text(content, encoding="utf-8")
    print("Created exercise:", filename)

for filename, content in solutions.items():
    (solution_dir / filename).write_text(content, encoding="utf-8")
    print("Created solution:", filename)

print("\nAll exercises and solutions created successfully.")
