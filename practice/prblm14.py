class Student:
    def __init__(self, detail):
        values = Student.breakStudentDetail(detail)
        self.name = values[0]
        self.age = values[1]
        self.branch = values[2]
    def student_details(self):
        return f'{self.name} is {self.age} years old and the branch he is in is {self.branch}'
    @classmethod
    def breakStudentDetail(cls, details):
        dts = details.split('-')
        return dts

s1 = Student('Ashlesh-22-ISE')
print(s1.student_details())