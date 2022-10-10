#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 04 (Oct 10 - Oct 17)
# Purpose/Assignment: Lab 4 (ListPatterns)
#

input = [1, 1, 1, 1, 1, 1, 1, 1]
goal  = [0, 1, 0, 1, 0, 1, 0, 1]

def patternFunction(index: int, element: int) -> int:
    return index % 2
