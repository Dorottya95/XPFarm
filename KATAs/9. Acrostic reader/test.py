import unittest as test
from main import read_out


class TestString(test.TestCase):
    def test_check_string(self):
        self.assertEqual(read_out(['Jolly', 'Amazing', 'Courteous', 'Keen']), "JACK")
        self.assertEqual(read_out(['Marvelous', 'Excellent', 'Gifted']), "MEG")
