import unittest

from part1.line.line import Line


class LineTests(unittest.TestCase):
    def test_line(self):
        sampleLine = Line(2, 2, 2, 2)
        secondSampleLine = Line(5, 5, 5, 5)

        self.assertEqual(sampleLine.x1, 2)
        self.assertEqual(sampleLine.x2, 2)
        self.assertEqual(sampleLine.y1, 2)
        self.assertEqual(sampleLine.y2, 2)

        self.assertEqual(secondSampleLine.x1, 5)
        self.assertEqual(secondSampleLine.x2, 5)
        self.assertEqual(secondSampleLine.y1, 5)
        self.assertEqual(secondSampleLine.y2, 5)

        # 2) Use assertEqual on each field in the new Line to verify
        #    that it holds the expected value.


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
