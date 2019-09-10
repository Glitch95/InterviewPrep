class Solution:
    def swapPairs(self, head):
        # If 0 or 1 node
        if not head or not head.next:
            return head
        
        # We will use a dummy head to handle the edge cases
        sentinel = ListNode(None)
        sentinel.next =  head
        
        # Let's visualize the logic
        # | 1 | 2 | 3 | 4 |
        
        # | D | 1 | 2 | 3 | 4 |
        #   p   c   n
        
        # p -> n
        # c -> n.next
        # n -> c
        
        # | D | 2 | 1 | 3 | 4 |
        #   p   n   c
        
        # Incrementing the pointers
        # p = c
        # c = c.next
        prev, curr, next = sentinel, head, head.next
        
        while curr and curr.next:
            next = curr.next
            
            prev.next = next
            curr.next = next.next
            next.next = curr
            
            prev, curr = curr, curr.next
        
        return sentinel.next
            
