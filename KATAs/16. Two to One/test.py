import unittest as test
from main import longest


class TestString(test.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(longest("string", "string2"), True)
    def test_basic_test_cases(self):
        self.assertEqual(longest("sttttriiing", "string"), "string", "string")


if __name__ == '__main__':
    test.main()