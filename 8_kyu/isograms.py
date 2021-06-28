from collections import Counter

def is_isogram(string):
    if string == "":
        return True
    string = string.upper()
    return True if Counter(string).most_common()[0][1] == 1 else False

print(is_isogram("isIsogram"))