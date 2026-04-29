import math

class Point:
    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def distance_to(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def __repr__(self):
        return f"Point({self.x}, {self.y})"


class Line:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def length(self):
        return self.p1.distance_to(self.p2)

    def slope(self):
        if self.p2.x == self.p1.x:
            return None
        return (self.p2.y - self.p1.y) / (self.p2.x - self.p1.x)

    def __repr__(self):
        return f"Line({self.p1}, {self.p2})"