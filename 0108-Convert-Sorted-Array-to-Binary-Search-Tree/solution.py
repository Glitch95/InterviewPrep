# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bst(nums, start, end):
    if start < end:
        # NOTE: (start + end + 1) // 2 will ensure that left nodes
        # are filled first.
        # However, (start + end) // 2 also works (right nodes have priority)
        mid = (start + end) // 2
        root = TreeNode(nums[mid])
        root.left = bst(nums, start, mid-1)
        root.right = bst(nums, mid+1, end)
        return root
    elif start == end:
        return TreeNode(nums[start])
    else:
        return None

class Solution:
    def sortedArrayToBST(self, nums):
        # Solution 1 - Recursive Divide and Conquer
        # Use the middle of the array as the root
        n = len(nums)
        return bst(nums, 0, n-1)

