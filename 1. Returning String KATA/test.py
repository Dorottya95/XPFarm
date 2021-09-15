import unittest as test
from main import greet, check_string


class TestString(test.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(greet('Ryan'), "Hello, Ryan how are you doing today?")

    def test_check_if_string(self):
        self.assertEqual(check_string('string'), True)

    def test_check_if_not_string(self):
        self.assertEqual(check_string(5), False)


if __name__ == '__main__':
    test.main()
