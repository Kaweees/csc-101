# Name:
# Date:
# Github:

import unittest

class listFunctionTests(unittest.TestCase):
    # Do not modify these tests
    def test_includedOne(self):
        self.assertTrue(functions.areTwoEqual([1, 2, 3, 2], 1, 3))
        self.assertFalse(functions.areTwoEqual([1, 2, 3, 2], 1, 2))

    def test_includedTwo(self):
        self.assertEqual(functions.sumOfThree([1, 2, 3, 2]), 0)
        self.assertEqual(functions.sumOfThree([1, 2]), 0)
        self.assertEqual(functions.sumOfThree([1, 2, 3]), 6)

    def test_includedThree(self):
        self.assertEqual(functions.sumOfUpToThree([1, 2, 3, 2]), 6)
        self.assertEqual(functions.sumOfUpToThree([1, 2]), 3)
        self.assertEqual(functions.sumOfUpToThree([1, 2, 3]), 6)

    def test_includedFour(self):
        self.assertEqual(functions.getFromFirstAsIndex([1, 2, 3, 2]), 2)
        self.assertEqual(functions.getFromFirstAsIndex([2, 2, 3, 2]), 3)
        self.assertEqual(functions.getFromFirstAsIndex([-1, 2, 3, 2]), 2)

    # Write your tests below

if __name__ == "__main__":
    unittest.main()
