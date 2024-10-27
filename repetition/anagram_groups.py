from typing import List
class Solution:
    def groupAnagrams1(self, strs: List[str]) -> List[List[str]]:
        # O(n * mlog(m))
        lookup = dict()

        for string in strs:
            sorted_str = "".join(sorted(string))
            if sorted_str not in lookup:
                lookup[sorted_str] = []
            lookup[sorted_str].append(string)

        return list(lookup.values())
        
    def groupAnagrams2(self, strs: List[str]) -> List[List[str]]:
        # O(n * m)
        lookup = dict()
         
        for string in strs:
            count = [0] * 26
            for char in string:
                count[ord(char) - ord('a')] += 1
            count_tuple = tuple(count)
            if count_tuple not in lookup:
                lookup[count_tuple] = []
            lookup[count_tuple].append(string)
        return list(lookup.values())
            

Test = Solution()
input = ["act","pots","tops","cat","stop","hat"]
print(Test.groupAnagrams(input))
