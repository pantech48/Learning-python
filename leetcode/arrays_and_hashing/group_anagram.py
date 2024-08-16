from collections import defaultdict
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    anagram_dict = {}
    for index, word in enumerate(strs):
        sorted_word = str(sorted(word))
        if sorted_word not in anagram_dict:
            anagram_dict[sorted_word] = [word]
        else:
            anagram_dict[sorted_word].append(word)

    return list(anagram_dict.values())

def groupAnagrams2(strs: List[str]) -> List[List[str]]:
    ans = defaultdict(list)

    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return ans.values()

print(groupAnagrams(["act","pots","tops","cat","stop","hat"]))
print(groupAnagrams2(["act","pots","tops","cat","stop","hat"]))