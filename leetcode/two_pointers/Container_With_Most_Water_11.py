from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        f_p = 0
        s_p = len(height) - 1
        max_water = 0

        while f_p != s_p:
            current_water = min(height[f_p], height[s_p]) * (s_p - f_p)
            if current_water > max_water:
                max_water = current_water

            if height[f_p] < height[s_p]:
                f_p += 1
            else:
                s_p -= 1

        return max_water
