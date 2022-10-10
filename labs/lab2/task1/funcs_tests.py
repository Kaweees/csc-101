#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 09/19/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 02 (Sept 26 - Oct 03)
# Purpose/Assignment: Lab 2 - Task 1
#

import unittest
import funcs

class TestCases(unittest.TestCase):
  def test_f_1(self):
    self.assertEqual(funcs.f(1.0), 9.0)
    self.assertEqual(funcs.f(3.0), 69.0)
  def test_f_2(self):
    self.assertEqual(funcs.g(3.0, 4.0), 25.0)
    self.assertEqual(funcs.g(4.0, 3.0), 25.0)
  def test_f_3(self):
    self.assertEqual(funcs.hypotenuse(3.0, 4.0), 5.0)
    self.assertEqual(funcs.hypotenuse(4.0, 3.0), 5.0)
  def test_f_4(self):
    self.assertTrue(funcs.is_positive(1.0))
    self.assertFalse(funcs.is_positive(-1.0))

# Run the unit tests.
if __name__ == '__main__':
  unittest.main()