class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # Compute the failure function
        failure = [0] * len(needle)
        i = 1
        j = 0
        while i < len(needle):
            if needle[i] == needle[j]:
                failure[i] = j + 1
                i += 1
                j += 1
            elif j > 0:
                j = failure[j - 1]
            else:
                failure[i] = 0
                i += 1


s = Solution()
r = s.strStr("aabaaabaaac", "aabaaac")
print(r)