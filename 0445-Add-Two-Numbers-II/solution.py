# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        
        # We can reverse the 2 lists and do as we did in Add Two Number I
        # However, we will try a different approach here.
        # Lets get the values represented
        # Do the addition and
        # Convert the result into its list representation.
        
        val1 = val2 = 0
        
        while l1:
            val1, l1 = val1 * 10 + l1.val, l1.next
            
        while l2:
            val2, l2 = val2 * 10 + l2.val, l2.next
        
        val3 = val1 + val2
        
        # Handle case where result is 0
        if val3 == 0:
            return ListNode(val3)
        
        l3 = None
        while val3:
            node = ListNode(val3 % 10)
            node.next = l3
            l3 = node
            val3 //= 10
        
        return l3

