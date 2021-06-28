import collections

def anagrams(word, words):
    anagram = []
    for w in words:
        if collections.Counter(word) == collections.Counter(w):
            anagram.append(w)
    return anagram
    #your code here

print(anagrams('abba', ['aabb', 'abcd', 'bbaa', 'dada']))
