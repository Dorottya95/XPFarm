import unittest as test
from main import validate_param, tower_builder


class TestString(test.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(validate_param(2), 2)
        self.assertEqual(tower_builder(1), '*')
        self.assertEqual(tower_builder(2), ' * ', '***')
        self.assertEqual(tower_builder(3), '  *  ', ' *** ', '*****')


if __name__ == '__main__':
    test.main()


