# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def bst(arr, start, end):
    if start > end:
        return None
    if start == end:
        return TreeNode(arr[start])
    else:
        # NOTE: (start+end+1)//2 will ensure the extra node (if any) is in the left subtree
        # However, (start+end)//2 also works (extra node in right subtree)
        mid = (start+end+1) // 2
        root = TreeNode(arr[mid])
        root.left = bst(arr, start, mid-1)
        root.right = bst(arr, mid+1, end)
        return root

class Solution:
    def sortedListToBST(self, head):
        # Solution 1 - Recursive Preorder Divide and Conquer
        # O(n) Time, O(n) Space

        # We first convert the linked list to an array and
        # then recursively use the middle of the array
        # as the corresponding subtree root.

        arr = []
        while head:
            arr.append(head.val)
            head = head.next

        return bst(arr, 0, len(arr)-1)

