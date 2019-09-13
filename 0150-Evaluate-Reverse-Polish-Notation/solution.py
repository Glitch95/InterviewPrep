class Solution:
    def evalRPN(self, tokens):
        # SOLUTION 1 - Stack
        # O(n) Time O(n) Space

        operators, stack = set('+-*/'), []

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else:
                y, x = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(x + y)
                elif token == '-':
                    stack.append(x - y)
                elif token == '*':
                    stack.append(x * y)
                else:
                    # Required: Division between two integers should truncate toward zero.
                    # Note: Be careful with the division
                    # 5 // 10 = 0
                    # 5 // -10 = - 1
                    stack.append(int(x / y))

        return stack[0]
    
        # # A more pythonic but less efficient code of the 
        # # same approach:
        
        # operators, stack = set('+-*/'), []

        # for token in tokens:
        #     if token not in operators:
        #         stack.append(token)
        #     else:
        #         y, x = stack.pop(), stack.pop()
        #         stack.append(str(int(eval(x + token + y))))

        # return stack[0]

