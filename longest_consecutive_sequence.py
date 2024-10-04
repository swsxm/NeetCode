from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        ret = 0
        for num in nums:
            if num - 1 not in nums_set:
                i = num
                consec = 0
                while i in nums_set:
                    consec+=1
                    i+=1
                ret = max(ret, consec)
        return ret

Test = Solution() 
print(Test.longestConsecutive([2,20,4,10,3,4,5]))
