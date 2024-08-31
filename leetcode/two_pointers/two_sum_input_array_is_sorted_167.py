from typing import List


# [2,3,4], 6
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        idx = 1
        hash_map = {numbers[0] : 0}
        while idx < len(numbers):
            diff = target - numbers[idx]
            if diff in hash_map:
                return [hash_map[diff] + 1, idx + 1]
            hash_map[numbers[idx]] = idx
            idx += 1



