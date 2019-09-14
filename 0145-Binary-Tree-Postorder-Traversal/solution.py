# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        # Solution 1 - Using 2 stacks
        # Second stack contains the post order traversal in reverse.
        # stack1 = [root]
        # stack2 = []

        # if not root:
        #     return stack2

        # while stack1:
        #     node = stack1.pop()
        #     stack2.append(node)

        #     left_child = node.left
        #     right_child = node.right

        #     if left_child:
        #         stack1.append(left_child)

        #     if right_child:
        #         stack1.append(right_child)

        # return [x.val for x in stack2[::-1]]

        # Solution 2 - Using 1 Stack
        # and Modifying the Tree to avoid infinite loop
        # post_order = []

        # if not root:
        #     return post_order

        # stack = [root]

        # while stack:
        #     node = stack[-1]

        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        #     if not node.left and not node.right:
        #         stack.pop()
        #         post_order.append(node.val)

        #     # After adding children to the stack
        #     # remove them to avoid inifinte loop
        #     node.left = None
        #     node.right = None

        # return post_order

        # Solution 3 - Using 1 Stack with extra information
        # to avoid modifying the tree.

        post_order = []

        if not root:
            return post_order

        stack = [(root, False)]     # (node, visited - considered children already)

        while stack:
            node, visited = stack.pop()

            if visited:
                post_order.append(node.val)
            else:
                stack.append((node, True))

                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))

        return post_order

