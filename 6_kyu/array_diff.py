def array_diff(a, b):
    for b_number in b:
        [a.remove(b_number) for count in range(a.count(b_number))]
    return a

print(array_diff([1,2,2], [2]))
