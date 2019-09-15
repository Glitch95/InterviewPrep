# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        # Solution 1 - Iterative Level Order Traversal
        # O(n) Time, O)(n) Space

        if not root:
            return []

        curr_level, next_level, max_vals, = [root], [], []

        while curr_level:
            curr_max = float('-inf')
            for node in curr_level:
                curr_max = max(curr_max, node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            max_vals.append(curr_max)
            curr_level, next_level = next_level, []

        return max_vals

