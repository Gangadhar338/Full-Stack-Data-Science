# Lesson 2: Variables and Data Types

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
