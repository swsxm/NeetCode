from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()
        for s in strs:
            arr = [0] * 26
            for char in s:
                arr_pos = ord('a') - ord(char)
                arr[arr_pos] += 1
            key = tuple(arr)
            hashmap[key] = hashmap.get(key, [])
            hashmap[key].append(s)
        return list(hashmap.values()) 
Test = Solution()
print(Test.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]))
