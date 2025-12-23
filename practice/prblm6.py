class Animal:
    def speak(self):
        print('Animal does not speak')

class Dog(Animal):
    def speak(self):
        super().speak()
        return f'Woof'
    
obj = Dog()
print(obj.speak())