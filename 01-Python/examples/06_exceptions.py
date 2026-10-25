try:
    value = int("123")
except ValueError:
    print("Invalid integer")
else:
    print(value * 2)
finally:
    print("Finished")
