import unittest
import HW4
import cmath

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