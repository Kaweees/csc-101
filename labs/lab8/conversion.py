#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/22/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 06 (Oct 24 - Oct 31)
# Purpose/Assignment: Assignment 3
#

from typing import Optional

def stringToFloat(input: str) -> Optional[float]:
  try:
    return float(input)
  except ValueError:
    return None