import unittest as test
from main import validate_param, tower_builder


class TestString(test.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(validate_param(2), True)




if __name__ == '__main__':
    test.main()


'''
    def test_basic_test_cases(self):
        self.assertEqual(tower_builder(1), ['*', ])
        
    def test_check_if_string(self):
        self.assertEqual(tower_builder(2), [' * ', '***'])

    def test_check_if_not_string(self):
        self.assertEqual(tower_builder(3), ['  *  ', ' *** ', '*****'])
'''