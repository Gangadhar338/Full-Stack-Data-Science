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
