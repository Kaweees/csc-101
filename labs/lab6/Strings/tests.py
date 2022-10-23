#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/22/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 06 (Oct 24 - Oct 31)
# Purpose/Assignment: Lab 6 (String Operations)
#

import unittest
import functions

class StringTest(unittest.TestCase):
  def test_1(self):
    self.assertEqual(functions.swapCase("AbC"), "aBc")
    self.assertEqual(functions.swapCase("aBc"), "AbC")
  def test_2(self):
    self.assertEqual(functions.replaceChar("AbC", "A", "Q"), "QbC")
    self.assertEqual(functions.replaceChar("aBc", "B","Q"), "aQc")
if __name__ == "__main__":
  unittest.main()
