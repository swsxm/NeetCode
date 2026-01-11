from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(start, current_subset):
            res.append(list(current_subset))
            
            for i in range(start, len(nums)):
                dfs(i + 1, current_subset + [nums[i]])

        dfs(0, [])
        return res