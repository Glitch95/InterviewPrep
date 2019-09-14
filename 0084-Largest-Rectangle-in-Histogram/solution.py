class Solution:
    def largestRectangleArea(self, heights):
        # Using a Stack
        # Time O(n), Space O(n)
        
        # We will use a stack based algorithm to solve this problem
        
        # 1. Add to the stack if the current height is greater than 
        #    or equal to the top of the stack.
        # 2. Otherwise, pop from the stack UNTIL a height less than
        #    or equal to the current height is found.
        # 3. We will update the area every time we pop from the
        #    stack as follows:
        #           top = stack.pop()
        #           if stack is empty:
        #               area = input[top] * i
        #           else:
        #               area = input[top] * (i - stack[-1] - 1)
        
        stack, max_area, n = [], 0, len(heights)
        
        for i in range(n):
            while stack and heights[i] < heights[stack[-1]]:
                top = stack.pop()
                if stack:
                    area = heights[top] * (i - stack[-1] - 1)
                else:
                    area = heights[top] * i
                max_area = max(area, max_area)
            
            stack.append(i)
            
        # i = n now
        while stack:
            top = stack.pop()
            if stack:
                area = heights[top] * (n - stack[-1] - 1)
            else:
                area = heights[top] * n
            max_area = max(area, max_area)
        
        return max_area        

