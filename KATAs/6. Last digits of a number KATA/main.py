def solution(n, d):
    digit_list = list(map(int, str(n)))
    if d <= 0:
        return []
    else:
        return digit_list[-d:]
    pass

