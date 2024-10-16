from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        rectangle = 0
        for height in heights:
            print(stack)
            pop_count = 0
            pop_sum = 0
            while stack and height < stack[-1]:
                pop_sum += stack.pop()
                pop_count += 1
            rectangle = max(pop_sum, rectangle)
            while pop_count > 0:
                stack.append(height)
                pop_count-=1
            stack.append(height)
        print('----', stack)
        while stack:
            print(stack)
            last_el = stack.pop()
            pop_count = 1
            pop_sum = last_el
            while stack and last_el == stack[-1]:
                pop_sum += stack.pop()
                pop_count += 1
            rectangle = max(pop_sum, rectangle)
            while stack and pop_count > 0:
                stack.append(stack[-1])
                pop_count-=1
        return rectangle

Test = Solution()
print(Test.largestRectangleArea(heights = [2,1,5,6,2,3]))


        
