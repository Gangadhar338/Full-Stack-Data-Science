class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def passed(self):
        return self.score >= 40
student = Student("Asha", 75)
print(student.name, student.passed())
