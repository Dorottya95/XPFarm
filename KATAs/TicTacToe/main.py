import time
import random


def create_initial_board():
    return {k: v for k, v in zip(list(range(1, 10)), list(" " * 9))}


def display_board(initial_board):
    board_template = """
    {}|{}|{}
    -+-+-
    {}|{}|{}
    -+-+-
    {}|{}|{}"""
    return board_template.format(*initial_board.values())


def handle_turn(position, initial_board, player, free_position_list):
    if position in free_position_list:
        initial_board[position] = player
        free_position_list.remove(position)
        time.sleep(2)
        print(display_board(initial_board))
        return display_board(initial_board)


def check_win_col(board, player):
    if (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[3] == player and board[6] == player and board[9] == player):
        return str(player) + " won"
    else:
        return False


def check_win_row(board, player):
    if (board[1] == player and board[2] == player and board[3] == player) or \
            (board[4] == player and board[5] == player and board[6] == player) or \
            (board[7] == player and board[8] == player and board[9] == player):
        return str(player) + " won"
    else:
        return False


def check_win_diagonal(board, player):
    if (board[1] == player and board[5] == player and board[9] == player) or \
            (board[3] == player and board[5] == player and board[7] == player):
        return str(player) + " won"
    else:
        return False


def playing():
    board = create_initial_board()
    free_position_list = list(board.keys())
    while len(free_position_list) > 1:
        if check_win_col(board, "X") or check_win_col(board, "O") or \
            check_win_row(board, "X") or check_win_row(board, "O") or \
            check_win_diagonal(board, "X") or check_win_diagonal(board, "O"):
            print("O won")
            return "O won"
        handle_turn(random.choice(free_position_list), board, "X", free_position_list)
        if check_win_col(board, "X") or check_win_col(board, "O") or \
                check_win_row(board, "X") or check_win_row(board, "O") or \
                check_win_diagonal(board, "X") or check_win_diagonal(board, "O"):
            print("X won")
            return "X won"
        handle_turn(random.choice(free_position_list), board, "O", free_position_list)
    else:
        handle_turn(random.choice(free_position_list), board, "X", free_position_list)
        if check_win_col(board, "X") or check_win_col(board, "O") or \
                check_win_row(board, "X") or check_win_row(board, "O") or \
                check_win_diagonal(board, "X") or check_win_diagonal(board, "O"):
            print("X won")
            return "X won"
        else:
            print("Draw")
            return "Draw"


if __name__ == '__main__':
    playing()

