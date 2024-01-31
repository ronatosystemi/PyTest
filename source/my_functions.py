def add(i, j):
    return i + j


def divide(i, j):
    if j == 0:
        raise ValueError
    return i / j


print(add(1, 2))