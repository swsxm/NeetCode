class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        paren = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        for char in s:
            if char in paren:
                stack.append(paren[char])
                continue
            if len(stack) <= 0 or char != stack[-1]:
                return False
            stack.pop()
        return len(stack) == 0

Test = Solution()
print(Test.isValid(s = "({[]})"))

