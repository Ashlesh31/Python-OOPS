class Student():
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
    def average(self):
        avg = 0
        for val in self.marks:
            avg += val
        return avg/len(self.marks)
    def details(self):
        return f'my name is {self.name}, i am {self.age} years old having the average marks as {self.average()}'
check = Student('Vinod', 23, [89,91,78,67])
print(check.average())
print(check.details())