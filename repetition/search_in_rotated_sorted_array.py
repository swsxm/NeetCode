from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                if nums[mid] >= target >= nums[l]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1


Test = Solution()
print(Test.search([5, 1, 3], target=5))
