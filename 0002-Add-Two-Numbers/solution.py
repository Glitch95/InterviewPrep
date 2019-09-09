class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """ The approach here is the same as addition by hand. """
        carry = 0
        l3 = tail = None

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            sum = x + y + carry
            carry = sum // 10

            if l3:
                tail.next = ListNode(sum % 10)
                tail = tail.next
            else:
                l3 = tail = ListNode(sum % 10)

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        if carry:
            tail.next = ListNode(carry)

        return l3

