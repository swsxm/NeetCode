class MinStack:
    def __init__(self):
        self.stack = []        
        self.min_stack = []
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.min_stack[-1] or len(self.min_stack) == 0:
            self.min_stack.append(val)
        else:
            self.min_stack.append(self.min_stack[-1])
    def pop(self) -> None:
        self.stack.pop() 
        self.min_stack.pop()
    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        return 0
    def getMin(self) -> int:
        if len(self.min_stack) > 0:
            return self.min_stack[-1]
        return 0
