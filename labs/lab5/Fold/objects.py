#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/16/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 05 (Oct 17 - Oct 21)
# Purpose/Assignment: Lab 5 (Fold Patterns)
#

import math

class Point:
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y
  def __repr__(self) -> str:
    return f"Point({self.x},{self.y})"
  def __eq__(self, other) -> bool:
    return (other is self or
        type(other) == Point and
        math.isclose(self.x, other.x) and
        math.isclose(self.y, other.y))
