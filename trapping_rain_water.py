from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height)-1
        water = 0

        while l < r:
            min_element = min(height[l], height[r])
            while l < r and min_element >= height[l]:
                water += min_element - height[l]
                l+=1
            while l < r and min_element >= height[r]:
                water += min_element - height[r]
                r-=1
        return water

Test = Solution()       
print(Test.trap([0,2,0,3,1,0,1,3,2,1]))

        
