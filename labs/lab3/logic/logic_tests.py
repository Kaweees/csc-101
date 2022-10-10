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
    self.assertEqual(logic.max_101(1, 2), 2)
    self.assertEqual(logic.max_101(2, 1), 2)
    self.assertEqual(logic.max_101(1, -2), 1)

  def test_logic_two(self):
    pass

  def test_logic_three(self):
    self.assertEqual(logic.rental_late_fee(0), 0)
    self.assertEqual(logic.rental_late_fee(15), 7)
    self.assertEqual(logic.rental_late_fee(69), 100)
    pass

# Run the unit tests.
if __name__ == '__main__':
  unittest.main()