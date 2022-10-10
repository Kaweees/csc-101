#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 09/19/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 02 (Sept 26 - Oct 03)
# Purpose/Assignment: Lab 2 - Task 1
#

import math

def f(x: float) -> float:
  return (7 * (x ** 2)) + (2 * x)

def g(x: float, y: float) -> float:
  return ((x ** 2) + (y ** 2))

def hypotenuse(x: float, y: float) -> float:
  return math.sqrt((x ** 2) + (y ** 2))

def is_positive(x: float) -> bool:
  return x > 0