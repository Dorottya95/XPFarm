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

    def test_check_win_col(self):
        """Check if a player wins with a column of same marks"""
        board = {1: 'X', 2: ' ', 3: ' ', 4: 'X', 5: ' ', 6: ' ', 7: 'X', 8: ' ', 9: ' '}
        self.assertEqual(main.check_win_col(board, "X"), "X won")
        board = {1: 'O', 2: ' ', 3: ' ', 4: 'O', 5: ' ', 6: ' ', 7: 'O', 8: ' ', 9: ' '}
        self.assertEqual(main.check_win_col(board, "O"), "O won")

    def test_check_not_win_col(self):
        """Check if no player wins with a column of same marks"""
        board = {1: ' ', 2: ' ', 3: ' ', 4: 'X', 5: ' ', 6: ' ', 7: 'X', 8: ' ', 9: ' '}
        self.assertEqual(main.check_win_col(board, "X"), False)
        board = {1: ' ', 2: 'O', 3: ' ', 4: 'X', 5: ' ', 6: ' ', 7: 'X', 8: ' ', 9: ' '}
        self.assertEqual(main.check_win_col(board, "O"), False)

    def test_check_win_row(self):
        """Check if a player wins with a row of same marks"""
        board = {1: 'X', 2: 'X', 3: 'X', 4: 'O', 5: ' ', 6: ' ', 7: 'O', 8: ' ', 9: ' '}
        self.assertEqual(main.check_win_row(board, "X"), "X won")
        board = {1: 'O', 2: 'O', 3: 'O', 4: 'X', 5: ' ', 6: ' ', 7: 'X', 8: ' ', 9: ' '}
        self.assertEqual(main.check_win_row(board, "O"), "O won")

    def test_check_not_win_row(self):
        """Check if no player wins with a row of same marks"""
        board = {1: 'O', 2: 'O', 3: ' ', 4: 'X', 5: ' ', 6: ' ', 7: 'X', 8: ' ', 9: ' '}
        self.assertEqual(main.check_win_row(board, "X"), False)
        board = {1: 'O', 2: 'O', 3: ' ', 4: 'X', 5: ' ', 6: ' ', 7: 'X', 8: ' ', 9: ' '}
        self.assertEqual(main.check_win_row(board, "O"), False)

    def test_check_win_diagonal(self):
        """Check if  aplayer wins with a diagonal of same marks"""
        board = {1: 'X', 2: 'O', 3: ' ', 4: 'X', 5: 'X', 6: ' ', 7: 'O', 8: 'O', 9: 'X'}
        self.assertEqual(main.check_win_diagonal(board, "X"), "X won")
        board = {1: 'O', 2: 'X', 3: ' ', 4: ' ', 5: 'O', 6: ' ', 7: 'X', 8: 'X', 9: 'O'}
        self.assertEqual(main.check_win_diagonal(board, "O"), "O won")


if __name__ == '__main__':
    unittest.main()