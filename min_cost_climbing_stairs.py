from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        lookup = {}
        def dfs(i):
            if i in lookup:
                return lookup[i]
            if i >= len(cost):
                return 0 
            res = min(dfs(i+1), dfs(i+2)) + cost[i]
            lookup[i] = res
            return res 
        return min(dfs(0), dfs(1))







        

