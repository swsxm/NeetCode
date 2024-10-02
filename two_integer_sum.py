from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = dict()
        for i in range(len(nums)):
            cor_value = target - nums[i]
            if cor_value in hashmap.keys():
                return [hashmap[cor_value], i] 
            else:
                hashmap[nums[i]] = i
        return [] 

Test = Solution()
print(Test.twoSum(nums = [4,5,6], target = 10))
