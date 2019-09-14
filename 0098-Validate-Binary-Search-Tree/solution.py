# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def valid(node, lower=float('-inf'), upper=float('inf')):
    if not node:
        return True

    val = node.val

    if val <= lower or val >= upper:
        return False

    if not valid(node.right, val, upper):
        return False

    if not valid(node.left, lower, val):
        return False

    return True

class Solution:
    def isValidBST(self, root):
        
        # Solution 1 - Recursive Preorder
        # return valid(root)
        
        # Solution 2 - Iterative Preorder
        if not root:
            return True
        
        stack = [(root, float('-inf'), float('inf'))]
        
        while stack:
            node, lower, upper = stack.pop()
            val = node.val
            
            if val <= lower or val >= upper:
                return False
            if node.right:
                stack.append((node.right, val, upper))
            if node.left:
                stack.append((node.left, lower, val))
        
        return True

