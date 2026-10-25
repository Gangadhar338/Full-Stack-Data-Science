# Decorators

A decorator wraps a function to add behavior without changing its core implementation. The `@decorator` syntax applies a decorator.

## Example
```python
def announce(fn):
    def wrapper():
        print("Starting")
        result = fn()
        print("Finished")
        return result
    return wrapper
@announce
def greet():
    print("Hello")
greet()
```

## Practice
1. Create a decorator that measures elapsed time.
2. Explain why `functools.wraps` is useful.
3. Make a decorator that logs a function call.
