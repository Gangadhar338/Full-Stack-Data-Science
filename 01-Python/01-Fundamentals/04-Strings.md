# Lesson 4: Strings

## Theory
A string is an immutable sequence of Unicode characters.
Strings can be created with single or double quotes.

## Indexing and slicing
```python
language = "Python"

print(language[0])    # P
print(language[-1])   # n
print(language[0:3])  # Pyt
print(language[2:])   # thon
print(language[::-1]) # nohtyP
```

The starting index is included; the ending index is excluded.
Invalid single-character indexing raises `IndexError`.

## Useful methods
```python
message = "  Learn Python  "

print(message.strip())
print(message.lower())
print(message.upper())
print(message.replace("Python", "Data Science"))
print("one,two,three".split(","))
print("-".join(["data", "science"]))
```

Methods such as `upper()` return new strings; they do not mutate
the original string.

## Formatting
```python
name = "Student"
hours = 2
print(f"{name} studies {hours} hours daily.")
```

F-strings are useful for readable output and reports.

## Searching and membership
```python
text = "data science"
print("science" in text)
print(text.find("data"))
print(len(text))
```

## Common mistakes
- Forgetting that indexing starts at zero.
- Expecting a string method to modify the original string.
- Accessing an index outside the string.
- Confusing `find()` returning -1 with an exception.

## Exercises
1. Store your full name and print its first and last characters.
2. Convert a sentence to uppercase and lowercase.
3. Remove leading and trailing spaces.
4. Count the characters in a sentence.
5. Split a comma-separated list into a list of words.

## Challenge
Create a text-cleaning function that strips whitespace, converts
text to lowercase, and collapses repeated internal spaces.
