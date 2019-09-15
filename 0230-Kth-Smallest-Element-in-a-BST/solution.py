# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        # Controlled Recursion using
        # Iterative Inorder Traversal
        # O(n) Time, O(n) Space

        stack, curr = [], root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit
            curr = stack.pop()
            k -= 1
            if not k:
                return curr.val

            curr = curr.right

        # Unreachable if k is valid
        return -1

