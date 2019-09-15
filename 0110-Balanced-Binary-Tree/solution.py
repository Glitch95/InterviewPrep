# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def helper(root):
    """Returns the height of the tree if it is balanced else -1."""
    if not root:
        return 0

    left, right = helper(root.left), helper(root.right)

    if left < 0 or right < 0:
        return -1
    elif abs(left-right) > 1:
        return -1
    else:
        return 1 + max(left, right)

class Solution:
    def isBalanced(self, root):
        # Solution 1 - Recursive Postorder Traversal
        # O(n) Time, O(1) Space
        return helper(root) >= 0

