import unittest
import funcs

class TestCases(unittest.TestCase):
  def test_f_1(self):
    self.assertEqual(funcs.f(1.0), 9.0)
  def test_f_2(self):
    self.assertEqual(funcs.g(3.0, 4.0), 25.0)
  def test_f_3(self):
    self.assertEqual(funcs.hypotenuse(3.0, 4.0), 5.0)
  def test_f_4(self):
    self.assertTrue(funcs.f(1.0))

# Run the unit tests.
if __name__ == '__main__':
  unittest.main()