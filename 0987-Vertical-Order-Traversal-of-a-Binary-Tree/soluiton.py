from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def preorder(root, x, y, nodes):
    if root:
        nodes[x][y].append(root.val)
        preorder(root.left, x-1, y+1, nodes)
        preorder(root.right, x+1, y+1, nodes)

class Solution:
    def verticalTraversal(self, root):
        # Solution 1 - Recursive Preorder Traversal
        # O(nlogn)Time , O(n) Space
        # One idea is to traverse the tree once and keeping track of
        # the horizontal distance with respect to root.

        # The above idea would work fine if not for the following
        # requirement:
        # "If two nodes have the same position, then the value of the node that
        # is reported first is the value that is smaller."

        # In order to satisfy this condition we will need to keep track of the
        # vertical as will as the horizontal distance with respect to the root.
        # We will then sort the nodes by x, then y and then value.

        nodes = defaultdict(lambda: defaultdict(list))
        preorder(root, 0, 0, nodes)

        res = []
        for x in sorted(nodes):
            vert_level = []
            for y in sorted(nodes[x]):
                vert_level += sorted(nodes[x][y])
            res.append(vert_level)
        return res

