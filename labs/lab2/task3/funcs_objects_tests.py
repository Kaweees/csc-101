#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 09/19/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 02 (Sept 26 - Oct 03)
# Purpose/Assignment: Lab 2 - Task 3 (Objects)
#

import unittest
import objects

class TestCases(unittest.TestCase):
  def test_point(self):
    # Add code here to verify that a point is initialized correctly.
    p = objects.Point(1.0, 2.0)
    self.assertEqual(p.x, 1.0)
    self.assertEqual(p.y, 2.0)

  def test_circle(self):
    # Add code here to verify that a circle is initialized correctly.
    c = objects.Circle(1.0, 2.0, 3.0)
    self.assertEqual(c.x, 1.0)
    self.assertEqual(c.y, 2.0)
    self.assertEqual(c.radius, 3.0)

  # Add other testing functions for distance and circles_overlap.
  def test_distance(self):
    p1 = objects.Point(1.0, 2.0)
    p2 = objects.Point(4.0, 6.0)
    self.assertEqual(objects.distance(p1, p2), 5.0)
  def test_overlap(self):
    c1 = objects.Circle(1.0, 2.0, 3.0)
    c2 = objects.Circle(4.0, 6.0, 3.0)
    self.assertTrue(objects.circles_overlap(c1, c2))
# Run the unit tests.
if __name__ == '__main__':
  unittest.main()