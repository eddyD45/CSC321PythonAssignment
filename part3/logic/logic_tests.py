import unittest
from part3.logic.logic import *


class TestCases(unittest.TestCase):
    def test_case(self):
        self.assertTrue(is_even(4), True)
        self.assertTrue(in_an_interval(4), True)
        pass


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
