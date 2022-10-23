#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 03 (Oct 03 - Oct 10)
# Purpose/Assignment: Lab 3 (Object Equality)
#

import math

class Point:
  def __init__(self, x: float, y: float) -> None:
    self.x = x
    self.y = y
  def __eq__(self, other : object) -> bool:
    return (type(other) is Point
      and math.isclose(self.x, other.x) and math.isclose(self.y, other.y))