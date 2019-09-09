class Solution:
    def oddEvenList(self, head):
        """ We will build up 2 separate lists (an odd and
        an even list) as we iterate over the list.
        Then we will concatenate the even list to the odd
        list to get the solution. """

        if not head or not head.next:
            return head

        oddHead = oddTail = head
        evenHead = evenTail = head.next

        while evenTail and evenTail.next:
            oddTail.next = evenTail.next
            oddTail = oddTail.next
            evenTail.next = oddTail.next
            evenTail = evenTail.next

        oddTail.next = evenHead

        return oddHead

