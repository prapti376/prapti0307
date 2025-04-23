import math

class Shape:
    def __init__(self, shape_type, dimensions):
        self.shape_type = shape_type
        self.dimensions = dimensions

    def area(self):
        if self.shape_type == "circle":
            r = self.dimensions['radius']
            return math.pi * r ** 2
        elif self.shape_type == "square":
            a = self.dimensions['side']
            return a ** 2
        elif self.shape_type == "triangle":
            b = self.dimensions['base']
            h = self.dimensions['height']
            return 0.5 * b * h

    def perimeter(self):
        if self.shape_type == "circle":
            r = self.dimensions['radius']
            return 2 * math.pi * r
        elif self.shape_type == "square":
            a = self.dimensions['side']
            return 4 * a
        elif self.shape_type == "triangle":
            return sum(self.dimensions['sides'])

shape = Shape("square", {"side": 5})
print("Area:", shape.area())
print("Perimeter:", shape.perimeter())