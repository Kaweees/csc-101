#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/22/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 06 (Oct 24 - Oct 31)
# Purpose/Assignment: Lab 6 (Characters and Unicode)
#

def isEnglishUpper(char: str) -> bool:
  """Returns True if char is an uppercase English letter"""
  return ord(char) in range(65, 91)