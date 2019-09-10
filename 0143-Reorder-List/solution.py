# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from math import ceil

class Solution:
    def length(self, head):
        """ Returns the length of the list. """
        length, curr = 0, head
        while curr:
            length, curr = length + 1, curr.next
        return length

    def split(self, head):
        """ Splits a list in 2.
        The first list is larger if number of elements is odd. """
        prev = head
        for _ in range(ceil(self.length(head)/2)-1):
            prev = prev.next
        head2 = prev.next
        prev.next = None
        return head, head2

    def reverse(self, head):
        """ Reverses the list. """
        prev, curr = None, head
        while curr:
            next = curr.next
            curr.next = prev
            prev, curr = curr, next
        return prev
    
    def interleave(self, head1, head2):
        """ Interleaves the 2 lists starting with elements from list 1 first
        (i.e. Assuming list1 is the larger list. """
        curr = head1
        while head2:
            next, next2 = curr.next, head2.next
            curr.next, head2.next = head2, next
            curr, head2 = next, next2
        return head1
        
    def reorderList(self, head):
        """
        Do not return anything, modify head in-place instead.
        """
        
        # We can achieve this by creating 2 smaller lists and then interleaving them
        # Reversing the second list and then interleaving them
        
        # If 0 or 1 node
        if not head or not head.next:
            return head
        
        head1, head2 = self.split(head)
        head2 = self.reverse(head2)
        return self.interleave(head1, head2)

