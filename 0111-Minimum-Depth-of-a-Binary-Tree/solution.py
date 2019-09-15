# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def postorder(root):
    if not root:
        return float('inf')
    if not root.left and not root.right:
        return 1
    left_depth, right_depth = postorder(root.left), postorder(root.right)
    return 1 + min(left_depth, right_depth)

class Solution:
    def minDepth(self, root):
        # SOLUTION 1 - Recursive Postorder Traversal
        # This solution was inspired by Lucy Lu from summer class :)
        # O(n) Time, O(h) = O(n) Space

        # if not root:
        #     return 0
        # return postorder(root)

        # SOLUTION 2 - Iterative Level Order Traversal
        # Allows us to return once we find the 1st leaf
        if not root:
            return 0

        curr_level, next_level, depth = [root], [], 0

        while curr_level:
            depth += 1
            for node in curr_level:
                if not node.left and not node.right:
                    return depth
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            curr_level, next_level = next_level, []

        # Unreachable

