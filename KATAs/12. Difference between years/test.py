import unittest as test
from main import how_many_years


class TestString(test.TestCase):
    def test_basic_test_cases(self):
        self.assertEqual(how_many_years('1997/10/10', '2015/10/10'), 18)
        self.assertEqual(how_many_years('1990/10/10', '2015/10/10'), 25)
        self.assertEqual(how_many_years('2015/10/10', '1990/10/10'), 25)
        self.assertEqual(how_many_years('1992/10/24', '2015/10/24'), 23)
        self.assertEqual(how_many_years('2018/10/10', '2000/10/10'), 18)


if __name__ == '__main__':
    test.main()
