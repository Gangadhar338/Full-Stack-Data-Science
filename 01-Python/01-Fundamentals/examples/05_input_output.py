"""Lesson 5: Reading input and displaying output."""

name = input("Enter your name: ").strip()
age_text = input("Enter your age: ").strip()

if not name:
    print("Name cannot be empty.")
else:
    try:
        age = int(age_text)
        if age < 0:
            print("Age cannot be negative.")
        else:
            print(f"Hello, {name}!")
            print(f"Next year, you will be {age + 1}.")
    except ValueError:
        print("Please enter your age as a whole number.")
