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
        # O(n) Time, O(h) = O(n) Space

        # This solution was inspired by Lucy Lu from summer class.
        # postorder(root)

        # SOLUTION 2 - Iterative Stack Approach
        # O(n) Time, O(n) Space

        # This solution was inspired by Henchhing.
        # In order to see the intuition for this approach,
        # lets look at a simply example.

        """
          2                2
         / \        --->    \
        3   4                3
                              \
                               4

        It appears that we take the left sub tree of the root (3), its right sub tree and
        we make the root's right subtree (4) the right subtree of its left sub tree.

        In order, to keep a reference to the right subtrees we can use a stack.

        Lets look at a slightly more complex example:

        Initially
            1           root = 1
           / \          stack = []
          2   5
         / \   \
        3   4   6

        There is a right child so we add it to the stack
            1           root = 1
           / \          stack = [5]
          2   5
         / \   \
        3   4   6

        There is a left child so we:
        1. Make the left sub tree the right child of the root
        2. Set the left subtree to None
        3. Set root to its right subtree
            1           root = 2
           / \          stack = [5]
          N   2
             / \
            3   4

        There is a right child, so we add it to the stack.
            1           root = 2
           / \          stack = [5, 4]
          N   2
             / \
            3   4

        There is a left child so we:
        1. Make the left sub tree the right child of the root
        2. Set the left subtree to None
        3. Set root to its right subtree
            1           root = 3
           / \          stack = [5, 4]
          N   2
             / \
            N   3

        There is no left or right child, so we:
        1. Set the right child of the root to the popped element from the stack.
        2. Set the left subtree to None
        3. Set the root to it's right subtree.

            1           root = 4
           / \          stack = [5]
          N   2
             / \
            N   3
               / \
              N   4

        There is no left or right child, so we:
        1. Set the right child of the root to the popped element from the stack.
        2. Set the left subtree to None
        3. Set the root to it's right subtree.

            1           root = 5
           / \          stack = []
          N   2
             / \
            N   3
               / \
              N   4
                 / \
                N   5
                     \
                      6

        There is a right child so we add it to the stack.

            1           root = 5
           / \          stack = [6]
          N   2
             / \
            N   3
               / \
              N   4
                 / \
                N   5
                     \
                      6

        There is no left child so we:
        1. Set the right child of the root to the popped element from the stack.
        2. Set the left subtree to None
        3. Set the root to it's right subtree.

            1           root = 6
           / \          stack = []
          N   2
             / \
            N   3
               / \
              N   4
                 / \
                N   5
                   / \
                  N   6

        There is no right child left child or stack, so we
        1. Set the left child to None
        2. Set root to its right child

            1           root = N
           / \          stack = []
          N   2
             / \
            N   3
               / \
              N   4
                 / \
                N   5
                   / \
                  N   6
                     / \
                    N   N

        Since root is None, the algorithm terminates.
        """
        # stack = []
        # while root:
        #     if root.right:
        #         stack.append(root.right)

        #     if root.left:     # if there is right child
        #         root.right = root.left
        #     elif stack:       # get the node from the stack
        #         root.right = stack.pop()
        #     root.left = None
        #     root = root.right

        # SOLUTION 3 - Inspired by Morris Traversal Algorithm
        # Same idea as solution 2 except we do the restructuring in a way to avoid
        # using extra space. ie. we make the root's right subtree the right subtree of the
        # root's left subtree; then we make the left subtree the root's right subtree.

        # O(n) Time, O(1) Space

        # TIME COMPLEXITY ANALYSIS
        # This is a bit slower than the stack solution but the Time Complexity is still O(n)
        # You're moving the root pinter over all nodes and for each one potentially dive down deep
        # into its left subtree, using the curr pointer, so one might think it's more than O(n) time.
        # But, a long path down the left subtree immediately pays off, as you then insert that
        # entire path into the "right border" of the whole tree, where root will walk over it,
        # but curr will never have to walk over it again.
        # To put it differently: Every node is visited by root exactly once and by curr at most once,
        # and the runtime is proportional to the number of steps taken by root and curr, so O(n) overall.

        while root:
            if root.left:
                curr = root.left
                while curr.right:
                    curr = curr.right
                curr.right = root.right
                root.right = root.left
            root.left = None
            root = root.right

