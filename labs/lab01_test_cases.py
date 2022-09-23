#
# Test cases example for lab 1.
#

import unittest # import the module that supports writing unit tests

# Define a class that will be used for these test cases.
# This class will include testing functions.
#
# We will explain what the is code does in lecture.
#

class TestsLab1(unittest.TestCase):
  # Define one testing function per test.
  def test_expression_1(self):
    self.assertEqual(0 + 1, 1)
    
  def test_expression_2(self):
    self.assertEqual(2 * 2, 4)

  # Add additional tests below  
  def test_expression_3(self):
    self.assertEqual(19 // 3, 6)
  
  def test_expression_4(self):
    self.assertAlmostEqual(round(19 / 3, 2), 6.33)

  def test_expression_5(self):
    self.assertAlmostEqual(round(19 / 3.0, 2), 6.33)

  def test_expression_6(self):
    self.assertAlmostEqual(round(19.0 / 3.0, 2), 6.33)
  
  def test_expression_7(self):
    self.assertEqual(4 * 2 + 27 // 3 + 4, 4)

  def test_expression_7(self):
    self.assertEqual(4 * (2 + 27) // 3 + 4, 6)
  
  def test_expression_7(self):
    x = 1
    y = 2
    self.assertEqual(2 * x + y, 4)

# Run the unit tests.
if __name__ == '__main__':
  unittest.main()
