import unittest
import main


class TestClass(unittest.TestCase):

    def test_initial_board_must_be_empty(self):
        """Check if initial board is empty"""
        self.assertEqual(main.create_initial_board(), {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})


if __name__ == '__main__':
    unittest.main()