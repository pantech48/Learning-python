from typing import List

# [0,0,1,1,1,2,2,3,3,4]
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        # Указатель для уникальных элементов
        k = 1

        # Проходим по массиву начиная со второго элемента
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k

s = Solution()
s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])