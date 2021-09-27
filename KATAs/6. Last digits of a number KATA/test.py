import unittest as test
from main import solution


class TestInt(test.TestCase):
    def test_basic_test_case(self):
        self.assertEqual(solution(123, 2), [2, 3])

    def test_check_if_D_zero(self):
        self.assertEqual(solution(123, 0), [])

    def test_check_if_D_bigger(self):
        self.assertEqual(solution(123, 5), [1, 2, 3])


if __name__ == '__main__':
    test.main()
