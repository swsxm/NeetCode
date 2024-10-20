from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_value = nums[0]

        while l <= r:
            mid = (l+r) // 2
            print(l, r, mid)
            min_value = min(min_value, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1

        return min_value

Test = Solution()
print(Test.findMin(nums=[4,5,6,7,0,1,2]))

