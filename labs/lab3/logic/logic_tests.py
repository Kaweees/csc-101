#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 03 (Oct 03 - Oct 10)
# Purpose/Assignment: Lab 3 (Logic)
#

import unittest
import logic

class TestCases(unittest.TestCase):
  def test_logic_one(self):
    # Replace pass with the test code.
    self.assertEqualTrue(logic.is_even(2))
    self.assertEqualTrue(logic.is_even(2))
    self.assertEqualFalse(logic.is_even(1))

  def test_logic_two(self):
    self.assertEqualTrue(logic.in_an_interval(50.0))
    self.assertEqualTrue(logic.in_an_interval(13.0))

# Run the unit tests.
if __name__ == '__main__':
  unittest.main()