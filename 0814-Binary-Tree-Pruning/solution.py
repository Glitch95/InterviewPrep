# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        # SOLUTION 1 - Recursive Post Order Traversal
        # We remove zeros that are leaves,
        # then check the new leaves for zeroes
        # and so on.

        if root:
            left, right = self.pruneTree(root.left), self.pruneTree(root.right)

            # Visit() - If left is a leaf and is a 0
            if left and not left.left and not left.right and left.val == 0:
                root.left = None
            if right and not right.left and not right.right and right.val == 0:
                root.right = None

        return root

