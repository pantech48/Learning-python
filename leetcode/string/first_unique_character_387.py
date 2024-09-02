from collections import Counter

# "loveleetcode"
class Solution:
    def firstUniqChar(self, s: str) -> int:
        print(Counter(s), )
        hash_map = {}
        for char in s:
            if char not in hash_map:
                hash_map[char] = 1
            else:
                hash_map[char] += 1

        for idx, char in enumerate(s):
            if hash_map[char] == 1:
                return idx

        return -1

s = Solution()
s.firstUniqChar('adsfsdsdg')