import unittest
from math import log

from pierre.measures import shannon


class TestShanon(unittest.TestCase):

    def test_kullback_leibler(self):
        answer = sum([0.389 * log(0.389 / 0.35), 0.5 * log(0.5 / 0.563), 0.25 * log(0.25 / 0.4),
                      0.625 * log(0.625 / 0.5), 0.00001 * log(0.00001 / 0.00001), 0.00001 * log(0.00001 / 0.00001),
                      0.25 * log(0.25 / 0.00001)])
        self.assertEqual(shannon.kullback_leibler(p=[0.389, 0.5, 0.25, 0.625, 0.0, 0.0, 0.25],
                                                  q=[0.35, 0.563, 0.4, 0.5, 0.0, 0.0, 0.0]),
                         answer)

    def test_jeffreys(self):
        answer = sum([(0.389 - 0.35) * log(0.389 / 0.35),
                      (0.5 - 0.563) * log(0.5 / 0.563),
                      (0.25 - 0.4) * log(0.25 / 0.4),
                      (0.625 - 0.5) * log(0.625 / 0.5),
                      (0.00001 - 0.00001) * log(0.00001 / 0.00001),
                      (0.00001 - 0.00001) * log(0.00001 / 0.00001),
                      (0.25 - 0.00001) * log(0.25 / 0.00001)])
        self.assertEqual(shannon.jeffreys(p=[0.389, 0.5, 0.25, 0.625, 0.0, 0.0, 0.25],
                                          q=[0.35, 0.563, 0.4, 0.5, 0.0, 0.0, 0.0]),
                         answer)

    def test_k_divergence(self):
        answer = sum([0.389 * log((2 * 0.389) / (0.389 + 0.35)),
                      0.5 * log((2 * 0.5) / (0.5 + 0.563)),
                      0.25 * log((2 * 0.25) / (0.25 + 0.4)),
                      0.625 * log((2 * 0.625) / (0.625 + 0.5)),
                      0.00001 * log((2 * 0.00001) / (0.00001 + 0.00001)),
                      0.00001 * log((2 * 0.00001) / (0.00001 + 0.00001)),
                      0.25 * log((2 * 0.25) / (0.25 + 0.00001))])
        self.assertEqual(shannon.k_divergence(p=[0.389, 0.5, 0.25, 0.625, 0.0, 0.0, 0.25],
                                              q=[0.35, 0.563, 0.4, 0.5, 0.0, 0.0, 0.0]),
                         answer)

    def test_topsoe(self):
        answer = sum([
            (0.389 * log((2 * 0.389) / (0.389 + 0.35))) + (0.35 * log((2 * 0.35) / (0.389 + 0.35))),
            (0.5 * log((2 * 0.5) / (0.5 + 0.563))) + (0.563 * log((2 * 0.563) / (0.5 + 0.563))),
            (0.25 * log((2 * 0.25) / (0.25 + 0.4))) + (0.4 * log((2 * 0.4) / (0.25 + 0.4))),
            (0.625 * log((2 * 0.625) / (0.625 + 0.5))) + (0.5 * log((2 * 0.5) / (0.625 + 0.5))),
            (0.00001 * log((2 * 0.00001) / (0.00001 + 0.00001))) + (0.00001 * log((2 * 0.00001) / (0.00001 + 0.00001))),
            (0.00001 * log((2 * 0.00001) / (0.00001 + 0.00001))) + (0.00001 * log((2 * 0.00001) / (0.00001 + 0.00001))),
            (0.25 * log((2 * 0.25) / (0.25 + 0.00001))) + (0.00001 * log((2 * 0.00001) / (0.25 + 0.00001))),
        ])
        self.assertEqual(shannon.topsoe(p=[0.389, 0.5, 0.25, 0.625, 0.0, 0.0, 0.25],
                                        q=[0.35, 0.563, 0.4, 0.5, 0.0, 0.0, 0.0]),
                         answer)

    def test_jensen_shannon(self):
        answer_l = sum([0.389 * log((2 * 0.389) / (0.389 + 0.35)),
                        0.5 * log((2 * 0.5) / (0.5 + 0.563)),
                        0.25 * log((2 * 0.25) / (0.25 + 0.4)),
                        0.625 * log((2 * 0.625) / (0.625 + 0.5)),
                        0.00001 * log((2 * 0.00001) / (0.00001 + 0.00001)),
                        0.00001 * log((2 * 0.00001) / (0.00001 + 0.00001)),
                        0.25 * log((2 * 0.25) / (0.25 + 0.00001))])

        answer_r = sum([0.35 * log((2 * 0.35) / (0.389 + 0.35)),
                        0.563 * log((2 * 0.563) / (0.5 + 0.563)),
                        0.4 * log((2 * 0.4) / (0.25 + 0.4)),
                        0.5 * log((2 * 0.5) / (0.625 + 0.5)),
                        0.00001 * log((2 * 0.00001) / (0.00001 + 0.00001)),
                        0.00001 * log((2 * 0.00001) / (0.00001 + 0.00001)),
                        0.00001 * log((2 * 0.00001) / (0.25 + 0.00001))])
        self.assertEqual(shannon.jensen_shannon(p=[0.389, 0.5, 0.25, 0.625, 0.0, 0.0, 0.25],
                                                q=[0.35, 0.563, 0.4, 0.5, 0.0, 0.0, 0.0]),
                         (1 / 2) * (answer_l + answer_r))

    def test_jensen_difference(self):
        answer = sum([
            (((0.389 * log(0.389)) + (0.35 * log(0.35))) / 2) - (((0.389 + 0.35) / 2) * log((0.389 + 0.35) / 2)),
            (((0.5 * log(0.5)) + (0.563 * log(0.563))) / 2) - (((0.5 + 0.563) / 2) * log((0.5 + 0.563) / 2)),
            (((0.25 * log(0.25)) + (0.4 * log(0.4))) / 2) - (((0.25 + 0.4) / 2) * log((0.25 + 0.4) / 2)),
            (((0.625 * log(0.625)) + (0.5 * log(0.5))) / 2) - (((0.625 + 0.5) / 2) * log((0.625 + 0.5) / 2)),
            (((0.00001 * log(0.00001)) + (0.00001 * log(0.00001))) / 2) - (((0.00001 + 0.00001) / 2) * log(
                (0.00001 + 0.00001) / 2)),
            (((0.00001 * log(0.00001)) + (0.00001 * log(0.00001))) / 2) - (((0.00001 + 0.00001) / 2) * log(
                (0.00001 + 0.00001) / 2)),
            (((0.25 * log(0.25)) + (0.00001 * log(0.00001))) / 2) - (((0.25 + 0.00001) / 2) * log(
                (0.25 + 0.00001) / 2)),
        ])
        self.assertEqual(shannon.jensen_difference(p=[0.389, 0.5, 0.25, 0.625, 0.0, 0.0, 0.25],
                                                   q=[0.35, 0.563, 0.4, 0.5, 0.0, 0.0, 0.0]),
                         answer)