class Shape:
    def area(self):
        return 0
    def perimeter(self):
        return 0
class Circle(Shape):
    def area(self,rad):
        return 3.14 * rad**2
    def perimeter(self,rad):
        return 2 * 3.14 * rad
class Traingle(Shape):
    def area(self, base, height):
        return (base * height)/2
    def perimeter(self,a,b,c):
        return a+b+c
class Square(Shape):
    def area(self,a):
        return a**2
    def perimeter(self, a):
        return 4 * a
c = Circle()
print(c.area(4))
print(c.perimeter(4))
t = Traingle()
print(t.area(4,5))
print(t.perimeter(4,5,6))
s = Square()
print(s.area(5))
print(s.perimeter(5))