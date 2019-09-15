from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def postorder(root, counter, roots):
    if not root:
        idn = 'null'
    else:
        left, right = postorder(root.left, counter, roots), postorder(root.right, counter, roots)

        idn = ','.join([str(root.val), left, right])
        if counter[idn] < 2:
            counter[idn] += 1
            if counter[idn] > 1:
                roots.append(root)

    return idn

class Solution:
    def findDuplicateSubtrees(self, root):
        # Recursive Postorder Traversal
        # We will represent each subtree by a unique string
        # namely, 'root.val,root.left.str,root.right.string'
        # We than keep a map of these unique identifiers
        # an return all the ones with count > 1
        counter, roots = defaultdict(int), []
        postorder(root, counter, roots)
        return roots

