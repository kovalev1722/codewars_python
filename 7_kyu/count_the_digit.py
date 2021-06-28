def nb_dig(n, d):
    lst = [number**2 for number in range(n + 1)]
    return ''.join(list(map(str, lst))).count(str(d))

print(nb_dig(25, 1))