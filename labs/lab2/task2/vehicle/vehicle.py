#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 09/19/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 02 (Sept 26 - Oct 03)
# Purpose/Assignment: Lab 2 - Task 2 (Vehicle)
#

class vehicle:
  def __init__(self, color: str, year: int, cost: float) -> None:
    self.color = color
    self.year = year
    self.cost = cost
  def __str__(self) -> str:
    return f"Car of color ({self.color} from the year {self.year}) of cost ({self.cost}"