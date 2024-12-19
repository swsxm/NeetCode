from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0

        stack = []
        heights.append(0)
        largest = 0
        i = 0

        while i < len(heights):
            if not stack or heights[i] >= heights[stack[-1]]:
                stack.append(i)
                i += 1
            else:
                top = stack.pop()
                height = heights[top]
                width = i if not stack else i - stack[-1] - 1
                largest = max(largest, height * width)

        return largest


Test = Solution()
print(Test.largestRectangleArea(heights=[7, 1, 7, 2, 2, 4]))  # Expected output: 8
