from typing import List

# [5,25,75], 100
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while True:
            summ = numbers[l] + numbers[r]
            if summ == target:
                return [l + 1, r + 1]
            if summ > target:
                r -= 1
            else:
                l += 1


s = Solution()
result = s.twoSum([3,24,50,79,88,150,345], 200)
print(result)