class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # it would be better to directly initialize prefix and postfix with the size of n
        if not nums:
            return []
        prefix = [1]
        postfix = [1]
        start = 1
        for i in range(1, len(nums)):
            start = start * nums[i - 1]
            prefix.append(start)
        start = 1
        for i in range(len(nums) - 2, -1, -1):
            start = start * nums[i + 1]
            postfix.append(start)
        ret = []
        for i in range(len(nums)):
            value = 1
            value *= prefix[i]
            value *= postfix[len(nums) - i - 1]
            ret.append(value)
        return ret
