from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 
        while l < r:
            sum_ = numbers[l] + numbers[r]
            if sum_ < target:
                l+=1
            elif sum_ > target:
                r-=1
            else:
                return [l+1, r+1]
        return [-1]

Test = Solution()
print(Test.twoSum([1, 2, 3, 4], 3))
