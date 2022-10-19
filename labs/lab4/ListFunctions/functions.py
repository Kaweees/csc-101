#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 04 (Oct 10 - Oct 17)
# Purpose/Assignment: Lab 4 (ListFunctions)
#

def areTwoEqual(l: list, index_1: int, index_2: int) -> bool:
  """Given a list and two indexes, returns whether the two values at those indexes are equal"""
  return l[index_1] == l[index_2]

def sumOfThree(l: list) -> float:
  """Given a list, returns the sum of the first three values"""
  if len(l) != 3:
    return 0
  return l[0] + l[1] + l[2]

def sumOfUpToThree(l: list) -> float:
  """Given a list, returns the sum of the first three values, or the sum of all values if there are less than three"""
  if len(l) == 0:
    return 0
  elif len(l) <= 2:
    return sum(l)
  else:
    return l[0] + l[1] + l[2]

def getFromFirstAsIndex(l: list) -> int:
  """Given a list, returns the value at the index of the value of the first element"""
  return l[l[0]]