def is_triangle(a, b, c):
    if a == 0 or b == 0 or c == 0 or a + b < c:
        return False
    else:
        return True


is_triangle(1, 2, 2)