from typing import List


# nums = [-1,0,3,5,9,12], target = 9
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        mid = len(nums) // 2
        end = len(nums)
        prev_mid = -1
        while prev_mid != mid:
            mid_value = nums[mid]
            if mid_value == target:
                return mid
            elif mid_value < target:
                start = mid
                prev_mid = mid
                mid = (start + end) // 2
            elif mid_value > target:
                prev_mid = mid
                end = mid
                mid = end // 2
        return -1
# nums = [-1,0,3,5,9,12], target = 5
    def search_optimized(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) // 2
            mid_value = nums[mid]

            if mid_value == target:
                return mid
            elif mid_value < target:
                start = mid + 1
            else:  # mid_value > target
                end = mid - 1

        return -1

s = Solution()
print(s.search(nums = [-1,0,3,5,9,12], target = 3))
