import unittest as test
from main import check_string, remove_duplicates


class TestString(test.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(check_string("string", "string2"), True)
    def test_basic_test_cases(self):
        self.assertEqual(remove_duplicates("sttttriiing", "string"), ["string", "string"])


if __name__ == '__main__':
    test.main()