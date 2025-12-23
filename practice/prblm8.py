class Employee:
    def __init__(self, name, id, base_salary):
        self.name = name
        self.id = id
        self.base_salary = base_salary
    def getdetails(self):
        return f'{self.id}. The name of employee us {self.name} having a salary of {self.base_salary}'
    def total_salary(self):
        return self.base_salary
class Manager(Employee):
    def __init__(self, name, id, base_salary, bonus):
        super().__init__(name, id, base_salary)
        self.base_salary += bonus
    def getdetails(self):
        return super().getdetails()
    def total_salary(self):
        return self.base_salary

man = Manager('suresh', 12, 45000, 7000)
print(man.getdetails())
print(man.total_salary())
emp = Employee('ramesh', 11, 30000)
print(emp.getdetails())
print(emp.total_salary())