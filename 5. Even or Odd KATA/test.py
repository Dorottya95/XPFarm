import unittest as test
from main import even_or_odd, check_int


class TestString(test.TestCase):
    def test_check_even(self):
        self.assertEqual(even_or_odd(10), "Even.")

    def test_check_odd(self):
        self.assertEqual(even_or_odd(11), "Odd.")

    def test_check_if_int(self):
        self.assertEqual(check_int(5), True)

    def test_check_if_not_int(self):
        self.assertEqual(even_or_odd("5"), "Input is not integer.")