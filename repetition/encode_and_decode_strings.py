class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}_{s}"
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_str_list = []
        left = 0
        number = ""
        while left < len(s):
            numbers = "0123456789"
            if s[left] in numbers:
                number += s[left]
                left += 1
            else:
                left += 1
                length = int(number)
                decoded_str_list.append(s[left : left + length])
                left += length
                number = ""
        return decoded_str_list
