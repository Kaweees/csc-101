import unittest
import vehicle

class VehicleTests(unittest.TestCase):
  def test_vehicle(self):
    v = vehicle.vehicle("red", 2019, 10000)
    self.assertEqual(v.color, "red")
    self.assertEqual(v.year, 2019)
    self.assertEqual(v.cost, 10000)

# Run the unit tests.
if __name__ == '__main__':
  unittest.main()
