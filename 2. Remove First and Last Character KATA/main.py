def remove_char(s):
    if check_string(s):
        return print(s[1:-1])


def check_string(s):
    return isinstance(s, str)
