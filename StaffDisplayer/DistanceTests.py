import unittest
from StaffDisplayer import DisplayStaff
import math


class MyTestCase(unittest.TestCase):

    def test_distance_1(self):
        dist = DisplayStaff.calc_distance(-41.2920728, 174.7748162, -41.337468696878226, 174.74167418422815)
        self.assertTrue(math.fabs(int(dist) - 5757) < 10)


if __name__ == '__main__':
    unittest.main()
