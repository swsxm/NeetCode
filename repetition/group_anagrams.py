from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        lookup = dict()
        for s in strs:
            char_count = [0] * 26
            for c in s:
                char_count[ord(c) - ord("a")] += 1
            char_count_tuple = tuple(char_count)
            if tuple(char_count) in lookup:
                lookup[char_count_tuple].append(s)
            else:
                lookup[char_count_tuple] = [s]
        return [value for value in lookup.values()]
