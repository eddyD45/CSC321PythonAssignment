import unittest

from part1.vehicle.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    def test_vehicle(self):
        myVehicle = Vehicle(4, 100, 4, True)
        yourVehicle = Vehicle(2, 0, 1, False)

        self.assertEqual(myVehicle.numberOfWheels, 4)
        self.assertEqual(myVehicle.currentFuel, 100)
        self.assertEqual(myVehicle.numberOfDoors, 4)
        self.assertEqual(myVehicle.isConvertible, True)

        self.assertEqual(yourVehicle.numberOfWheels, 2)
        self.assertEqual(yourVehicle.currentFuel, 0)
        self.assertEqual(yourVehicle.numberOfDoors, 1)
        self.assertEqual(yourVehicle.isConvertible, False)

# Add code here.


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
