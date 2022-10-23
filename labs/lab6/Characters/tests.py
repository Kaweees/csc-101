#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/22/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 06 (Oct 24 - Oct 31)
# Purpose/Assignment: Lab 6 (Characters and Unicode)
#

import unittest
import functions

class CharacterTest(unittest.TestCase):
  def test_1(self):
    self.assertEqual(functions.isEnglishUpper('A'), True)
    self.assertEqual(functions.isEnglishUpper('C'), True)
  
if __name__ == "__main__":
  unittest.main()