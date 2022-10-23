#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/16/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 05 (Oct 17 - Oct 21)
# Purpose/Assignment: Lab 5 (Fold Patterns)
#

import objects

def getMinimumDistance(ls: list[int]) -> int:
  """return the index of the element of minimum value from the input list"""
  if len(ls) == []:
    return None
  minVal = ls[0]
  for i in range(len(ls)):
    if ls[i] < minVal:
      minVal = i
  return minVal

def areAllTrue(ls: list[bool]) -> bool:
  """return True if all elements in the input list are True"""
  if ls == []:
    return None
  for item in ls:
    if item == False:
      return False
  return True

def getCenterPoint(ls: list[objects.Point]) -> objects.Point:
  """return the center point of the input list of points"""
  x, y = 0, 0
  if len(ls) == []:
    return None
  for item in ls:
    x += item.x
    y += item.y
  return objects.Point(x / len(ls), y / len(ls))

def countLessThanFour(ls: list[str]) -> int:
  """return the number of elements in the input list whose length is less than 4"""
  if len(ls) == []:
    return None
  count = 0
  for item in ls:
    if item < 4:
      count += 1
  return count