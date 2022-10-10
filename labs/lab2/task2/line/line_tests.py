#
# Programmer: Miguel Villa Floran
# GitHub: Kaweees
# Date: 09/19/2022
# Course Name: CSC 101 - Fundamentals of Computer Science
# Section: Week 02 (Sept 26 - Oct 03)
# Purpose/Assignment: Lab 2 - Task 2 (Line)
#

import unittest
import line

class LineTests(unittest.TestCase):
  def test_line(self):
    # The following line should show a warning on the value "shoe".
    result = line.Line(1.0, 2.0, 3.0, 4.0)
    self.assertEqual(result.x1, 1.0)
    self.assertEqual(result.y1, 2.0)
    self.assertEqual(result.x2, 3.0)
    self.assertEqual(result.y2, 4.0)

  def test_line_again(self):
    # Add code here.
    l1 = line.Line(687.0, 254.0, 9999.0, 4414.0)
    self.assertEqual(l1.x1, 687.0)
    self.assertEqual(l1.y1, 254.0)
    self.assertEqual(l1.x2, 9999.0)
    self.assertEqual(l1.y2, 4414.0)

# Run the unit tests.
if __name__ == '__main__':
  unittest.main()