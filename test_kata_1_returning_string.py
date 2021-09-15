import unittest as test
from kata_1_returning_string import greet, check_string


class TestString(test.TestCase):
    def basic_test_cases():
        test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
        test.assert_equals(greet('Shingles'), "Hello, Shingles how are you doing today?")
    def check_if_string(self):
        self.assertEqual(check_string('string'), True)

if __name__ == '__main__':
    test.main()