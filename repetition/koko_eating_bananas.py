import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        min_p_per_h = r
        while l <= r:
            mid = (l + r) // 2
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / mid)
            if hours <= h:
                min_p_per_h = mid
                r = mid - 1
            else:
                l = mid + 1
        return min_p_per_h


Test = Solution()
print(Test.minEatingSpeed(piles=[3, 6, 7, 11], h=8))
