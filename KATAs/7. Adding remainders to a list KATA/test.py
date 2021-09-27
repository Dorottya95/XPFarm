import unittest as test
from main import solve


class TestInt(test.TestCase):
    def test_basic_test_case(self):
        self.assertEqual(solve([2, 4, 6, 8, 10, 12], 3), [4, 5, 6, 10, 11, 12])
        self.assertEqual(solve([1000, 999, 998, 997], 5), [1000, 1003, 1001, 999])
        self.assertEquals(solve([], 2), [])


if __name__ == '__main__':
    test.main()
