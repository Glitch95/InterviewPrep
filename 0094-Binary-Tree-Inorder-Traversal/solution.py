# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root):
        result, stack, curr = [], [], root

        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left

            # Visit()
            curr = stack.pop()
            result.append(curr.val)

            curr = curr.right

        return result

