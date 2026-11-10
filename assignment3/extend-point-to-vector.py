#Task 5
from math import sqrt
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"p {self.x} {self.y}"
    def __eq__(self,other):
        return self.y == other.y and self.x == other.x
    def euclidean(self,other):
        return sqrt((self.x -other.x)**2 + (self.y - other.y)**2)
class Vector(Point):
    def __str__(self):
        return f"v {self.x} {self.y}"
    def __add__(self,other):
        return Vector((self.x + other.x),(self.y + other.y))
v1 = Vector(3, 4)
v2 = Vector(7, 8)
p1 = Point(5, 6)
p2 = Point(5, 6)
p3 = Point(8, 4)
v3 = v1 + v2
print(p1)
print(p2)
print(v1)
print(v2)
print(v3)
print(p1 == p2)
print(p1 == p3)
print(p1.euclidean(p3))
print(v1.euclidean(v3))
print(v1 == v2)
print(type(v1))
