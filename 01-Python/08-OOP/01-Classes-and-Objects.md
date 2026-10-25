# Object-Oriented Programming

Classes define object structure and behavior. Objects are instances of classes. `__init__` initializes instance state, and `self` refers to the current instance.

## Example
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def passed(self):
        return self.score >= 40

student = Student("Asha", 75)
print(student.name, student.passed())
```

## Practice
1. Create a `Rectangle` class with area and perimeter methods.
2. Create a `BankAccount` class with deposit and withdraw methods.
3. Explain inheritance and composition.
