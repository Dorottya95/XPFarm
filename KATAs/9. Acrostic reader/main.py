def read_out(acrostic):
    letters = []
    for string in acrostic:
        letters.append(string[0])
    return ''.join(letters)
