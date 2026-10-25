# Lesson 3: Python Operators

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
