from collections import Counter

def duplicate_count(text):
    dic = list(Counter(text.upper()).values())
    return len(dic) - dic.count(1)

print(duplicate_count("abcdeaB"))