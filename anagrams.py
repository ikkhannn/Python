from collections import Counter

def anagram(first, second):
    return Counter(first) == Counter(second)


print(anagram("abcd3", "3acdb")) # True