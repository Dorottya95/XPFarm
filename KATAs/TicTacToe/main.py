import time


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
    return True