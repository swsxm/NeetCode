from typing import List
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_piles = max(piles)
        l, r = 1, max_piles 
        min_rate = max_piles 
        while l <= r:
            mid = (r+l)//2
            count = 0
            for i in range(0, len(piles)):
                count += math.ceil(piles[i] / mid)
            if count > h:
                l = mid + 1
            else:
                min_rate = mid
                r = mid - 1
        return min_rate

Test = Solution()
print(Test.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
          
