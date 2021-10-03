import unittest as test
from main import add


class TestString(test.TestCase):
    def test_add(self):
        self.assert_equals(add(2)(5), 7)
