#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 04 (Oct 10 - Oct 17)
# Purpose/Assignment: Lab 4 (ListPatterns)
#

input = ["A", "A", "A", "A", "B", "B", "B", "B"]
goal  = ["A", "C", "A", "C", "B", "D", "B", "D"]

def patternFunction(index: int, element: int) -> int:
  return chr(ord(element) + (2 * (index % 2)))