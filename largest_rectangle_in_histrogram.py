from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        rectangle = 0
        stack = []
        for i, height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > height:
                index_of_prev, height_of_prev = stack.pop()
                rectangle = max(rectangle, height_of_prev * (i - index_of_prev))
                start = index_of_prev  
            stack.append((start, height))  
        
        for index_of_prev, height_of_prev in stack:
            rectangle = max(rectangle, height_of_prev * (len(heights) - index_of_prev))
        
        return rectangle

Test = Solution()
print(Test.largestRectangleArea(heights = [7, 1, 7, 2, 2, 4]))  # Erwartetes Ergebnis: 10

        
