import unittest
from part2.funcs_objects.funcs_objects import *
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

    def test_distance_function(self):
        point1 = Point(1, 1)
        point2 = Point(1, 1)
        point3 = Point(0, 0)
        point4 = Point(0, 5)

        self.assertEqual(distance(point1, point2), 0)
        self.assertEqual(distance(point3, point4), 5)

    def test_circles_overlap_function(self):
        circle1 = Circle(Point(0, 0), 5)
        circle2 = Circle(Point(0, 1), 5)
        circle3 = Circle(Point(0, 0), 1)
        circle4 = Circle(Point(5, 5), 1)

        self.assertTrue(circles_overlap(circle1, circle2), True)
        self.assertFalse(circles_overlap(circle3, circle4), True)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
