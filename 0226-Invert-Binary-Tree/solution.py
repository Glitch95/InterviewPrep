from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root):
        # Solution 1 - Recursive Preorder Traversal
        # O(n) Time O(1) Space
        # if root:
        #     root.left, root.right = root.right, root.left
        #     self.invertTree(root.left)
        #     self.invertTree(root.right)
        # return root

        # Solution 2 - Iterative Level Order Traversal
        # O(n) Time O(n) Space
        # curr_level, next_level = [root], []
        # while curr_level:
        #     for node in curr_level:
        #         if node:
        #             node.left, node.right = node.right, node.left
        #             next_level += [node.left, node.right]
        #     curr_level, next_level = next_level, []
        # return root

        # Solution 3 - Iterative Beadth First Traversal
        # O(n) Time, O(n) Space
        if not root:
            return root

        queue = deque()
        queue.append(root)

        while queue:
            node = queue.popleft()

            node.left, node.right = node.right, node.left

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

