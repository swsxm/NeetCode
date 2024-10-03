from typing import List
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        postfix = [1] * len(nums)
        sol = []
        for i in range(1, len(nums)):
            prefix.append(nums[i-1] * prefix[i-1])
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = nums[i+1] * postfix[i+1]
        for i in range(len(nums)):
            sol.append(prefix[i] * postfix[i])
        return sol

Test = Solution()
print(Test.productExceptSelf(nums = [1,2,4,6]))




        
