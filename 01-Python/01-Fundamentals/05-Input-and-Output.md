# Lesson 5: Input and Output

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
