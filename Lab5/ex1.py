import math


class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        p = (self.side1 + self.side2 + self.side3) / 2
        return math.sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))

    def perimeter(self):
        return self.side1 + self.side2 + self.side3


# Example usage:
c = Circle(5)
print("Aria cercului:", c.area())
print("Perimetrul cercului:", c.perimeter())

r = Rectangle(4, 6)
print("Aria derptunghiului:", r.area())
print("Perimetrul derptunghiului:", r.perimeter())

t = Triangle(3, 4, 5)
print("Aria triunghiului:", t.area())
print("Perimetrul triunghiului:", t.perimeter())
