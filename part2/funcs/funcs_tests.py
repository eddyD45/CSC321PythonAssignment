import unittest
from part2.funcs.funcs import *


class TestCases(unittest.TestCase):
    def test_f_1(self):
        self.assertEqual(f(1), 9)
        pass

    def test_f_2(self):
        self.assertEqual(f(2), 32)
        pass

    def test_g_1(self):
        self.assertEqual(g(1, 1), 2)
        pass

    def test_g_2(self):
        self.assertEqual(g(2, 2), 8)
        pass

    def test_hypotenuse_1(self):
        self.assertAlmostEqual(hypotenuse(1, 1), sqrt(2))
        pass

    def test_hypotenuse_2(self):
        self.assertAlmostEqual(hypotenuse(2, 2), sqrt(8))
        pass

    def test_is_positive_1(self):
        self.assertTrue(3, True)
        pass

    def test_is_positive_2(self):
        self.assertTrue((-3), False)
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
