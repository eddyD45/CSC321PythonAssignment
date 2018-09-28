import unittest
import utility
import point


class TestCases(unittest.TestCase):
    def test_point_one(self):
        pt = point.Point(1, 2)
        self.assertAlmostEqual(pt.x, 1)
        self.assertAlmostEqual(pt.y, 2)
        self.assertTrue(utility.epsilon_equal(pt.x, 1))
        self.assertTrue(utility.epsilon_equal(pt.y, 2))

    def test_point_two(self):
        pt = point.Point(-4.7, 19.2)
        self.assertAlmostEqual(pt.x, -4.7)
        self.assertTrue(utility.epsilon_equal(pt.x, -4.7))

        self.assertAlmostEqual(pt.y, 19.2)
        self.assertTrue(utility.epsilon_equal(pt.y, 19.2))


def test_equality(self):
        point1 = point.Point(3, 2)
        point2 = point.Point(3, 2)
        self.assertEqual(point1, point2)
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
