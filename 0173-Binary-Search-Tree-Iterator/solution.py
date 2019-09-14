# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Solution 1 - Sorted Array (Recursive Inorder Traversal)
# class BSTIterator:

#     def __init__(self, root):
#         self.queue = []
#         self.index = -1
#         self._inorder(root)
#         self.last_idx = len(self.queue) - 1

#     def _inorder(self, root):
#         if root:
#             self._inorder(root.left)
#             self.queue.append(root.val)
#             self._inorder(root.right)

#     def next(self):
#         """
#         @return the next smallest number
#         """
#         self.index += 1
#         return self.queue[self.index]

#     def hasNext(self) -> bool:
#         """
#         @return whether we have a next smallest number
#         """
#         return self.index < self.last_idx

# Solution 2 - Controlled Recursion (Iterative Inorder Traversal)
class BSTIterator:

    def __init__(self, root):
        self.stack = []

        # We initalize the stack with a call to the helper
        self._left_inorder(root)

    def _left_inorder(self, root):
        # Add all the elements of root's left most branch to the
        # stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        """
        node = self.stack.pop()
        if node.right:
            # Need to maintain invariant
            self._left_inorder(node.right)
        return node.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

