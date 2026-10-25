# Comprehensions

Comprehensions create collections from iterables using concise expressions. Add conditions when filtering.

## Example
```python
squares = [n*n for n in range(1, 6)]
evens = {n for n in range(10) if n % 2 == 0}
lookup = {n: n*n for n in range(1, 4)}
print(squares, sorted(evens), lookup)
```

## Practice
1. Create cubes from 1 to 10.
2. Filter words longer than five characters.
3. Build a dictionary mapping names to their lengths.
