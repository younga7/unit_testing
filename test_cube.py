# CS362 test_cube
# Alex Young
# 2/2/2021
# Run this file using python3 test_cube.py
# This program holds funtions to unit test for the cube function in HW4

import unittest
import HW4

class TestCube(unittest.TestCase):
    def test_one(self):
        self.assertEqual(HW4.cube(5), 125)
        self.assertEqual(HW4.cube(-5), -125)
        self.assertEqual(HW4.cube(0), 0)
    def test_two(self):
        self.assertEqual(HW4.cube('h'), "Type Error")
        self.assertEqual(HW4.cube('five'), "Type Error")
        self.assertEqual(HW4.cube([5, -5]), "Type Error")
    def test_three(self):
        self.assertEqual(HW4.cube(complex(0,1)), 0-1j)
        self.assertEqual(HW4.cube(complex(3,5)), -198+10j)
        self.assertEqual(HW4.cube(complex(3,-5)), -198-10j)

if __name__ == '__main__':
    unittest.main(verbosity=2)