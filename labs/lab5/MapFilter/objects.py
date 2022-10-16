#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/16/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 05 (Oct 17 - Oct 21)
# Purpose/Assignment: Lab 5 (Map and Filter Patterns)
#

class Book:
  def __init__(self, title: str, author: str, year: int):
    self.title = title
    self.author = author
    self.year = year

  def __repr__(self) -> str:
    return f"Book({self.title},{self.author},{self.year})"

  def __eq__(self, other) -> bool:
    return (other is self or
        type(other) == Book and
        self.title == other.title and
        self.author == other.author and
        self.year == other.year)
