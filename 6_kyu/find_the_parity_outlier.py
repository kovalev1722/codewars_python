def find_outlier(integers):
    if integers[0] % 2 == 0 and integers[1] % 2 == 0 or integers[0] % 2 == 0 and integers[2] % 2 == 0 or integers[1] % 2 == 0 and integers[2] % 2 == 0:
        return list(filter(lambda number: number % 2 != 0, integers))[0]
    return list(filter(lambda number: number % 2 == 0, integers))[0]


print(find_outlier( [9181910, 7630921, -8220790, -6847450, -3134162, -9321564, 8078240, 7178670, 8248896, -9170106, -724156, -9880704, -3816432, 2515290, -1888468, -3905158, -7923730, -2330278, 7018204, -3873230, 8554142, 5343928, 2873534, -5075294, -587938, 8754998, -873786, 9139176, 9974316, -3624842, 6681242, -8562630, 7484456, 590202, 3330404, -3454198, 2113312, -2457036, -4939348, 7257326, -9333964, 6198158, 2081638, -7709728, 2285164, -4796816]))
#Expected: 7630921
