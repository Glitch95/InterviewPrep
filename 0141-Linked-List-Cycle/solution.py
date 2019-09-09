class Solution:
    def hasCycle(self, head):
        """ Floyd's Tortoise and Hare

            Another approach is using a Hash Map
            or Set to keep track of nodes we have
            visited before.
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head.next

        while fast and fast.next:
            if slow == fast:
                return True
            fast = fast.next.next
            slow = slow.next

        return False

