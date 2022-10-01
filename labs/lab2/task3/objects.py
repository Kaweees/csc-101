import math

class Point:
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y
  def __str__(self):
    return f"({self.x}, {self.y})"

class Circle(Point):
  def __init__(self, x: float, y: float, radius: float):
    super().__init__(x, y)
    self.radius = radius

def distance(p1: Point, p2: Point):
  return math.sqrt(((p1.x - p2.x) ** 2) + ((p1.y - p2.y) ** 2))

def circles_overlap(c1: Circle, c2: Circle):
  return distance(c1, c2) < c1.radius + c2.radius