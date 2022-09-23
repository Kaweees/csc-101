class vehicle:
  def __init__(self, color: str, year: int, cost: float):
    self.color = color
    self.year = year
    self.cost = cost
  def __str__ (self):
    return f"Car of color ({self.color} from the year {self.year}) of cost ({self.cost}"