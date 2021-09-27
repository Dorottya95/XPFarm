import unittest as test
from main import generate_range


class TestString(test.TestCase):
    def test_step_two(self):
        self.assertEqual(generate_range(2, 12, 2), [2, 4, 6, 8, 10, 12])

    def test_step_two(self):
        self.assertEqual(generate_range(2, 12, 3), [2, 5, 8, 11])

    def test_negative_numbers(self):
        self.assertEqual(generate_range(-4, 12, 2), [-4, -2, 0, 2, 4, 6, 8, 10, 12])

    def test_step_bigger(self):
        self.assertEqual(generate_range(2, 6, 8), [2])


if __name__ == '__main__':
    test.main()