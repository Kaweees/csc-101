#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/16/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 05 (Oct 17 - Oct 21)
# Purpose/Assignment: Lab 5 (Map and Filter Patterns)
#

import unittest
import objects
import functions

class MapFilterTest(unittest.TestCase):
  def test_1(self):
    self.assertEqual(functions.getAuthors([objects.Book("The Hobbit", "J.R.R. Tolkien", 1937), objects.Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)]), ["J.R.R. Tolkien", "J.R.R. Tolkien"])
    self.assertEqual(functions.getAuthors([objects.Book("Philosopher's Stone", "J. K. Rowling", 1997), objects.Book("Chamber of Secrets", "J. K. Rowling", 1998)]), ["J. K. Rowling", "J. K. Rowling"])
  
  def test_2(self):
    self.assertEqual(functions.getBooksBeforeYear([objects.Book("The Hobbit", "J.R.R. Tolkien", 1937), objects.Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)], 1950), [objects.Book("The Hobbit", "J.R.R. Tolkien", 1937)])
    self.assertEqual(functions.getBooksBeforeYear([objects.Book("Philosopher's Stone", "J. K. Rowling", 1997), objects.Book("Chamber of Secrets", "J. K. Rowling", 1998), objects.Book("Prisoner of Azkaban", "J. K. Rowling", 1999)], 1999), [objects.Book("Philosopher's Stone", "J. K. Rowling", 1997), objects.Book("Chamber of Secrets", "J. K. Rowling", 1998)])
  
  def test_3(self):
    self.assertEqual(functions.getAuthorsLC([objects.Book("The Hobbit", "J.R.R. Tolkien", 1937), objects.Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)]), ["J.R.R. Tolkien", "J.R.R. Tolkien"])
    self.assertEqual(functions.getAuthorsLC([objects.Book("Philosopher's Stone", "J. K. Rowling", 1997), objects.Book("Chamber of Secrets", "J. K. Rowling", 1998)]), ["J. K. Rowling", "J. K. Rowling"])
  
  def test_4(self):
    self.assertEqual(functions.getBooksBeforeYearLC([objects.Book("The Hobbit", "J.R.R. Tolkien", 1937), objects.Book("The Lord of the Rings", "J.R.R. Tolkien", 1954)], 1950), [objects.Book("The Hobbit", "J.R.R. Tolkien", 1937)])
    self.assertEqual(functions.getBooksBeforeYearLC([objects.Book("Philosopher's Stone", "J. K. Rowling", 1997), objects.Book("Chamber of Secrets", "J. K. Rowling", 1998), objects.Book("Prisoner of Azkaban", "J. K. Rowling", 1999)], 1999), [objects.Book("Philosopher's Stone", "J. K. Rowling", 1997), objects.Book("Chamber of Secrets", "J. K. Rowling", 1998)])

if __name__ == "__main__":
  unittest.main()
