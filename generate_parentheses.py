from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parens = []
        paren = ['(']
        
        def backtrack(open_b, closed_b):
            print(paren)
            if open_b == closed_b == n:
                parens.append("".join(paren))
                return
            if open_b < n:  
                paren.append('(')
                backtrack(open_b+1, closed_b)
                paren.pop()
            if closed_b < open_b:
                paren.append(")")
                backtrack(open_b, closed_b+1)
                paren.pop()

        backtrack(1, 0)

        return parens

Test = Solution()
print(Test.generateParenthesis(3))
        
