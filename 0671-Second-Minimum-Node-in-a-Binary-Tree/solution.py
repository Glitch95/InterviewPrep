# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def dfs(node, mins):
    if node:
        if mins[0] < node.val < mins[1]:
            mins[1] = node.val
        elif node.val == mins[0]:
            dfs(node.left, mins)
            dfs(node.right, mins)
    return mins[1] if mins[1] < float('inf') else -1


class Solution:
    def findSecondMinimumValue(self, root):
        # Controlled recursion (stopping after visiting the second node)
        # using an iterative inorder traversal seems intuitive 
        # but WON'T work in this case becuase the tree is
        # a special type of binary tree and not a 
        # binary search tree.
        
        # A simple way to solve the problem is to 
        # traverse the tree keeping track of the 2 minimum 
        # values found.
        
        # SOLUTION 1 - Recursive Preorder Traversal
        # O(n) Time, O(h) = O(n) Space
        # if not root:
        #     return -1
        # return dfs(root, [root.val, float('inf')])
        
        # SOLUTION 2 - Iterative Preorder traversal.
        # O(n) Time, O(n) Space
        
        if not root:
            return -1
        
        stack, min1, min2 = [root], root.val, float('inf')
        
        while stack:
            
            node = stack.pop()
            
            # Visit()
            if min1 < node.val < min2:      # node.val will not be < min1
                min2 = node.val             # due to the special tree property
            
            # Since the root is always the min of its left and right
            # we only need to consider the case where the
            # current val == the min val (i.e the real second min val)
            # could be in that sub tree.
            if node.val == min1:
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return min2 if min2 < float('inf') else -1        

