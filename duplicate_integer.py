from typing import List
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        cache = set()
        for num in nums:
            if num in cache:
                return True
            cache.add(num)
        return False

Test = Solution()
print(Test.hasDuplicate([1, 2, 3, 3]))

