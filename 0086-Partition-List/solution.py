# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head, x):
        # We can use the 2 pointer technique to keep track of 2 smaller lists,
        # which we will build up as we traverse the original list.
        # We will also make use of the dummy head technique to
        # nicely handle edge cases.
        
        if not head or not head.next:
            return head
        
        l_head = l_tail = ListNode(None)
        ge_head = ge_tail = ListNode(None)
        
        
        curr = head
        while curr:
            if curr.val < x:
                l_tail.next = curr
                l_tail = l_tail.next
            else:
                ge_tail.next = curr
                ge_tail = ge_tail.next
            
            curr = curr.next
        
        l_tail.next, ge_tail.next = ge_head.next, None
        
        return l_head.next

