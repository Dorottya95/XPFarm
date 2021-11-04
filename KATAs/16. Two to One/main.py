def check_string(a1, a2):
    return isinstance(a1, str) and isinstance(a2, str)


def remove_duplicates(a1, a2):
    input1 = ""
    input2 = ""
    for i in a1:
        if i in input1:
            pass
        else:
            input1 += i
    for j in a2:
        if j in input2:
            pass
        else:
            input2 += j
    inputs = [input1, input2]
    return inputs


def longest(a1, a2):
    return "".join(sorted(set(a1 + a2)))


