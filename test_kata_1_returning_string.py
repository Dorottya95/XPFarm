import unittest as test
from kata_1_returning_string import greet


class TestString(test.TestCase):
    def basic_test_cases():
        test.assert_equals(greet('Ryan'), "Hello, Ryan how are you doing today?")
        test.assert_equals(greet('Shingles'), "Hello, Shingles how are you doing today?")

if __name__ == '__main__':
    test.main()