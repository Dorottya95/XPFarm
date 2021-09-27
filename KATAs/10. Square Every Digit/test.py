import unittest as test
from main import square_digits


class TestString(test.TestCase):
    def test_check_square(self):
        self.assertEqual(square_digits(9119), 811181)
        self.assertEqual(square_digits(0), 0)