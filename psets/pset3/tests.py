#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/22/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 06 (Oct 24 - Oct 31)
# Purpose/Assignment: Assignment 3
#

import unittest
import math
import hw3

class AssignmentTests(unittest.TestCase):
  def test_part_1(self):
    self.assertEqual(hw3.getBooksByAuthors([hw3.Book("The Hobbit", ["J.R.R. Tolkien"], 1937)], ["J.R.R. Tolkien"]), [hw3.Book("The Hobbit", ["J.R.R. Tolkien"], 1937)])
    self.assertEqual(hw3.getBooksByAuthors([hw3.Book("Philosopher's Stone", ["J. K. Rowling"], 1997)], ["J. K. Rowling"]), [hw3.Book("Philosopher's Stone", ["J. K. Rowling"], 1997)])
  def test_part_2(self):
    self.assertEqual(hw3.belowAveragePay([hw3.Employee("Bob", 25, 687), hw3.Employee("Peter", 35, 687)], 30), [hw3.Employee("Bob", 25, 687)])
    self.assertNotEqual(hw3.belowAveragePay([hw3.Employee("Bob", 25, 687), hw3.Employee("Peter", 35, 687)], 30), [hw3.Employee("Peter", 35, 687)])
  def test_part_3(self):
    city_links = [
      ['san luis obispo', 'santa margarita'],
      ['san luis obispo', 'pismo beach'],
      ['atascadero', 'santa margarita'],
      ['atascadero', 'creston']
    ]
    self.assertTrue(hw3.validateRoute(city_links, ['san luis obispo', 'santa margarita', 'atascadero']))
    self.assertFalse(hw3.validateRoute(city_links, ['san luis obispo', 'atascadero']))
  def test_part_4(self):
    pass
if __name__ == "__main__":
  unittest.main()