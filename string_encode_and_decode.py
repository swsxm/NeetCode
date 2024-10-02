from typing import List
class Solution:

    def encode(self, strs: List[str]) -> str:
        d_string = ""
        for word in strs:
            d_string += f"{len(word)}#{word}"
        return d_string
    def decode(self, s: str) -> List[str]:
        i = 0
        words = []
        while i < len(s):
            w_len_str = ""
            while i < len(s) and s[i].isdigit():
                w_len_str += s[i]
                i += 1
            w_len = int(w_len_str)
            i+=1
            word = s[i:i+w_len]
            words.append(word)
            i+= w_len
        return words


Test = Solution()
input = ["hiii"]
output = Test.encode(input)
print(Test.decode(output))

