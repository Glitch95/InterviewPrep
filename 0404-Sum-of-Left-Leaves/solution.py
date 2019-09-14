# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def is_leaf(root):
    return not root.left and not root.right

def helper(root, s, left_child):
    if root:
        if left_child and is_leaf(root):
            s[0] += root.val
        helper(root.left, s, True)
        helper(root.right, s, False)    

def solve(root):
    s = [0]
    helper(root, s, False)
    return s[0]

class Solution:
    def sumOfLeftLeaves(self, root):
        # # SOLUTION 1 - Recursive Preorder
        # # We could have used any traversal algorithm
        # # I just decided to use preorder.
        # # Time O(n) 
        # # Space O(h) ; h - height of the tree

        # return solve(root)
        
        # SOLUTION 2 - Iterative Preorder    
        if not root:
            return 0
        
        s, stack = 0, [root]
        
        while stack:
            node = stack.pop()
            left_node, right_node = node.left, node.right
            
            if right_node:
                stack.append(right_node)
            
            if left_node:
                if not left_node.left and not left_node.right:    # If left child is a leaf
                    s += left_node.val
                else:
                    stack.append(left_node)
        return s

