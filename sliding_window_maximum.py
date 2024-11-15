from typing import List
from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        vals = deque()
        output = []
        l, r = 0, 0
        while r < len(nums):
            while vals and nums[vals[-1]] <= nums[r]:
                vals.pop()
            vals.append(r)
            if l > vals[0]:
                vals.popleft()
            if r-l+1 >= k:
                output.append(nums[vals[0]])
                l+=1
            r+=1
        return output
