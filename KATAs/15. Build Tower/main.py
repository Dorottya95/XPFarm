def validate_param(floor_number):
    if int(floor_number):
        return floor_number


def tower_builder(floor_number):
    return '\n'.join([int(n - 1) * ' ' + (2 * i - 1) * '*' + int(n - 1) * ' ' for i, n in zip(range(1, floor_number + 1), reversed(range(floor_number + 1)))])

