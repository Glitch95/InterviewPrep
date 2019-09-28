# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def preorder(root, sum, path, solutions):
    if not root:
        return

    # Update path
    path.append(root.val)

    if not root.left and not root.right and sum == root.val:    # Leaf
        solutions.append(path.copy())

    rem = sum - root.val
    preorder(root.left, rem, path, solutions)
    preorder(root.right, rem, path, solutions)

    # Restore the path
    path.pop()


class Solution:
    def pathSum(self, root, sum):
        # Recursive Preorder Traversal / Backtracking
        # O(n) Time, O(h) = O(n) Space

        path, solutions = [], []
        preorder(root, sum, path, solutions)
        return solutions

