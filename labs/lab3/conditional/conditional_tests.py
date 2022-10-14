#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 03 (Oct 03 - Oct 10)
# Purpose/Assignment: Lab 3 (Logic)
#

import unittest
import conditional

class TestCases(unittest.TestCase):
  def test_case_one(self):
    # Replace pass with the test code.
    self.assertAlmostEqual(conditional.max_101(1.0, 2.0), 2.0)
    self.assertAlmostEqual(conditional.max_101(3.0, 2.0), 3.0)

  def test_case_two(self):
    self.assertAlmostEqual(conditional.max_of_three(1.0, 2.0, 3.0), 3.0)
    self.assertAlmostEqual(conditional.max_of_three(3.0, 7.0, 3.0), 7.0)

  def test_case_three(self):
    self.assertEqual(conditional.rental_late_fee(69), 100)

# Run the unit tests.
if __name__ == '__main__':
  unittest.main()