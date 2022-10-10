#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 03 (Oct 03 - Oct 10)
# Purpose/Assignment: Lab 3 (Object Equality)
#

import unittest
import point

class TestCases(unittest.TestCase):
  def test_point_one(self):
    pt = point.Point(1, 2)
    self.assertAlmostEqual(pt.x, 1)
    self.assertAlmostEqual(pt.y, 2)

  def test_point_two(self):
    pt = point.Point(-4.7, 19.2)
    self.assertAlmostEqual(pt.x, -4.7)
    self.assertAlmostEqual(pt.y, 19.2)

  def test_equality_one(self):
    # Replace pass with the test code.
    pt1 = point.Point(-4, 19)
    pt2 = point.Point(-4, 19)
    self.assertEqual(pt1, pt2)

  def test_equality_two(self):
    # Replace pass with the test code.
    pt1 = point.Point(69, 19)
    pt2 = point.Point(175, 19)
    self.assertEqual(pt1, pt2)

# Run the unit tests.
if __name__ == '__main__':
  unittest.main()