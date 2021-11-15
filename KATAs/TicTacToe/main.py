def create_initial_board():
    return {k: v for k, v in zip(list(range(1, 10)), list(" " * 9))}


def display_board(initial_board):
    return initial_board