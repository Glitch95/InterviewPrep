from collections import deque

def eval_expr(stack):
    res = stack.pop()

class Solution:
    def decodeString(self, s):

        # Solution 1 - Using a Stack
        # O(n) Time, O(n) Space

        # The idea is to keep track of the string and number we've seen so far.
        # Once we encounter a '[' we save the current string and number on the stack.
        # when we encounter a ']' expand the current string using curr string * curr num
        # and set it to the previous string + the expanded current string.

        # stack, curr_num, curr_str = [], 0, ''
        # for c in s:
        #     if c.isdigit():
        #         curr_num = curr_num * 10 + int(c)
        #     elif c == '[':
        #         stack.append(curr_str)
        #         stack.append(curr_num)
        #         curr_num, curr_str = 0, ''
        #     elif c == ']':
        #         curr_num = stack.pop()
        #         prev_str = stack.pop()
        #         curr_str = prev_str + curr_str * curr_num
        #         curr_num = 0
        #     else:
        #         curr_str += c
        # return curr_str


        # Solution 2 - Stack
        # O(n) Time, O(n) Space

        # This approach is more intuitive and slightly more efficient than that
        # presented in Solution 1.

        # We push the elements of the tokens of the encoded string one by one
        # onto the stack until we encounter a closing bracket ']'.
        # We then we pop the elements from the stack one by one and evaluate
        # tokens one by one from the stack and concatenate them together, until
        # we encounter the corresponding open bracket '['.
        # We pop the open bracket and the number before it. This allows us to expnad
        # the substring and place the result back on the stack.

        i, n, stack = 0, len(s), []

        while i < n:
            if s[i].isdigit():
                j = i
                while j < n and s[j].isdigit():
                    j += 1
                num = int(s[i:j])
                stack.append(num)
                i = j
            elif s[i].isalpha():
                j = i
                while j < n and s[j].isalpha():
                    j += 1
                substr = s[i:j]
                stack.append(substr)
                i = j
            elif s[i] == ']':   # Eval until we reach the corresponding '['
                queue = deque()
                while stack[-1] != '[':
                    queue.appendleft(stack.pop())
                substr = ''.join(queue)
                stack.pop()     # Remove '['
                num = stack.pop()
                stack.append(num * substr)
                i += 1
            else:               # '[' put on the stack
                stack.append(s[i])
                i += 1

        return ''.join(stack)

