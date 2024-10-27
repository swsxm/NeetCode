from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # O(n * mlog(m))
        lookup = dict()
        
        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in lookup:
                lookup[sorted_str] = []
            lookup[sorted_str].append(string)

        return list(lookup.values())
            

Test = Solution()
input = ["act","pots","tops","cat","stop","hat"]
print(Test.groupAnagrams(input))
