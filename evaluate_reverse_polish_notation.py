
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token.lstrip('-').isdigit():  
                stack.append(int(token))
            else:
                num2 = stack.pop()  
                num1 = stack.pop()  
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    stack.append(int(num1 / num2))
        return stack[0]

# Test the function
Test = Solution()
input = ["1", "2", "+", "3", "*", "4", "-"]
print(Test.evalRPN(input))

