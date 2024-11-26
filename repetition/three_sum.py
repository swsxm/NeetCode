from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()

        for index, current_num in enumerate(nums):
            if index > 0 and current_num == nums[index - 1]:
                continue

            left, right = index + 1, len(nums) - 1
            while left < right:
                total_sum = current_num + nums[left] + nums[right]
                if total_sum > 0:
                    right -= 1
                elif total_sum < 0:
                    left += 1
                else:
                    results.append([current_num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        return results
