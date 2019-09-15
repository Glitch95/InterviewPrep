from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def postorder(root, counter):
    if not root:
        return 0

    left_sum, right_sum = postorder(root.left, counter), postorder(root.right, counter)
    s = left_sum + root.val + right_sum

    counter[s] += 1

    return s


class Solution:
    def findFrequentTreeSum(self, root):
        # Solution 1 - Recursive Postorder traversal and Map
        # We use the map to keep a count of the sums
        # and then return the sums with the maximum count

        if not root:
            return []

        counter = defaultdict(int)
        postorder(root, counter)
        max_count = max(counter.values())
        return [key for key, count in counter.items() if count == max_count]

