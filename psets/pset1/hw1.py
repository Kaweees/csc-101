import math

class Price:
  def __init__(self, dollars: int, cents: int):
    self.dollars = dollars
    self.cents = cents
  def __str__(self):
    return f"${str(self.dollars)}.{str(self.cents)}"
  def __eq__(self, other):
    return (other is self or
      type(other) == Price and
      self.dollars == other.dollars and self.cents == other.cents)

def add_prices(p1: Price, p2: Price) -> Price:
  """Returns the sum of two Price objects."""
  return Price(p1.dollars + p2.dollars + ((p1.cents + p2.cents) // 100), ((p1.cents + p2.cents) % 100))

class Point:
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y
  def __eq__(self, other: object) -> bool:
    return (other is self or
      type(other) == Point and
     math.isclose(self.x, other.x) and math.isclose(self.y, other.y))

class Rectangle:
  def __init__(self, top_left: Point, bottom_right: Point) -> None:
    self.top_left = top_left
    self.bottom_right = bottom_right
  def __eq__(self, other: object) -> bool:
    return (other is self or
      type(other) == Rectangle and
      self.top_left == other.top_left and self.bottom_right == other.bottom_right)

class Circle:
  def __init__(self, center: Point, radius: float) -> None:
    self.center = center
    self.radius = radius
  def __eq__(self, other: object) -> bool:
    return (other is self or
      type(other) == Circle and
      self.center == other.center and math.isclose(self.radius, other.radius))

def rectangle_perimeter(rect: Rectangle) -> float:
  """Returns the perimeter of a rectangle."""
  return 2 * (rect.bottom_right.x - rect.top_left.x) + 2 * (rect.top_left.y - rect.bottom_right.y)

def rectangle_lower_half(rect: Rectangle) -> Rectangle:
  """Returns a new Rectangle object that is the lower half of the given Rectangle object."""
  return Rectangle(Point(rect.top_left.x, (rect.top_left.y + rect.bottom_right.y) / 2), Point(rect.bottom_right.x, rect.bottom_right.y))

def is_square(rect: Rectangle) -> bool:
  """Returns True if the given Rectangle object is a square."""
  return (rect.bottom_right.x - rect.top_left.x) == (rect.top_left.y - rect.bottom_right.y)

def circle_within_rectangle(circle: Circle, rect: Rectangle) -> bool:
  """Returns True if the given Circle object is within the given Rectangle object."""
  return ((circle.center.x + circle.radius) > rect.top_left.x and
    (circle.center.y + circle.radius) < rect.top_left.y and
    (circle.center.x - circle.radius) < rect.bottom_right.x and
    (circle.center.y - circle.radius) > rect.bottom_right.y)

def circle_bound(rect: Rectangle) -> Circle:
  """Returns a new Circle object that is the smallest circle that bounds the given Rectangle object."""
  return Circle(Point((rect.top_left.x + rect.bottom_right.x) / 2, (rect.top_left.y + rect.bottom_right.y) / 2), math.sqrt((rect.bottom_right.x - rect.top_left.x) ** 2 + (rect.top_left.y - rect.bottom_right.y) ** 2))