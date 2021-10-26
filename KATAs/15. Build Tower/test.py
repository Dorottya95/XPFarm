import unittest as test
from main import validate_param


class TestString(test.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(validate_param(2), True)




if __name__ == '__main__':
    test.main()


