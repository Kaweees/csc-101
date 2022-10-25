#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/22/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 06 (Oct 24 - Oct 31)
# Purpose/Assignment: Assignment 3
#

from typing import Optional

class Book:
  """Represents a Book with multiple authors"""
  def __init__(self, title: str, authors: list[str], year: int) -> None:
    self.title = title
    self.authors = authors
    self.year = year
  def __repr__(self) -> str:
    return f"Book({self.title},{self.authors},{self.year})"
  def __eq__(self, other) -> bool:
    return (other is self or
      type(other) == Book and
      self.title == other.title and
      self.authors == other.authors and
      self.year == other.year)

def getBooksByAuthors(books: list[Book], authors: list[str]) -> list[Book]:
  """Returns a list of books that have the given authors"""
  return [book for book in books if set(authors).issubset(book.authors)]

class Employee:
  """Represents an Employee with a name, pay rate, and job code"""
  def __init__(self, name: str, pay_rate: int, job_code: int) -> None:
    self.name = name
    self.pay_rate = pay_rate
    self.job_code = job_code
  def __repr__(self) -> str:
    return f"Employee({self.name},{self.pay_rate},{self.job_code})"
  def __eq__(self, other) -> bool:
    return (other is self or
      type(other) == Employee and
      self.name == other.name and
      self.pay_rate == other.pay_rate and
      self.job_code == other.job_code)

def belowAveragePay(employees: list[Employee], average: float) -> list[Book]:
  """Returns a list of books that have a pay below the average"""
  return [employee for employee in employees if employee.pay_rate < average]

def validateRoute(city_links : list[list[str]], route: list[str]) -> bool:
  """Returns true if the route is valid, false otherwise"""
  for i in range(len(route) - 1):
    if not(any(city_link for city_link in city_links if set(sorted(route[i:i+2])).issubset(sorted(city_link)))):
      return False
  return True

def groupIntoThrees(nums: list[int]) -> list[list[int]]:
  """Returns a list of lists of 3 numbers"""
  return [nums[i:i+3] for i in range(0, len(nums), 3)]

def getLongestRepetition(nums: list[int]) -> Optional[int]:
  """Returns the longest repetition of an integer in a list"""
  if nums == []:
    return None
  longest_index = 0
  longest = 0
  for i in range(len(nums) - 1):
    for j in range(i, len(nums) - 1):
      if nums[i] == nums[j]:
        if j - i > longest:
          longest = j - i
          longest_index = i
      else:
        break
  return longest_index