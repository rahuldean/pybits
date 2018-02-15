import unittest
from q02_is_even import is_even

class IsEven(unittest.TestCase):
    def test_number_is_even_1(self):
        self.assertEqual(is_even(2), True)

    def test_number_is_even_2(self):
        self.assertTrue(is_even(0))

    def test_number_is_even_3(self):
        self.assertFalse(is_even(1))

    def test_number_is_not_even_2(self):
        self.assertFalse(is_even(-1))
