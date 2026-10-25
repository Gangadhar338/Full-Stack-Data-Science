
from pathlib import Path

root = Path(__file__).parent
folder = root / "01-Python" / "01-Fundamentals"
folder.mkdir(parents=True, exist_ok=True)

lessons = {
    "01-What-Is-Python.md": r'''# Lesson 1: What Is Python?

## Learning objectives
- Explain Python and its applications.
- Run a Python script.
- Understand syntax errors and program output.

## Theory
Python is a general-purpose programming language used in automation,
web development, data analysis, machine learning, and AI.

Python executes statements in order, unless control-flow constructs
change that order. Indentation is significant in Python blocks.

## First program
```python
print("Hello, Data Science!")
print(10 + 20)
```

Expected output:
```text
Hello, Data Science!
30
```

## How it works
- `print()` displays a representation of a value.
- Quoted text is a string.
- `10 + 20` is an arithmetic expression.
- Python evaluates the expression before printing its result.

## Common mistakes
- Missing a closing quotation mark.
- Misspelling a function name.
- Saving the file with the wrong extension.
- Running the command from the wrong folder.

## Exercises
1. Print your name.
2. Print your learning goal.
3. Calculate 125 + 375.
4. Print the results of 50 * 8 and 100 / 4.
5. Explain the difference between text and numeric values.

## Challenge
Print a three-line report containing your course, weekly study hours,
and learning goal.

## Review questions
1. What is Python used for?
2. What does `print()` do?
3. What is a syntax error?
4. Why does `10 + 20` produce a number rather than text?
''',

    "02-Variables-and-Data-Types.md": r'''# Lesson 2: Variables and Data Types

## Learning objectives
Understand assignment, names, values, built-in types, and conversion.

## Theory
A variable name refers to an object. The assignment operator `=`
binds a name to a value. Python is dynamically typed: a name can later
refer to a value of another type.

Common built-in types:
- `int`: integers such as 20
- `float`: floating-point numbers such as 1.75
- `str`: text such as "Python"
- `bool`: `True` or `False`
- `NoneType`: the type of `None`

## Example
```python
name = "Student"
age = 20
height = 1.75
enrolled = True

print(name, age, height, enrolled)
print(type(age))
print(type(name))
```

## Conversion
```python
number_text = "123"
number = int(number_text)
print(number + 1)  # 124

price = float("19.50")
print(price)
```

Conversion can fail when text does not represent a valid number:
`int("hello")` raises `ValueError`.

## Naming rules
- Names can contain letters, digits, and underscores.
- Names cannot begin with a digit.
- Python keywords cannot be used as names.
- Prefer descriptive names such as `total_score`.

## Common mistakes
- Treating `"20"` as the number `20`.
- Using a variable before assigning it.
- Assuming `input()` returns a number; it returns text.
- Using `==` when assignment with `=` is intended, or vice versa.

## Exercises
1. Create variables for a name, age, and course.
2. Print each variable's type.
3. Convert `"123"` to an integer and add 7.
4. Explain the difference between `int`, `float`, `str`, and `bool`.
5. Predict the result of `type(3.0)` and `type("3")`.

## Challenge
Ask for an age as text, convert it to an integer, and display the age
the user will be next year. Handle invalid input.
''',

    "03-Operators.md": r'''# Lesson 3: Python Operators

## Arithmetic operators
```python
a = 20
b = 6

print(a + b)   # 26: addition
print(a - b)   # 14: subtraction
print(a * b)   # 120: multiplication
print(a / b)   # 3.333...: true division
print(a // b)  # 3: floor division
print(a % b)   # 2: remainder
print(a ** 2)  # 400: exponentiation
```

## Comparison operators
Comparisons return Boolean values:
```python
print(5 == 5)  # True
print(5 != 4)  # True
print(5 > 4)   # True
print(5 < 4)   # False
print(5 >= 5)  # True
print(4 <= 5)  # True
```

`=` assigns a value; `==` compares values.

## Logical operators
```python
age = 22
has_id = True

print(age >= 18 and has_id)
print(age < 18 or has_id)
print(not has_id)
```

`and` requires both conditions to be true. `or` requires at least
one condition to be true. `not` reverses a Boolean value.

## Assignment operators
```python
count = 10
count += 2
count *= 3
print(count)  # 36
```

## Operator precedence
Parentheses make expressions clearer:
```python
result = (2 + 3) * 4
print(result)  # 20
```

## Common mistakes
- Confusing `/` and `//`.
- Dividing by zero.
- Comparing text and numbers without conversion.
- Forgetting operator precedence.

## Exercises
1. Calculate the area of a rectangle.
2. Check whether a number is greater than 100.
3. Determine whether a number is even using `%`.
4. Compare two numbers and print the larger one.
5. Explain the difference between `**` and `^`. In Python, `**`
   means exponentiation; `^` means bitwise XOR.

## Challenge
Build a simple calculator supporting addition, subtraction,
multiplication, and division. Handle division by zero.
''',

    "04-Strings.md": r'''# Lesson 4: Strings

## Theory
A string is an immutable sequence of Unicode characters.
Strings can be created with single or double quotes.

## Indexing and slicing
```python
language = "Python"

print(language[0])    # P
print(language[-1])   # n
print(language[0:3])  # Pyt
print(language[2:])   # thon
print(language[::-1]) # nohtyP
```

The starting index is included; the ending index is excluded.
Invalid single-character indexing raises `IndexError`.

## Useful methods
```python
message = "  Learn Python  "

print(message.strip())
print(message.lower())
print(message.upper())
print(message.replace("Python", "Data Science"))
print("one,two,three".split(","))
print("-".join(["data", "science"]))
```

Methods such as `upper()` return new strings; they do not mutate
the original string.

## Formatting
```python
name = "Student"
hours = 2
print(f"{name} studies {hours} hours daily.")
```

F-strings are useful for readable output and reports.

## Searching and membership
```python
text = "data science"
print("science" in text)
print(text.find("data"))
print(len(text))
```

## Common mistakes
- Forgetting that indexing starts at zero.
- Expecting a string method to modify the original string.
- Accessing an index outside the string.
- Confusing `find()` returning -1 with an exception.

## Exercises
1. Store your full name and print its first and last characters.
2. Convert a sentence to uppercase and lowercase.
3. Remove leading and trailing spaces.
4. Count the characters in a sentence.
5. Split a comma-separated list into a list of words.

## Challenge
Create a text-cleaning function that strips whitespace, converts
text to lowercase, and collapses repeated internal spaces.
''',

    "05-Input-and-Output.md": r'''# Lesson 5: Input and Output

## Theory
`input()` displays a prompt and returns the entered text as a string.
`print()` displays values. Convert input before performing arithmetic.

## Example
```python
name = input("Enter your name: ")
age_text = input("Enter your age: ")

try:
    age = int(age_text)
except ValueError:
    print("Please enter a whole-number age.")
else:
    print(f"Hello {name}, next year you will be {age + 1}.")
```

## Reading numeric values
```python
try:
    first = float(input("First number: "))
    second = float(input("Second number: "))
except ValueError:
    print("Enter valid numbers.")
else:
    print("Sum:", first + second)
```

## Output formatting
```python
average = 87.456
print(f"Average: {average:.2f}")
```

The format specifier `.2f` displays two digits after the decimal point.

## Common mistakes
- Adding two input strings instead of numbers.
- Converting invalid text without catching `ValueError`.
- Forgetting that empty input is possible.
- Assuming all numeric input should be an integer.

## Exercises
1. Ask for two numbers and add them.
2. Ask for a student's name and marks.
3. Calculate the average of three numbers.
4. Handle invalid numeric input.
5. Display a price to two decimal places.

## Challenge
Create a command-line student report that collects a name and three
marks, validates the marks, calculates the average, and prints a
formatted report.
'''
}

for filename, content in lessons.items():
    path = folder / filename
    path.write_text(content.strip() + "\n", encoding="utf-8")
    print("Wrote:", path.relative_to(root))

print("\nRepair complete. Five lesson files were rewritten.")
