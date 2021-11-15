def create_initial_board():
    return {k: v for k, v in zip(list(range(1, 10)), list("X" * 9))}