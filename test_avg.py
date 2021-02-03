# CS362 test_avg
# Alex Young
# 2/2/2021
# Run this file using python3 test_avg.py
# This program holds funtions to unit test for the avg function in HW4

import unittest
import HW4

class TestCube(unittest.TestCase):
    def test_one(self):
        self.assertEqual(HW4.avg([]), "Zero Division")
        self.assertEqual(HW4.avg([-5]), -5)
        self.assertEqual(HW4.avg(0), "Type Error")
    def test_two(self):
        self.assertEqual(HW4.avg('five'), "Type Error")
        self.assertEqual(HW4.avg([5]), 5)
        self.assertEqual(HW4.avg('0'), "Type Error")
    def test_three(self):
        self.assertEqual(HW4.avg([1,3]), 2)
        self.assertEqual(HW4.avg([3,5,7]), 5)
        self.assertEqual(HW4.avg([-3,-7,-5]), -5)

if __name__ == '__main__':
    unittest.main(verbosity=2)