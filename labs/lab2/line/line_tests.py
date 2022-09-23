import unittest
import line

class LineTests(unittest.TestCase):
  def test_line(self):
    # The following line should show a warning on the value "shoe".
    result = line.Line("shoe", 2.0, 3.0, 4.0)
    self.assertEqual(result.x1, 1.0)
    self.assertEqual(result.y1, 2.0)
    self.assertEqual(result.x2, 3.0)
    self.assertEqual(result.y2, 4.0)

  def test_line_again(self):
    # Add code here.
    l1 = Line(687.0, 254.0, 9999.0, 4414.0)
    self.assertEqual(result.x1, 687.0)
    self.assertEqual(result.y1, 254.0)
    self.assertEqual(result.x2, 9999.0)
    self.assertEqual(result.y2, 4414.0)

# Run the unit tests.
if __name__ == '__main__':
  unittest.main()