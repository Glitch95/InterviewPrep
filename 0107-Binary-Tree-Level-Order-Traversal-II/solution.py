from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        # Solution 1 - Iterative Level Order Traversal
        if not root:
            return []

        queue, curr_level, next_level = deque(), [root], []

        while curr_level:
            queue.appendleft([x.val for x in curr_level])

            for node in curr_level:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            curr_level, next_level = next_level, []

        return queue

