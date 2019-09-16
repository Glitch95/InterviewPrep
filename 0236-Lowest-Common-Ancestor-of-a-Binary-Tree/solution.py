# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def postorder(root, p, q, lca):
    if not root:
        return False

    left = postorder(root.left, p, q, lca)
    right = postorder(root.right, p, q, lca)

    mid = root is p or root is q

    # If any of the 3 flags (left, mid, right) are True
    if mid + left + right == 2:
        lca[0] = root

    # Return True if either of the flags are True
    return mid or left or right


class Solution:
    def lowestCommonAncestor(self, root, p, q):
        # Solution 1 - Post order traversal
        lca = [None]
        postorder(root, p, q, lca)
        return lca[0]

