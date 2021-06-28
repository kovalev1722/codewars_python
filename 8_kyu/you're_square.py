def is_square(n):
    if n == 0:
        return True
    elif n%(n**0.5) == 0:
        return True
    return False

print(is_square(-1))