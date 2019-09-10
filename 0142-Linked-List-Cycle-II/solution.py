# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head):
        
        # To detect where the cycle begins we will again
        # use a slow and a fast pointer.
        
        # However we will use some maths to figure out where
        # the start of the cycle is.
        
        # Let:
        # x - the distance from the start of the list to the start of the cycle.
        # y - the distance from the start of the cycle to the meeting point.
        # z - the distance from the meeting point to the start of the cycle.
        
        # Distance traveled by fast pointer = 2 * Distance travelled by slow pointer.
        # x + y + z + y = 2 * (x + y)
        # x + 2y + z = 2x + 2y
        # z = x
        
        # So if we start a pointer at the start of the list
        # and another at the meeting point.
        # If we move these 2 pointers forward in lock step
        # then the point at which they meet will be
        # the start of the cycle.
        
        slow = fast = head
        
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow is fast:
                fast = head
                while fast is not slow:
                    fast, slow = fast.next, slow.next
                return fast
        
        return None

