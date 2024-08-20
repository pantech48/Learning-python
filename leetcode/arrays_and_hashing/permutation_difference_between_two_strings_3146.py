class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        first_string_map = {key: value for value, key in enumerate(s)}

        result = 0

        for index, char in enumerate(t):
            result_num = abs(first_string_map[char] - index)
            result += result_num

        return result




