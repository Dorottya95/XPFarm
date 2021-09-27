def square_digits(num):
    squares = []
    for digit in [int(d) for d in str(num)]:
        digit = digit ** 2
        squares.append(digit)
    return int("".join(map(str, squares)))