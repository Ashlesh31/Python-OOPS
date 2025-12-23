class Person():
    def __init__(self,name, id, salary):
        self.name = name
        self.id = id
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    def set_salary(self, val):
        self.__salary = val
    def __str__(self):
        return f'{self.name} with id {self.id}.'
pr = Person('ganesh', 1, 23000)
print(pr)
print(pr.get_salary())
pr.set_salary(30000)
print(pr.get_salary())