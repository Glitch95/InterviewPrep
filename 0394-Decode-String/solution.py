from collections import deque

class Solution:
    def decodeString(self, s):
        
        # Solution 1 - Using a Stack
        # O(n) Time, O(n) Space
        
        # The idea is to keep track of the string and number we've seen so far.
        # Once we encounter a '[' we save the current string and number on the stack.
        # when we encounter a ']' expand the current string using curr string * curr num
        # and set it to the previous string + the expanded current string.
        stack, curr_num, curr_str = [], 0, ''
        for c in s:
            if c.isdigit():
                curr_num = curr_num * 10 + int(c)
            elif c == '[':
                stack.append(curr_str)
                stack.append(curr_num)
                curr_num, curr_str = 0, ''
            elif c == ']':
                curr_num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + curr_str * curr_num
                curr_num = 0
            else:
                curr_str += c
        return curr_str         
 
