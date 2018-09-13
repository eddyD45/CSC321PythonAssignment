import unittest
from part2.funcs_objects.objects import *


class TestCases(unittest.TestCase):
    def test_point(self):
        point = Point(2, 2)
        self.assertEqual(point.x, 2)
        self.assertEqual(point.y, 2)
        pass

    def test_circle(self):
        center = Point(1, 1)
        circle = Circle(center, 2)

        self.assertEqual(circle.center.x, 1)
        self.assertEqual(circle.center.y, 1)
        self.assertEqual(circle.radius, 2)
        pass

    # Add other testing functions


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
