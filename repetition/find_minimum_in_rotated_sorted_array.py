from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                r = mid
            else:
                l = mid + 1
        return nums[l]


Test = Solution()
print(Test.findMin([4, 5, 0, 1, 2, 3]))
