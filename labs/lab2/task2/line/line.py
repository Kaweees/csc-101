#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 09/19/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 02 (Sept 26 - Oct 03)
# Purpose/Assignment: Lab 2 - Task 2 (Line)
#

class Line:
  def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None:
    self.x1 = x1
    self.y1 = y1
    self.x2 = x2
    self.y2 = y2
  def __str__(self) -> str:
    return f"Line from ({self.x1}, {self.y1}) to ({self.x2}, {self.y2})"