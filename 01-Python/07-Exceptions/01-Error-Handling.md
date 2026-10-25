# Exceptions and Error Handling

Use try/except for expected runtime errors. Catch specific exceptions rather than hiding every error.

## Example
```python
try:
    number = int("123")
except ValueError:
    print("Input must be an integer.")
else:
    print(number * 2)
finally:
    print("Finished.")
```

## Practice
1. Safely convert user input to an integer.
2. Handle division by zero.
3. Explain the purpose of else and finally.
