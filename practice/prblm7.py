class Calculator:
    def add(self):
        val1, val2 = self.getval()
        return val1+val2
    def sub(self):
        val1 , val2 = self.getval()
        return val1-val2
    def mul(self):
        val1, val2 = self.getval()
        return val1*val2
    def div(self):
        val1, val2 = self.getval()
        return val1/val2
    @staticmethod
    def getval():
        val1 = int(input("enter the first value: "))
        val2 = int(input("Enter the second value: "))
        return val1, val2
calc = Calculator()
print(calc.add())
print(calc.sub())
print(calc.mul())
print(calc.div())