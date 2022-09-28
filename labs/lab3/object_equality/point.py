import math

class Point:
  def __init__(self, x: float, y: float):
    self.x = x
    self.y = y
  def __eq__(self, other : object) -> bool:
    return type(other) is Point and math.isclose(self.x, other.x) and math.isclose(self.y, other.y)