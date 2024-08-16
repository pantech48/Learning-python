from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    for i, num in enumerate(nums):
        second_num = target - num
        if second_num in nums[i+1:]:
            if num == second_num:
                first_index = i
                second_index = nums[i + 1:].index(second_num) + len(nums[:i + 1])
                return [first_index, second_index]
            return [i, nums.index(second_num)]


print(twoSum([-1,-2,-3,-4,-5], -8))
