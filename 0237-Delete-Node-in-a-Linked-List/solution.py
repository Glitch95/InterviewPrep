class Solution:
    def deleteNode(self, node):
        """ Given only access to the node to be deleted,
        the idea is to place the next node's value in the
        current node and delete the next node.

        An edge case being the case where the node to be
        deleted is the tail itself. """

        node.val = node.next.val
        node.next = node.next.next

