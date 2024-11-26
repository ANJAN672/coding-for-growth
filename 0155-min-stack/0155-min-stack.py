class MinStack:

    def __init__(self):
        self.stack=[]
        self.min_stack=[]
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack or val<=self.min_stack[-1]:
            self.min_stack.append(val)
    
    def pop(self) -> None:
        popped=self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1] if self.stack else None

    def getMin(self) -> int:
        return min(self.stack) if self.min_stack else None
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()