import re

def solve(s):
    #######print(re.split('[aeiou]+', s))
    vowels_ascii = [ord(char) - 96 for char in "aeiou"]
    s_ascii = [ord(char) - 96 for char in s]
    counter = 0
    sum_of_chars = []
    for char in s_ascii:
        if char not in  vowels_ascii:
            counter += char
        else:
            sum_of_chars.append(counter)
            counter = 0
    return max(sum_of_chars)

print(solve("zodiacs"))