class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # O(n**2)
        if len(s) == 1:
            return 1
        lookup = set()
        max_count = 0
        for i in range(0, len(s)):
            lookup.add(s[i])
            for k in range(i+1, len(s)):
                if s[k] not in lookup:
                    lookup.add(s[k])
                else:
                    break
            max_count = max(max_count, len(lookup))
            lookup.clear()

        return max_count

Test = Solution()
print(Test.lengthOfLongestSubstring(s="zyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcbaZYXWVUTSRQPONMLKJIHGFEDCBA"))

        
