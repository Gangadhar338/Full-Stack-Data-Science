# Type Hints

Type hints document expected types and help editors and static-analysis tools detect mistakes. Python generally does not enforce annotations at runtime.

## Example
```python
def average(values: list[float]) -> float:
    if not values:
        raise ValueError("values cannot be empty")
    return sum(values) / len(values)
print(average([2.0, 4.0, 6.0]))
```

## Practice
1. Add annotations to a function that joins two strings.
2. Annotate a function that returns a list of integers.
3. Explain the difference between a type hint and runtime validation.
