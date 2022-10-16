#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/16/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 05 (Oct 17 - Oct 21)
# Purpose/Assignment: Lab 5 (Fold Patterns)
#

import unittest
import objects
import functions

class FoldTest(unittest.TestCase):

  def test_1(self):
    self.assertEqual(functions.getMinimumDistance([1, 2, 3, 5, 8, 9]), 1)
    self.assertEqual(functions.getMinimumDistance([5, 7, 3, 5, 8, 9]), 3)
  
  def test_2(self):
    self.assertTrue(functions.areAllTrue([True, True, True, True]))
    self.assertFalse(functions.areAllTrue([True, False, True, True]))
  
  def test_3(self):
    pass
if __name__ == "__main__":
  unittest.main()
