#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/16/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 05 (Oct 17 - Oct 21)
# Purpose/Assignment: Lab 5 (Map and Filter Patterns)
#

import objects

def getAuthors(books: list[objects.Book]) -> list[str]:
  """Returns a list of authors from a list of books"""
  ls = []
  for book in books:
    ls += [book.author]
  return ls

def getBooksBeforeYear(books: list[objects.Book], year: int) -> list[objects.Book]:
  """Returns a list of books published before a given year"""
  ls = []
  for book in books:
    if book.year < year :
      ls += [book]
  return ls

def getAuthorsLC(books: list[objects.Book]) -> list[str]:
  """Returns a list of authors from a list of books using list comprehension"""
  return [book.author for book in books]

def getBooksBeforeYearLC(books: list[objects.Book], year: int) -> list[objects.Book]:
  """Returns a list of books published before a given year using list comprehension"""
  return [book for book in books if book.year < year]