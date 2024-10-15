from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [0]
        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                j = stack.pop()
                res[j] = i-j
            stack.append(i)

            
        return res

Test = Solution()
print(Test.dailyTemperatures(temperatures = [30,38,30,36,35,40,28]))

        
