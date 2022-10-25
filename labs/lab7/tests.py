#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/25/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 07 (Oct 31 - Oct Nov 7)
# Purpose/Assignment: Lab 7
#

import unittest
import histogram

class AssignmentTests(unittest.TestCase):
  def test_part_1(self):
    self.assertEqual(histogram.getHistogram("bears lions bears tigers bears lions"), {"lions": 2, "tigers": 1, "bears": 3})
    self.assertEqual(histogram.getHistogram("lions tigers bears lions bears bears"), {"lions": 2, "tigers": 1, "bears": 3})
if __name__ == "__main__":
  unittest.main()