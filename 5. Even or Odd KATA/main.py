def even_or_odd(number):
    if check_int(number):
        if number % 2 == 0:
            return "Even."
        else:
            return "Odd."
    else:
        return "Input is not integer."


def check_int(number):
    return isinstance(number, int)


