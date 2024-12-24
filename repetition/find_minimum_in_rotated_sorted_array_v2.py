from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = nums[0]
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] <= nums[r]:
                min_num = min(min_num, nums[mid])
                r = mid - 1
            else:
                min_num = min(min_num, nums[r])
                l = mid + 1
        return min_num


Test = Solution()
print(Test.findMin([4, 5, 0, 1, 2, 3]))
