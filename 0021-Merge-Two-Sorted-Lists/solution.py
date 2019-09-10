# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        # What we need to do here is perform the merge operation
        # of merge sort. 
        # We will make use of the dummy head technique to 
        # nicely handle edge cases.
        
        head = tail = ListNode(None)
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next, l1 = l1, l1.next
            else:
                tail.next, l2 = l2, l2.next
            tail = tail.next
        
        if l1:
            tail.next = l1
            
        if l2:
            tail.next = l2
        
        return head.next

