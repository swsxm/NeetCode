class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        count = 1
        nums_lookup = set(nums)
        for num in nums:
            count_sequence = num
            while count_sequence in nums_lookup:
                count_sequence += 1
            count = max(count, count_sequence - num)
        return count
