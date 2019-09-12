class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []
    
    def _reverse(self):
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def push(self, x):
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)
        
    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        """
        self._reverse()
        return self.out_stack.pop()       

    def peek(self):
        """
        Get the front element.
        """
        self._reverse()
        return self.out_stack[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        """
        self._reverse()
        return not self.out_stack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

