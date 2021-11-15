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