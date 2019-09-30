# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def postorder(root):
    if not root:
        return (0, 0)

    left, right = postorder(root.left), postorder(root.right)

    # If we rob the root
    rob_root = root.val + left[1] + right[1]

    # If we don't rob the root
    rob_subs = max(left) + max(right)    # Max of vals if we rob the roots of subtrees or not

    return rob_root, rob_subs


class Solution:
    def rob(self, root):
        # Solution 1 - Recursive Post Order Traversal
        # O(n) Time, O(h) = O(n) Space

        # The main idea is to have the recursion return both the max value
        # if the root is robbed; and the max value if the root is not robbed.

        return max(postorder(root))

