import unittest
import HW4

class TestCube(unittest.TestCase):
    def test_one(self):
        self.assertEqual(HW4.name('Alex','Young'), "Alex Young")
        self.assertEqual(HW4.name('Bob', 'Bob'), "Bob Bob")
        self.assertEqual(HW4.name('1', '2'), "1 2")
    def test_two(self):
        self.assertEqual(HW4.name('h', 0), "Type Error")
        self.assertEqual(HW4.name(5.8, 'hi'), "Type Error")
        self.assertEqual(HW4.name([5, -5], 'no'), "Type Error")
    def test_three(self):
        self.assertEqual(HW4.name('CS', '362'), "CS 362")
        self.assertEqual(HW4.name('Hello', 'World'), "Hello World")
        self.assertEqual(HW4.name('five', '5'), "five 5")

if __name__ == '__main__':
    unittest.main(verbosity=2)