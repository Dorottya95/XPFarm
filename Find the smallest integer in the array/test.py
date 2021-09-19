import unittest as test
from main import find_smallest_int


class TestString(test.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(find_smallest_int([1, 2, 3]), 1)
        self.assertEqual(find_smallest_int([1, 2, 3, -2]), -2)
        self.assertEqual(find_smallest_int([1, 2, 3*(-2), -2]), 3*(-2))

if __name__ == '__main__':
    test.main()

'''
import codewars_test as test

# for backward compatibility
try:
    from solution import findSmallestInt as find_smallest_int
except ImportError:
    from solution import find_smallest_int

@test.describe("Fixed Tests")
def basic_tests():
    @test.it('Basic Test Cases')
    def basic_test_cases():
        test.assert_equals(find_smallest_int([78, 56, 232, 12, 11, 43]), 11)
        test.assert_equals(find_smallest_int([78, 56, -2, 12, 8, -33]), -33)
        test.assert_equals(find_smallest_int([0, 1-2**64, 2**64]), 1-2**64)
'''