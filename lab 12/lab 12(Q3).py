import math

class Solid:
    def __init__(self, shape, dimensions):
        self.shape = shape
        self.dimensions = dimensions

    def surface_area(self):
        if self.shape == "sphere":
            r = self.dimensions['radius']
            return 4 * math.pi * r ** 2
        elif self.shape == "cube":
            a = self.dimensions['side']
            return 6 * a ** 2
        elif self.shape == "cylinder":
            r = self.dimensions['radius']
            h = self.dimensions['height']
            return 2 * math.pi * r * (r + h)

    def volume(self):
        if self.shape == "sphere":
            r = self.dimensions['radius']
            return (4/3) * math.pi * r ** 3
        elif self.shape == "cube":
            a = self.dimensions['side']
            return a ** 3
        elif self.shape == "cylinder":
            r = self.dimensions['radius']
            h = self.dimensions['height']
            return math.pi * r ** 2 * h

s = Solid("sphere", {"radius": 3})
print("Surface Area:", s.surface_area())
print("Volume:", s.volume())