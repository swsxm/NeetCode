class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                day_index = stack.pop()
                output[day_index] = i - day_index
            stack.append(i)
        while stack:
            output[stack.pop()] = 0
        return output
