# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root, sum):
        # Soltion 1 - Recursive Preorder Traversal
        if not root:
            return False
        if not root.left and not root.right:
            return root.val == sum

        target = sum - root.val
        return self.hasPathSum(root.left, target) or self.hasPathSum(root.right, target)

