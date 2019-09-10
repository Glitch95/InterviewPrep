# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        # We will use the 2 pointer technique
        
        # Let's visualize
        
        # Advance pointers to get this state
        # | 1 | 2 | 3 | 4 | 5 | None |  k = 2
        #           l       r
        
        # Implies r = l + k
        
        # Save new head
        # n_head = l.next
        
        # Then
        # r -> head
        # l -> None
        
        # Return n_head
        
        # If 0 or 1 node
        if not head or not head.next:
            return head
        
        # Get the length of the list
        curr, length = head, 0
        while curr:
            curr, length = curr.next, length + 1
        
        # Handle edge case values of k
        k = k % length       
        if k < 1:
            return head
        
        left = right = head
        
        for _ in range(k):
            right = right.next
        
        while right.next:
            left, right = left.next, right.next
        
        new_head, left.next, right.next = left.next, None, head

        return new_head
        
