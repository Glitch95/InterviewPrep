# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        # Let's we a 2 pointer techinque to keep track of the start and end 
        # of each distinct region.
        # We will also use a dummy head to nicely handle edge cases.
        # A region being a section of the list with all nodes having the same value.
        
        # Let's try to visualize this
        
        # | C | D | 1 | 2 | 3 | 3 | 4 | 4 | 5 |     c != n
        #   p   c   n 
        
        # | C | D | 1 | 2 | 3 | 3 | 4 | 4 | 5 |     c != n
        #       p   c   n
        
        # | C | D | 1 | 2 | 3 | 3 | 4 | 4 | 5 |     c != n    
        #           p   c   n
        
        # | C | D | 1 | 2 | 3 | 3 | 4 | 4 | 5 |     c == n    
        #               p   c   n
        
        # | C | D | 1 | 2 | 3 | 3 | 4 | 4 | 5 |     c != n and c.next != n
        #               p   c       n
        
        # | C | D | 1 | 2 | 4 | 4 | 5 |     p.next = n, c = p.next, n = c.next
        #               p   c   n
        
        # | C | D | 1 | 2 | 4 | 4 | 5 |     c == n
        #               p   c   n
        
        # | C | D | 1 | 2 | 4 | 4 | 5 |     c != n and c.next != n
        #               p   c       n
        
        # | C | D | 1 | 2 | 4 | 4 | 5 |     p.next = n
        #               p   c       n
        
        # | C | D | 1 | 2 | 5 |
        #               p
        
        n1, n2 = ListNode(None), ListNode(None)
        n1.next, n2.next = n2, head
        
        prev = n1
        while prev.next and prev.next.next:
            curr, next = prev.next, prev.next.next
            
            while curr and next and curr.val == next.val:
                next = next.next
            
            if curr.next is not next:
                prev.next = next
            else:
                prev = prev.next
        
        return n1.next.next  
        
