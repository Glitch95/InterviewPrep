"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head):
        if not head:
            return None
        
        map = {}
        curr = head
        while curr:
            map[curr] = Node(curr.val, None, None)
            curr = curr.next
            
        for node, copy in map.items():
            copy.next = None if not node.next else map[node.next]
            copy.random = None if not node.random else map[node.random]
            
        return map[head]
    
#         # We can also achieve this in O(1) space
#         # Using the existing pointers to make the temporary mapping
    
#         # Sanity check
#         if not head:
#             return head
        
#         # First we clone all the nodes and next pointers
#         c_head = c_tail = Node(None, None, None)
#         curr = head
#         while curr:
#             c_tail.next = Node(curr.val, None, None)
#             curr, c_tail = curr.next, c_tail.next
#         c_head = c_head.next
            
#         # Then we iterate over the 2 lists in lock step,
#         # pointing the next pointers of original nodes to cloned nodes
#         # and the random pointer of cloned nodes to original nodes.
#         # This in effect is a bidirectional mapping
#         curr, c_curr = head, c_head
#         while curr:
#             next = curr.next
#             curr.next = c_curr
#             c_curr.random = curr
#             curr, c_curr = next, c_curr.next
        
#         # We then traverse over the cloned lists, and point its
#         # random pointers to the cloned random node, using the mapping.
#         curr = c_head
#         while curr:
#             curr.random = curr.random.random.next
#             curr = curr.next
        
#         return c_head

