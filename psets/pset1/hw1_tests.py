#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 10/10/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 03 (Oct 03 - Oct 10)
# Purpose/Assignment: Assignment 1
#

import hw1
import unittest

class TestCases(unittest.TestCase):
  def test_Price_1(self):
    self.assertTrue(hw1.add_prices(hw1.Price(101, 1), hw1.Price(100, 1)) == hw1.Price(201, 2))
    self.assertTrue(hw1.add_prices(hw1.Price(301, 1), hw1.Price(105, 1)) == hw1.Price(406, 2))

  def test_Price_2(self):
    self.assertTrue(hw1.Rectangle(hw1.Point(0, 1), hw1.Point(1, 0)).bottom_right == hw1.Rectangle(hw1.Point(-1, 4), hw1.Point(1, 0)).bottom_right)
    self.assertTrue(hw1.Rectangle(hw1.Point(1, 0), hw1.Point(4, -1)).top_left == hw1.Rectangle(hw1.Point(1, 0), hw1.Point(6, -5)).top_left)

  def test_Price_eq_1(self):
    self.assertEqual(hw1.Price(1, 20), hw1.Price(1, 20))
    self.assertEqual(hw1.Price(20, 20), hw1.Price(20, 20))

  def test_Rectangle_1(self):
    self.assertEqual(hw1.rectangle_perimeter(hw1.Rectangle(hw1.Point(0, 1), hw1.Point(1, 0))), 4)
    self.assertEqual(hw1.rectangle_perimeter(hw1.Rectangle(hw1.Point(0, 0), hw1.Point(1, -1))), 4)

  def test_Rectangle_2(self):
    self.assertEqual(hw1.rectangle_lower_half(hw1.Rectangle(hw1.Point(0, 1), hw1.Point(1, 0))), hw1.Rectangle(hw1.Point(0, 0.5), hw1.Point(1, 0)))
    self.assertEqual(hw1.rectangle_lower_half(hw1.Rectangle(hw1.Point(0, 0), hw1.Point(1, -1))), hw1.Rectangle(hw1.Point(0, -0.5), hw1.Point(1, -1)))
  
  def test_Rectangle_3(self):
    self.assertTrue(hw1.is_square(hw1.Rectangle(hw1.Point(0, 1), hw1.Point(1, 0))))
    self.assertTrue(hw1.is_square(hw1.Rectangle(hw1.Point(0, 0), hw1.Point(1, -1))))

  def test_Rectangle_4(self):
    self.assertTrue(hw1.circle_within_rectangle(hw1.Circle(hw1.Point(0, 0), 1), hw1.Rectangle(hw1.Point(-4, 4), hw1.Point(4, -4))))
    self.assertTrue(hw1.circle_within_rectangle(hw1.Circle(hw1.Point(0, 0), 3), hw1.Rectangle(hw1.Point(-5, 5), hw1.Point(5, -5))))
  
  def test_Rectangle_5(self):
    self.assertEqual(hw1.circle_bound(hw1.Rectangle(hw1.Point(-2, 1.5), hw1.Point(2, -1.5))), hw1.Circle(hw1.Point(0, 0), 5))
    self.assertEqual(hw1.circle_bound(hw1.Rectangle(hw1.Point(-1.5, 2), hw1.Point(1.5, -2))), hw1.Circle(hw1.Point(0, 0), 5))
if __name__ == '__main__':
  unittest.main()