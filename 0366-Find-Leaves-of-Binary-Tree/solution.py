# Given a binary tree, collect a tree's nodes as if you were doing this:
# Collect and remove all leaves, repeat until the tree is empty.

# Example:
#       1
#      / \
#     2   3
#    / \
#   4   5

# Returns [4, 5, 3], [2], [1].

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def getHeight(root, leaves):
    if not root:
        return -1

    height = max(getHeight(root.left, leaves), getHeight(root.right, leaves)) + 1

    if height == len(leaves):
        leaves.append([root.val])
    else:
        leaves[height].append(root.val)
    return height

r = TreeNode(1)
rleft = r.left = TreeNode(2)
rright = r.right = TreeNode(3)
rleft.left = TreeNode(4)
rleft.right = TreeNode(5)

def findLeaves(root):
    leaves = []
    getHeight(root, leaves)
    return leaves

print(findLeaves(None))
print(findLeaves(r))

