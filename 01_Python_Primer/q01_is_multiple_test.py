import unittest
from q01_is_multiple import is_multiple

class IsMultiple(unittest.TestCase):
    def test_if_n_lessthan_m(self):
        self.assertEqual(is_multiple(1,2), False)

    def test_if_m_equals_zero(self):
        self.assertEqual(is_multiple(0,0), False)

    def test_valid_case_1(self):
        self.assertEqual(is_multiple(4,1), True)
    
    def test_valid_case_2(self):
        self.assertEqual(is_multiple(4,2), True)

    def test_n_is_negative_and_valid(self):
        self.assertEqual(is_multiple(-4, 2), True)