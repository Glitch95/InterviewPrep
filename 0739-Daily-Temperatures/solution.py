class Solution:
    def dailyTemperatures(self, T):
        # We can use a stack to solve this problem in O(n) time.
        # The idea is we traverse through the list, adding the index
        # of elements to a stack.
        # If the current element in the list is larger
        # than the element at the top of the stack we pop elements
        # from the stack and update their result until the top
        # of the stack has an element greater than or equal to the 
        # current element.
        
        n = len(T)
        stack, result = [], [0] * n
        
        for i in range(n):
            while stack and T[stack[-1]] < T[i]:
                res_index = stack.pop()
                result[res_index] = i - res_index
            
            stack.append(i)
            
        return result

