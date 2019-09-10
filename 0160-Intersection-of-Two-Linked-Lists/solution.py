# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getLen(self, head):
        curr, length = head, 0
        while curr:
            curr, length = curr.next, length + 1
        return length
    
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        # We will try to find the first position where the nodes of the list are the same.
        # To do this we will traverse the lists in lock step after aligning them so that
        # their last nodes will be reached at the same time.
        # To perform this alignment, we will use the difference between the lengths of the lists.
        
        lenA, lenB = self.getLen(headA), self.getLen(headB)
        
        if lenB > lenA:
            for _ in range(lenB-lenA):
                headB = headB.next
        else:
            for _ in range(lenA-lenB):
                headA = headA.next
        
        while headA:
            if headA is headB:
                return headA
            headA, headB = headA.next, headB.next
            
        return None

