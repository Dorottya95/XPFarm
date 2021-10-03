import unittest as test
from main import is_triangle


class TestString(test.TestCase):
    def basic_test_cases(self):
        self.assertEqual(is_triangle(1, 2, 2), True)
        self.assertEqual(is_triangle(7, 2, 2), False)
        self.assertEqual(is_triangle(1, 2, 3), False)
        self.assertEqual(is_triangle(1, 3, 2), False)
        self.assertEqual(is_triangle(3, 1, 2), False)
        self.assertEqual(is_triangle(5, 1, 2), False)
        self.assertEqual(is_triangle(1, 2, 5), False)
        self.assertEqual(is_triangle(2, 5, 1), False)
        self.assertEqual(is_triangle(4, 2, 3), True)
        self.assertEqual(is_triangle(5, 1, 5), True)
        self.assertEqual(is_triangle(2, 2, 2), True)
        self.assertEqual(is_triangle(-1, 2, 3), False)
        self.assertEqual(is_triangle(1, -2, 3), False)
        self.assertEqual(is_triangle(1, 2, -3), False)
        self.assertEqual(is_triangle(0, 2, 3), False)


if __name__ == '__main__':
    test.main()