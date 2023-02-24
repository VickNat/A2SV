class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        if self.isEmpty(self.minStack) or val <= self.minStack[-1]:
            self.minStack.append(val)
        
        self.stack.append(val)
            

    def pop(self) -> None:
        if self.isEmpty(self.stack):
            return None
        
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        
        self.stack.pop()

    def top(self) -> int:
        if self.isEmpty(self.stack):
            return None
        
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
    
    def isEmpty(self, stack):
        return len(stack) == 0
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()