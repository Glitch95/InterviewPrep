# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def postorder(s, t):
    if not s:
        return not t
    # The order of this boolean condition determines if it is
    # a preorder, postorder or inorder traversal.
    # (Specifically the placement of `preorder(s, t)` for the comparison)
    # For this problem test suite, postorder is the fastest :)
    if postorder(s.left, t) or postorder(s.right, t) or preorder(s, t):
        return True
    return False

def preorder(s, t):
    """Preorder comparison of 2 trees."""
    if not s and not t:
        return True
    if not s or not t:
        return False
    return s.val == t.val and preorder(s.left, t.left) and preorder(s.right, t.right)

class Solution:
    def isSubtree(self, s, t):
        # SOLUTION 1 - Recursive Postorder Traversal
        # with Recursive Preorder Lockstep Comparison
        return postorder(s, t)

