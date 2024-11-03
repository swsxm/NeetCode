from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += f"{len(s)}#{s}"
        return string
    def decode(self, s: str) -> List[str]:
        strs = []
        start = 0
        while start < len(s):
            number = ""
            while s[start] != "#":
                number += s[start]
                start+=1
            start += 1
            string = ""
            for _ in range(int(number)):
                string+=s[start]
                start+=1
            strs.append(string)
        return strs



Test = Solution()
print(Test.decode(Test.encode(["hallo", "i", "bins"])))
