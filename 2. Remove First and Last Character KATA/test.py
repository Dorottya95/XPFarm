import unittest as test
from main import remove_char, check_string


class TestString(test.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(remove_char('test'), 'es')
        self.assertEqual(remove_char('long test'), 'ong tes')

    def test_check_if_string(self):
        self.assertEqual(check_string('test'), True)

    def test_check_if_not_string(self):
        self.assertEqual(check_string(33), False)


if __name__ == '__main__':
    test.main()