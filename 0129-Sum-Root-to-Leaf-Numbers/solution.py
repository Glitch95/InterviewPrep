# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def helper(root, s, curr):
    if root:
        curr = curr * 10 + root.val
        if not root.left and not root.right:
            s[0] += curr
        helper(root.left, s, curr)
        helper(root.right, s, curr)
        return s[0]
    return 0
        

class Solution:
    def sumNumbers(self, root):
        # # SOLUTION 1 - Recursive Preorder Traversal
        # # Time O(n), Space O(h)

        # # We can build the number starting from the root down
        # # When we get to a leaf we can add the number to
        # # the sum.

        # return helper(root, [0], 0)
        
        # SOLUTION 2 - Iterative Preorder Traversal
        if not root:
            return 0
        
        stack, s = [(root, 0)], 0
        
        while stack:
            node, curr = stack.pop()
            curr = curr * 10 + node.val
            
            if not node.right and not node.left:
                s += curr
                continue
            
            if node.right:
                stack.append((node.right, curr))
            
            if node.left:
                stack.append((node.left, curr))
        
        return s

