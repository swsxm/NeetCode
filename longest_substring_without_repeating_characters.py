class Solution:
    def lengthOfLongestSubstring2(self, s: str) -> int:
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
    
    # O(n)
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        count = 0
        l = 0

        for i in range(0, len(s)):
            while s[i] in lookup:
                lookup.remove(s[l])
                l+=1
            lookup.add(s[i])
            count = max(count, i-l+1) 

        return count

Test = Solution()
print(Test.lengthOfLongestSubstring("abcabcbb"))
        
