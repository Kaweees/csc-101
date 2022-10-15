#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/14/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 04 (Oct 10 - Oct 17)
# Purpose/Assignment: Assignment 2
#

import unittest
import hw2

class AssignmentTests(unittest.TestCase):
  # The following test must not be modified and pass
  def test_part_1(self):
    self.assertTrue(hw2.isShorterThan(hw2.Duration(3, 20), hw2.Duration(3, 21)))
    self.assertFalse(hw2.isShorterThan(hw2.Duration(3, 21), hw2.Duration(3, 20)))

  def test_part_2(self):
    self.assertEqual(hw2.triangulateRectangle(hw2.Rectangle(hw2.Point(0, 1), hw2.Point(1, 0))), [hw2.Triangle(hw2.Point(0, 1), hw2.Point(1, 1), hw2.Point(1, 0)), hw2.Triangle(hw2.Point(1, 0), hw2.Point(0, 0), hw2.Point(0, 1))])
    self.assertEqual(hw2.triangulateRectangle(hw2.Rectangle(hw2.Point(0, 0), hw2.Point(1, -1))), [hw2.Triangle(hw2.Point(0, 0), hw2.Point(1, 0), hw2.Point(1, -1)), hw2.Triangle(hw2.Point(1, -1), hw2.Point(0, -1), hw2.Point(0, 0))])

  def test_part_3(self):
    self.assertEqual(hw2.createRectangle(hw2.Point(0, 1), hw2.Point(1, 0)), hw2.Rectangle(hw2.Point(0, 1), hw2.Point(1, 0)))
    self.assertEqual(hw2.createRectangle(hw2.Point(1, 1), hw2.Point(0, 0)), hw2.Rectangle(hw2.Point(0, 1), hw2.Point(1, 0)))

  def test_part_4(self):
    self.assertTrue(hw2.Song("Can't Help Falling In Love", "Elvis Presley", hw2.Duration(3, 0)).artist == "Elvis Presley")
    self.assertTrue(hw2.Song("Swing! Pendulum of Souls", "Bachi The Sunset", hw2.Duration(3, 21)).artist == "Bachi The Sunset")

  def test_part_5(self):
    self.assertTrue(hw2.getLengthsInSeconds([hw2.Song("Good Morning World!", "BURNOUT SYNDROMES", hw2.Duration(4, 9)), hw2.Song("熱き決闘者たち(Re-arranged)", "光宗信吉", hw2.Duration(4, 1))]), [249, 241])

  def test_part_6(self):
    self.assertTrue(hw2.getLengthsInSeconds([]))

if __name__ == "__main__":
  unittest.main()