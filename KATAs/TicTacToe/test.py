import unittest
import main


class TestClass(unittest.TestCase):

    def test_initial_board_must_be_empty(self):
        """Check if initial board is empty"""
        self.assertEqual(main.create_initial_board(), {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '})

    def test_initial_board_not_be_empty(self):
        """Check if initial board is not empty"""
        self.assertNotEqual(main.create_initial_board(), {1: 'X', 2: 'X', 3: 'X', 4: 'X', 5: 'X', 6: 'X', 7: 'X', 8: 'X', 9: 'X'})

    def test_initial_board_display(self):
        """Check if displayed board is formatted"""
        initial_board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
        output_board = """
     | | 
    -+-+-
     | | 
    -+-+-
     | | """
        self.assertEqual(output_board, main.display_board(initial_board))

    def test_handle_turn(self):
        """Test handle turn function"""
        board = {1: ' ', 2: ' ', 3: ' ', 4: ' ', 5: ' ', 6: ' ', 7: ' ', 8: ' ', 9: ' '}
        output_board = """
     |X| 
    -+-+-
     | | 
    -+-+-
     | | """
        self.assertEqual(output_board, main.handle_turn(2, board, "X", list(board.keys())))


if __name__ == '__main__':
    unittest.main()