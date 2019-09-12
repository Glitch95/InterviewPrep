class MinStack:
    """ The idea is to save the a history of the mins,
    to cicumvent having to recompute the min every time
    we pop an element from the stack. """

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        curr_min = self.stack[-1][1] if self.stack else x
        if curr_min > x:
            curr_min = x
        self.stack.append((x, curr_min))
        

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        return None

    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        return None

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
