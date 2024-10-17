from typing import List
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            distance = r - l
            min_height = min(heights[l], heights[r])
            area = max(distance * min_height, area)
            if heights[l] < heights[r]:
                l+=1 
            else:
                r-=1 
        return area

Test = Solution()
print(Test.maxArea(heights =[1,500,500,6] ))
        
