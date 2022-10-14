#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 03 (Oct 03 - Oct 10)
# Purpose/Assignment: Lab 3 (Logic)
#

def is_even(x : int) -> bool:
  return x % 2 == 0

def in_an_interval(n : float) -> bool:
  return (2 <= n and n < 9) or (12 < n and n <= 19) or (101 <= 101 and n <= 103)