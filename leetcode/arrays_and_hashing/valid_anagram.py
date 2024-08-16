def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    anagram_dict = {}
    for letter in s:
        if letter not in anagram_dict.keys():
            anagram_dict[letter] = 1
        else:
            anagram_dict[letter] += 1

    for letter in t:
        if letter in anagram_dict.keys() and anagram_dict.get(letter) > 0:
            anagram_dict[letter] -= 1
        else:
            return False
    return True