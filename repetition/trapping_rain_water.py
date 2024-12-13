from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        trapped = 0
        left_max = height[l]
        right_max = height[r]
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                trapped += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                trapped += right_max - height[r]
                r -= 1
        return trapped
