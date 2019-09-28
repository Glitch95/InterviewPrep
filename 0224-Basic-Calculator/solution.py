def eval_expr(stack):
    res = stack.pop() if stack else 0

    # Evaluate the expression till we get corresponding ')'
    while stack and stack[-1] != ')':
        sign = stack.pop()
        if sign == '+':
            res += stack.pop()
        else:
            res -= stack.pop()
    return res

class Solution:
    def calculate(self, s):
        # Solution 1 - Stack and String Reversal
        # O(n) Time, O(n) Space

        # We push the elements of the expression one by one onto the stack
        # until we get a closing bracket ')'. Then we pop the elements from
        # the stack one by one and evaluate the expression on-the-go.
        # This is done till we find the corresponding '(' opening bracket.
        # However, if you notice the way we calculate the final answer,
        # you will realize that we actually process the values from right
        # to left whereas it should be the other way around.
        # To solve this problem we will iterate over the string in reverse order.

        n, stack = len(s), []
        i = n-1
        while i >= 0:
            if s[i].isdigit():  # Form the numeric operand
                j = i
                while j > 0 and s[j-1].isdigit():
                    j -= 1
                stack.append(int(s[j:i+1]))
                i = j
            elif s[i] == '(':   # Evaluate until we get a ')'
                res = eval_expr(stack)
                stack.pop()     # Remove ')' from stack
                stack.append(res)
            elif s[i] != ' ':   # '+' or '-' or ')'
                stack.append(s[i])
            i -= 1
        return eval_expr(stack)

