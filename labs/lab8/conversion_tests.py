#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/22/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 06 (Oct 24 - Oct 31)
# Purpose/Assignment: Assignment 3
#

import unittest
import conversion
import summation

class ConversionTests(unittest.TestCase):
  def test_part_1(self):
    self.assertEqual(conversion.stringToFloat("687.69"), 687.69)
    self.assertEqual(conversion.stringToFloat("h"), None)
  def test_part_2(self):
    pass
if __name__ == "__main__":
  unittest.main()