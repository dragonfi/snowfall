
import unittest
import math

from utils import to_polar, to_cartesian


class TestPolarCartesian(unittest.TestCase):
    def assertSeqAlmostEqual(self, seq1, seq2):
        self.assertEqual(len(seq1), len(seq2))
        for i, j in zip(seq1, seq2):
            self.assertAlmostEqual(i, j, msg= "seqs: {} != {}".format(seq1, seq2))

    def test_roundtrip(self):
        r, theta = 1, 2
        self.assertSeqAlmostEqual((r,theta), to_polar(*to_cartesian(r, theta)))

        x, y = 5, 2
        self.assertSeqAlmostEqual((x, y), to_cartesian(*to_polar(x, y)))

    def test_conversions(self):
        coordinate_pairs = [
            (1, 0, 1, 0),
            (0, 1, 1, math.pi / 2),
            (-1, 0, 1, math.pi),
            (0, -1, 1, - math.pi / 2),
            (1, 1, math.sqrt(2), math.pi / 4),
            (-1, -1, math.sqrt(2), -math.pi * 3 / 4),
            (5, 0, 5, 0),
            (0, -5, 5, - math.pi / 2),
            (3, 4, 5, math.atan2(4, 3)),
            (-3, -4, 5, math.atan2(-4, -3)),
        ]
        for x, y, r, theta in coordinate_pairs:
            self.assertSeqAlmostEqual((r, theta), to_polar(x, y))
            self.assertSeqAlmostEqual((x, y), to_cartesian(r, theta))


