# Iterators and Generators

An iterator produces values one at a time. A generator function uses `yield` to produce values lazily, which can reduce memory usage for large sequences.

## Example
```python
def countdown(start):
    while start > 0:
        yield start
        start -= 1
print(list(countdown(3)))
```

## Practice
1. Write a generator for even numbers.
2. Explain `iter()` and `next()`.
3. Describe when lazy evaluation helps.
