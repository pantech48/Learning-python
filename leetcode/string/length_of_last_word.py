class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = len(s) - 1
        count = 0
        while idx >= 0:
            if s[idx].isalpha():
                count += 1
            if count and s[idx] == " ":
                return count
            idx -= 1
        return count
