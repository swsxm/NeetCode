class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {"(": ")", "{": "}", "[": "]"}
        stack = []
        for p in s:
            if p in open_to_close:
                stack.append(open_to_close[p])
            else:
                if len(stack) == 0 or stack[-1] != p:
                    return False
                stack.pop()
        return len(stack) == 0
