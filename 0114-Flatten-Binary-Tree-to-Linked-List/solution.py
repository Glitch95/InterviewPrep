# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def postorder(root):
    """Return the head, tail of the linked list."""
    if not root:
        return (None, None)

    if not root.right and not root.left:
        return (root, root)

    left_head, left_tail = postorder(root.left)
    right_head, right_tail = postorder(root.right)

    # Using right pointer as next pointer
    head = tail = root
    root.left = root.right = None
    if left_head:
        tail.right = left_head
        tail = left_tail
    if right_head:
        tail.right = right_head
        tail = right_tail
    return (root, tail)


class Solution:
    def flatten(self, root):
        """
        Do not return anything, modify root in-place instead.
        """

        # SOLUTION 1 - Recursive Postorder Traversal
        # This solution was inspired by Lucy Lu from summer class :)
        postorder(root)

